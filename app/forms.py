# app/forms.py
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired


class PredictionForm(FlaskForm):
    MedInc = FloatField('Median Income (in tens of thousands)',
                        validators=[DataRequired()])
    HouseAge = FloatField('House Age (in years)', validators=[DataRequired()])
    AveRooms = FloatField('Average Number of Rooms',
                          validators=[DataRequired()])
    AveBedrms = FloatField('Average Number of Bedrooms',
                           validators=[DataRequired()])
    Population = FloatField('Population', validators=[DataRequired()])
    AveOccup = FloatField('Average Occupancy', validators=[DataRequired()])
    Latitude = FloatField('Latitude', validators=[DataRequired()])
    Longitude = FloatField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Predict')
