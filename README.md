# AI-Powered Automated Code Analysis Engine

#### Client: Educational Institution (Private)

#### Stack: React, Python (Flask), OpenAI API, Docker, PostgreSQL

This tool was built as a lightweight, scrappy alternative to enterprise solutions like CodeGrade. The platform was designed to help a group of professors automate the labor-intensive process of code review. Developed between January and February 2024, the system was a "cutting-edge" implementation of LLM-based analysis, providing professors with an admin-focused dashboard to organize, execute, and analyze student submissions grouped by classroom and assignment.

# USAGE:
1. run `python3 db_init.py` to generate the SQL database
2. `python3 app.py` or `gunicorn -b 0.0.0.0:8000 app:app` to run the app

3. Deploying to Render
Ensure that `DATABASE_URL`, `FLASK_SECRET_KEY`, `OPENAI_API_KEY`, and `PYTHON_VERSION` (3.11.7) are set properly. See https://docs.render.com/python-version

4. Set DATABASE_URL of the Render flask web service to the internal URL of the Render sql server. In the url, it should be postgresql, not postgres. Note: If the internal URL is causing errors like hostname (https://community.render.com/t/django-could-not-translate-host-name-to-address/6187/2), simply use the external connection URL. This is because the internal URL does not work across different accounts or teams on Render, only the same account/team.

More details: https://www.youtube.com/watch?v=IBfj_0Zf2Mo for guide on connecting SQL server on Render
