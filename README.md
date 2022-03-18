# LITReview
***
Website that allows a community of users to consult or request a book review on demand.

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Run the project](#run-the-project)
5. [Admin](#django-admin)

## General Info
***

## Technologies
***
* [Django](https://www.djangoproject.com/): Version 4.0.1
* [Python](https://example.com): Version 3.9.6
* [Bootsrap](https://getbootstrap.com/)

## Installation
***

A little intro about the installation.

Clone the project-repository, and go to the project-folder.
```
$ cd ./LITReview 
$ git clone https://github.com/MarineBdlt/LITRreview.git
$ cd ./litreview
```

Set up your environnement and install the requirements.
```
$ python -m venv env
```
To activate the environment, run source env/bin/activate (if you are on Windows, the command will be env/Scripts/activate.bat ). 
```
~/LITreview/$ source env/bin/activate
(env) ~/LITreview$
```

The following command will install the packages according to the configuration file requirements.txt.
```
$ pip install -r requirements.txt
```

## Run the project

Write  the following line in the console to run the web server.
```
$ python manage.py runserver 
```
You can find the app on django-host : http://127.0.0.1:8000/

## Django admin

 Go to your browser and type the address http://127.0.0.1:8000/admin/. You will see a login page like this:

Login page

To log in, you need to create a superuser - a user account that has control over everything on the site. Go back to the command line, type python manage.py createsuperuser, and press enter.
To write new commands while the web server is running, open a new terminal window and activate your virtualenv. 

```
{% filename %}Mac OS X or Linux:{% endfilename %}

(myvenv) ~/litreview$ python manage.py createsuperuser

{% filename %}Windows:{% endfilename %}

(myvenv) C:\Users\LITReview> python manage.py createsuperuser

When prompted, type your username (lowercase, no spaces), email address, and password. Don't worry that you can't see the password you're typing in – that's how it's supposed to be. Type it in and press enter to continue. The output should look like this (where the username and email should be your own ones):

Username: ola
Email address: ola@example.com
Password:
Password (again):
Superuser created successfully.
```

Return to your browser. Log in with the superuser's credentials you chose; you should see the Django admin dashboard.

Go to Tickets and experiment a little bit with it. You can add tickets. Don't worry about the content –- it's only visible to you on your local computer -- you can copy-paste some text from this tutorial to save time. :)

Django admin

If you want to know more about Django admin, you should check Django's documentation: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

