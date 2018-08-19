mkdir Micro_Blog
cd Micro_Blog
pip install virtualenv
virtualenv -p=C:\Users\vmundaragi\AppData\Local\Programs\Python\Python36\python.exe venv
venv\Scripts\activate #activations belong to the terminal session in which you initiated them. for every new terminal you opem you need to activate again	
pip install flask
set FLASK_APP = micro_blog.py


Templates help you to seperate the application logic and Presentation logic.
By default flask is going to look for templates in a directory named templates.