from flask import Flask

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="secret key !!!")

from app import routes