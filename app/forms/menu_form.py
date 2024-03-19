from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.routes.aws_helpers import ALLOWED_EXTENSIONS
from app.models import Menu


class NewMenu(FlaskForm):
    name = StringField('Menu Item', validators=[DataRequired()])
    menu_category = [('Drink', 'Drink'), ('Appetizer', 'Appetizer'), ('Entree', 'Entree'), ('Dessert', 'Dessert'), ('Special', 'Special')]
    category = SelectField('Type', choices=menu_category, validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField("Create Post")

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    submit = SubmitField("Create Post")
