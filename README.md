# USAGE:
1. run `python3 db_init.py` to generate the SQL database
2. `python3 app.py` or `gunicorn -b 0.0.0.0:8000 app:app` to run the app

3. Deploying to Render
Ensure that `DATABASE_URL`, `FLASK_SECRET_KEY`, `OPENAI_API_KEY`, and `PYTHON_VERSION` (3.11.7) are set properly. See https://docs.render.com/python-version

4. Set DATABASE_URL of the Render flask web service to the interal URL of the Render sql server. In the url, it should be postgresql, not postgres.

More details: https://www.youtube.com/watch?v=IBfj_0Zf2Mo for guide on connecting SQL server on Render
