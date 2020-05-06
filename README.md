# Sample Flask code database model

This a minimal sample code utilize the following modules

flask
flask-sqlalchemy
flask-script

model.py stores the DB model and manage the DB with flask-script module, to initialize/update the database structure:

python model.py db init
python model.py db migrate
python model.py db upgrade


`model_query.py` demostrates how to query, insert, update, delete records with flask-sqlalchemy

`myconfig.py` demostrates how to switch between Development and Production settings

`python app.py run`
starts web application to load entries in the database

flask-bootstrap is not used due to maintenance outdated as the time written this code, bootstrap 4.1 links are hard-copied from getbootstrap.com
