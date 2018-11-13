# My Search Site

The goal is to implement an efficient and accurate search engine sample website.

# Technology used

* Django - 2.1.3
* Python 3.6.6
* virtualenv
* Faker
* SQLite3 (it will be replaced by PostgreSQL later on)
* Bootstrap 4
* Xubuntu 18.04
* Apache2 Webserver

#
Once complete, feel free to use for your own needs.

# Setup

* Download the following if you don't already have:

pip - sudo apt-get install -y python-pip python3-pip
virtualenv - sudo pip install virtualenv

* Download the repository as zip file or choose a folder and type:

user@localmachine: git clone https://github.com/rccrocha/search_django

* Create a virtual environment (I like to use virtualenv):

user@localmachine: virtualenv venv -p python3

* Activate virtual environment:

user@localmachine: source venv/bin/activate

* Install Django requirements:

(venv) user@localmachine: pip install -r requirements.txt

* In the folder where manage.py file is in, type:

(venv) user@localmachine: python manage.py runserver

* The default address will be http://127.0.0.1:8000

* Once in the website, sign up to see the search page.
* As the database is yet to be populate, you won't be able to search much.
* If you would like to access the Django Admin page, you will have to type in the command line:

(venv) user@localmachine: python manage.py createsuperuser

