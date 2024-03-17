from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length
from app.models import Business


class CreateBusiness(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    price_rating = IntegerField('Price Rating', validators=[DataRequired(), NumberRange(min=1, max=4, message='Price rating must be between 1 and 4')])
    category = StringField('Category', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=20)])
    description = StringField('Description')
