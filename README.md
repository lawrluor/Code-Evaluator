# Lightweight Automated Code Analysis Engine

#### Client: Educational Institution (Private)

#### Stack: React, Python (Flask), OpenAI API, Docker, PostgreSQL

This tool was built as a lightweight, scrappy alternative to enterprise solutions like CodeGrade. The platform was commissioned by a professor/department to research  solutions to automate code review. Developed between January and February 2024, the system was a "cutting-edge" implementation of LLM-based analysis, providing professors with an admin-focused dashboard to organize, execute, and analyze student submissions grouped by classroom and assignment.

## Features

- Full-Stack Flask Architecture: Uses Flask for the backend and HTML with Jinja2 templates for the frontend. The system handles the entire lifecycle of an evaluation, from initial file upload to the final display of AI-generated reports.

- Relational Database Persistence: Implements Flask-SQLAlchemy to manage the data layer. Models store metadata for each evaluation, ensuring that a professor can revisit and re-analyze past student submissions.

- Secure File Handling: Utilizes Werkzeug to manage file uploads securely, ensuring that student submissions are properly saved to the server’s filesystem and associated with the correct database records.

- Administrative Dashboard: A centralized "Evaluations" view allows the user to browse through a history of all analyzed work, providing a high-level overview of student performance and submission status.

- Lightweight Local-First Design: Engineered as a "plug-and-play" tool with minimal dependencies. The tool was designed to be highly portable and accessible for local use-cases, though it could be used in a cloud environment with some modifications.

# USAGE:
1. run `python3 db_init.py` to generate the SQL database
2. `python3 app.py` or `gunicorn -b 0.0.0.0:8000 app:app` to run the app

3. Deploying to Render
Ensure that `DATABASE_URL`, `FLASK_SECRET_KEY`, `OPENAI_API_KEY`, and `PYTHON_VERSION` (3.11.7) are set properly. See https://docs.render.com/python-version

4. Set DATABASE_URL of the Render flask web service to the internal URL of the Render sql server. In the url, it should be postgresql, not postgres. Note: If the internal URL is causing errors like hostname (https://community.render.com/t/django-could-not-translate-host-name-to-address/6187/2), simply use the external connection URL. This is because the internal URL does not work across different accounts or teams on Render, only the same account/team.

More details: https://www.youtube.com/watch?v=IBfj_0Zf2Mo for guide on connecting SQL server on Render
