from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Jeff'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']

    city_list = '\n'.join([f"<li>{city}</li>" for city in city_names])
    return f'''
        <!DOCTYPE html>
        <h1>Welcome {name}!</h1>
        <a href="https://www.google.com/">not google</a>
        <ul>{city_list}</ul>

    '''