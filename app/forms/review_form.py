from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from app.models import Review


class CreateReview(FlaskForm):
    review = StringField('Review', validators=[DataRequired()])
    star = IntegerField('Star', validators=[DataRequired(), NumberRange(min=0, max=5, message='Star rating must be between 1 and 5')])
