from wtforms.validators import DataRequired
from wtforms import FloatField, SubmitField
from flask_wtf import FlaskForm
from flask import render_template, url_for, flash, redirect, Blueprint
from app.forms import PredictionForm
import joblib
import numpy as np

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    form = PredictionForm()
    if form.validate_on_submit():
        model = joblib.load('models/model.pkl')
        features = np.array([[
            form.MedInc.data, form.HouseAge.data, form.AveRooms.data,
            form.AveBedrms.data, form.Population.data, form.AveOccup.data,
            form.Latitude.data, form.Longitude.data
        ]])
        prediction = model.predict(features)[0]
        rounded_prediction = round(prediction, 3)
        return render_template('index.html', form=form, prediction=prediction, rounded_prediction=rounded_prediction)
    return render_template('index.html', form=form)


# app/forms.py


class PredictionForm(FlaskForm):
    MedInc = FloatField('Median Income', validators=[DataRequired()])
    HouseAge = FloatField('House Age', validators=[DataRequired()])
    AveRooms = FloatField('Average Rooms', validators=[DataRequired()])
    AveBedrms = FloatField('Average Bedrooms', validators=[DataRequired()])
    Population = FloatField('Population', validators=[DataRequired()])
    AveOccup = FloatField('Average Occupancy', validators=[DataRequired()])
    Latitude = FloatField('Latitude', validators=[DataRequired()])
    Longitude = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Predict')
