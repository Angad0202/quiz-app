# Getting Started
clone the repository
```
git clone https://github.com/Angad0202/quiz-app.git
```
## Install dependencies:
```
pip install -r requirements.txt
```
## Configure the database
The application uses SQLite by default, which requires no additional setup. However, if you want to use a different database, update the DATABASES setting in quiz_project/settings.py
```
python manage.py makemigrations
python manage.py migrate
```
## Create a superuser(Optional):
If you want to access the Django admin interface to add questions, create a superuser account:
```
python manage.py createsuperuser
```
## Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:8000/
```
## Access the Admin Interface:
If you created a superuser, you can access the admin interface at:
```
http://127.0.0.1:8000/admin/
```
## Taking the Quiz
From the dashboard, click on the "Take Quiz" button to start answering questions. The occurances of the Questions in the quiz are randomized.
