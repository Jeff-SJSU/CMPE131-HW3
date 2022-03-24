from wsgiref.validate import validator
from flask import render_template, flash
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

name = 'Jeff'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']


class CityForm(FlaskForm):
    city = StringField('City Name', validators=[DataRequired()])
    submit  = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = CityForm()
    if form.validate_on_submit():
        flash(form.city.data)


    return render_template("home.html", name=name, city_names=city_names, form=form)