from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.routes.aws_helpers import ALLOWED_EXTENSIONS
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
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField("Create Post")
