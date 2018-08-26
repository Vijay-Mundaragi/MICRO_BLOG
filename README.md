mkdir Micro_Blog
cd Micro_Blog
pip install virtualenv
virtualenv -p=C:\Users\vmundaragi\AppData\Local\Programs\Python\Python36\python.exe venv
venv\Scripts\activate #activations belong to the terminal session in which you initiated them. for every new terminal you opem you need to activate again	
pip install flask
set FLASK_APP=micro_blog.py
pip install flask-sqlalchemy
pip install flask-migrate 	#for database migration (flask-migrate is Alembic framework(tool for transition of schemas from one version to another) extension)
flask db init #initialize a migration repository
flask db migrate -m "message"
flask db upgrade

Templates help you to seperate the application logic and Presentation logic.
By default flask is going to look for templates in a directory named templates.


For handling web-forms, use flask WTF package.
pip install flask-wtf

The flask application instance needs to be configured with a secret key the secret key is used in Flask.
Helps to avoid CSRF.

Separation of concerns - Keep the configs external to the app


C:\Users\vmundaragi\AppData\Local\Programs\Python\Python36\python.exe

When using flask WTF to work with web forms.
Each form is represented by a python class.

sqlalchemy supports many rdms including
	sqllite, mysql, postgresql