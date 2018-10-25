Installation:

Clone this repository

Create a new virtualenv: mkvirtualenv django_exo.
install django: pip install django==1.8.
install selenium: pip install selenium.

To run the application : 
  1.python manage.py migrate.
  2.python manage.py runserver.
command to run tests:
  1.Ajouter geckodriver.exe au dossoer Django_Exercice.
  2.python manage.py makemigrations.
  3.python manage.py test django_exercice.

Note:
  Les tests s'executent sur le navigateur Firefox.
