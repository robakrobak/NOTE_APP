
## NOTE APP - the web application

#### Introduction - the project's aim

The aim of this application is creating a tool useful for managing and delegating your tasks at work or other projects.
User can simply create notes and assign other users to it. Also, the user can see the archive of the notes whether they
met the deadline or not.

#### Technologies

* *Python 3.7 -  (https://www.python.org)*
* *Django 2.2 - (https://www.djangoproject.com)*
* *Django Crispy Forms (https://django-crispy-forms.readthedocs.io/en/latest/install.html)*
* *SQLite - (https://www.sqlite.org)*
* *Bootstrap 4 - (https://getbootstrap.com/)*
* *HTML*

#### Launch

Via Internet browser.

#### Start

The application was made using the PyCharm program. 
PyCharm is a great work environment. We can use commands embedded in this application and commands provided through the terminal. 
Here, I will use terminal commands because they are universal and can be used in another integrated development environment.

1.You should clone the repository with GitHub:
(https://github.com/robakrobak/NOTE_APP.git) -> Clone or download

2.Open a terminal
The method you use to open a terminal depends on your operating system.

Windows
Open the Windows Command Prompt (show path via Start menu and keyboard shortcuts)

Mac OS / Linux
Open the Terminal program. This is usually found under Utilities or Accessories.

Setup the pip package manager
Check to see if your Python installation has pip. Enter the following in your terminal:
``
pip -h
``

If you see the help text for pip then you have pip installed, otherwise download and install pip

3.Install the virtualenv package
The virtualenv package is required to create virtual environments.
You can install it with pip:
``
pip install virtualenv
``

4.Create the virtual environment
To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’, type the following:
``
virtualenv venv
``

5.Activate the virtual environment
You can activate the python environment by running the following command:

``
source venv/bin/activate
``

6.Module installation

``
pip install -r requirements.txt
``

7.Changes in models

``
python manage.py makemigrations
``
``
python manage.py migrate
``
8.Creating users

``
python manage.py createsuperuser
``

9.Starting server

``
python manage.py runserver
``


##### We invite you to test.

    Product: Junior Python Developer Team Poznan