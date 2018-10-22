mkdir Micro_Blog
cd Micro_Blog
pip install virtualenv
virtualenv --python=C:\Users\vmundaragi\AppData\Local\Programs\Python\Python36\python.exe venv
venv\Scripts\activate #activations belong to the terminal session in which you initiated them. for every new terminal you open you need to activate again	
pip install flask
set FLASK_APP=micro_blog.py
pip install flask-sqlalchemy


set FLASK_DEBUG=1 #for debug mode

For DB migrations:
	pip install flask-migrate 	#for database migration (flask-migrate is Alembic framework(tool for transition of schemas from one version to another) extension)
	flask db init #initialize a migration repository
	flask db migrate -m "message"
	flask db upgrade


Templates help you to seperate the application logic and Presentation logic.
By default flask is going to look for templates in a directory named templates.
Separation of concerns - Keep the configs external to the app



pip install flask-wtf  #For handling web-forms, use flask WTF package.

The flask application instance needs to be configured with a secret key the secret key is used in Flask.
Helps to avoid CSRF.


C:\Users\vmundaragi\AppData\Local\Programs\Python\Python36\python.exe

When using flask WTF to work with web forms.
Each form is represented by a python class.

sqlalchemy supports many rdms including
	sqllite, mysql, postgresql

flask shell

pip install flask-login #for working with user sessions

The flask login extension can work with any user model class regardless of how you implemented it.
It needs three attributes and one method to be implemented to make it easy.
The extension provides a useful mixin class that you can add as a base class to your model giving you
an appropriate implementation for these four elements.



u = User(username="Vijay", email="abc@asd.com")
u.set_password("qwe")
db.session.add(u)
db.session.commit()



Naming Convention - All sub_templates are named starting from "_".