import os
import json
from flask import Flask, redirect, render_template, request, url_for, flash

from werkzeug.security import check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

import openai
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('evaluate'))
        else:
            flash('Invalid login credentials!')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

def handle_exception(e):
    # Check if APIError
    if type(e) == openai.APIError:
        if e.http_status >= 500:
            flash("The OpenAI API service is temporarily down, please try again later. See https://status.openai.com/")
        elif e.http_status == 429:
            flash("Too many requests have been made to the OpenAI API, please wait a few minutes and try again. See https://help.openai.com/en/articles/6891839-api-error-code-guidance")
        else:
            flash("Error occurred. See https://help.openai.com/en/articles/6891839-api-error-code-guidance")
    else:
        if e:
            flash(str(e))
        else:
            flash("An error occurred.")

@app.route("/", methods=("GET", "POST"))
def index():
    return redirect(url_for("evaluate"))

@app.route("/code_evaluator", methods=("GET", "POST"))
def code_evaluator():
    if request.method == "POST":
        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": "You are a coding expert that will evaluate code and return revised code based on best practices, code quality, efficiency, and readability. Feel free to also add comments in the code."
                },
                {
                    "role": "user",
                    "content": request.form["prompt"]
                }
            ])

            # converts result string that looks like a Python dictionary into an actual Python dictionary/code
            data = response.choices[0].message.content
            # data = json.loads(response['choices'][0]['message']['content'])
            return render_template("code_evaluator.html", result=data)
        except Exception as e:
            handle_exception(e)
            return render_template("code_evaluator.html")
    else:
        return render_template("code_evaluator.html")


@app.route("/evaluate", methods=("GET", "POST"))
@login_required
def evaluate():
    if request.method == "POST":
        try:
            files = request.files.getlist("files")
            filenames = []
            results = []
            print(files)

            for file in files:
                if not file:
                    raise Exception("No file uploaded")

                filename = file.filename
                filenames.append(filename)

                # read text from file
                data = file.read()
                data = data.decode("utf-8")  # convert bytes to text

                # system_prompt = 'Replicate results for any coding language like pylint does on python code or jshint does on js. Each suggestion should be an object with keys "line", "category", "suggestion".'

                response = client.chat.completions.create(model="gpt-3.5-turbo",
                    temperature=0,
                    messages=[
                        {
                            "role": "system",
                            "content": 'Analyze the following python code. Include all suggestions as a JSON-compatible list of objects each with keys "line": X, "type": Y, "suggestion": Z }'
                        },
                        {
                            "role": "user",
                            "content": data
                        }
                    ])
                data = json.loads(response.choices[0].message.content)
                print(type(data), data)
                results.append(data)
            return render_template("evaluate.html", filenames=filenames, results=results)
        except Exception as e:
            print(e)
            handle_exception(e)
            return redirect(url_for("evaluate"))
    else:
        return render_template("evaluate.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)