from flask import Flask, redirect, render_template, request, url_for, flash, session
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import os
import json
import openai
from dotenv import load_dotenv
load_dotenv()

from utils import handleJSONDecodeError

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# 'extend_existing' allows redefining tables and columns
class User(UserMixin, db.Model):
  __tablename__ = 'user'
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(40), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)

  def set_password(self, password):
    self.password = generate_password_hash(password, method='scrypt')

  def check_password(self, password):
    return check_password_hash(self.password, password)

class Analysis(db.Model):
  __tablename__ = 'analysis'
  __table_args__ = {'extend_existing': True}
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  updated_at = db.Column(db.DateTime, nullable=False)
  filename = db.Column(db.String(255), nullable=False)
  data = db.Column(db.JSON, nullable=False)  # TODO: change to JSONB?

PROMPT = """Analyze the following code as if you are a computer science professor
whose goal is to identify critical errors in your students\' code.
Do not add suggestions on adding comments, docstrings, variable names, formatting, or indentation.
Make sure to look through the entire file.
Include the suggestions as a JSON-compatible list of objects each with keys "line": X, "type": Y, "suggestion": Z
Limit the final number of suggestions between 1 and 20 critical issues that you have identified.
"""

@login_manager.user_loader
def load_user(user_id):
  # TODO: Fix to Session.get?
  # LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
  return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    passwordRepeat = request.form.get('passwordRepeat')

    user = User.query.filter_by(username=username).first()
    if user:
      flash('Username already exists!')
    elif password != passwordRepeat:
      flash('Passwords do not match!')
    else:
      new_user = User(username=username)
      new_user.set_password(password)
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user)
      return redirect(url_for('evaluate'))
  return render_template('register.html')

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

@app.route("/api/deleteEval/<int:id>", methods=["GET", "POST"])
@login_required
def delete_eval(id):
  try:
    analysis = Analysis.query.filter_by(id=id).first()
    if analysis:
      db.session.delete(analysis)
      db.session.commit()
    else:
      raise Exception("Analysis not found")
  except Exception as e:
    handle_exception(e)
  return redirect(url_for("dashboard"))

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
  sort_by = request.args.get("sort_by") if request.args.get("sort_by") else "created_at"
  data = Analysis.query.filter_by(user_id=current_user.id).order_by(getattr(Analysis, sort_by).desc()).all()  # .limit()

  # Convert analysis objects to dictionaries with datetime converted to string
  evaluations = []
  for analysis in data:
    dict = analysis.__dict__
    corrected_hour = ((dict["created_at"].hour - 8) % 24)
    corrected_tz = dict["created_at"].replace(tzinfo=None, hour=(corrected_hour))
    dict["created_at"] = corrected_tz.strftime('%x %X %p')
    evaluations.append(dict)

  return render_template("dashboard.html", evaluations=evaluations)

@app.route("/evaluate", methods=["GET", "POST"])
@login_required
def evaluate():
  if request.method == "POST":
    try:
      files = request.files.getlist("files")
      filenames = []
      results = []

      for file in files:
        if not file:
          raise Exception("No file(s) uploaded")

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
              "content": PROMPT
            },
            {
              "role": "user",
              "content": data
            }
          ])

        # Note: There is a maximum response length per file of 4096 tokens.
        # In one test, this resulted in 12857 characters, 1309 words, 609 lines
        # so the response will be truncated if it exceeds this length
        # This results in errors because the JSON may be truncated in the middle, causing a syntax error
        # To prevent this, we should make sure that the response is always properly formatted
        # We could implement a maximum number of suggestions per file to avoid going over the limit.
        # We could also handle the exception so that if we ever run into the issue, we can truncate the message content to the last suggestion.
        # This would be the equivalent of rewinding back until we find the last closing bracket, removing everything after that, and adding a square bracket to close the list

        try:
          data = json.loads(response.choices[0].message.content)
        except json.JSONDecodeError as e:
          print("---------------Decode Error---------------")
          print(response.choices[0].message.content)
          print("------------------------------------------")
          data = handleJSONDecodeError(response.choices[0].message.content, e)
          data = json.loads(data)

        # save to results to display on template
        results.append(data)

        # save to database
        analysis = Analysis(user_id=current_user.id,
                  filename=filename, data=data,
                  created_at=db.func.now(),
                  updated_at=db.func.now()
                  )
        db.session.add(analysis)
        db.session.commit()
      return render_template("evaluate.html", filenames=filenames, results=results)
    except Exception as e:
      handle_exception(e)
      return redirect(url_for("evaluate"))
  else:
    return render_template("evaluate.html")

if __name__ == "__main__":
  app.run(debug=True, port=5001)