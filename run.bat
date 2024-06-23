@echo off
REM Activate the virtual environment
CALL venv\Scripts\activate

REM Run the Django development server
python manage.py runserver

