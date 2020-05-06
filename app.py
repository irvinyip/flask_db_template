from flask import Flask, render_template, url_for, session, request, redirect
from flask_sqlalchemy import SQLAlchemy
from model import postDB

app = Flask(__name__)
app.config.from_object('myconfig.DevelopmentConfig')
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    records = postDB.query.all()
    return render_template('index.html', records=records)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
