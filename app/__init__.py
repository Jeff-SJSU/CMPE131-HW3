from flask import Flask

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="secret key !!!")

myobj = app

from app import routes