from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField
from wtforms.validators import DataRequired
from app.models import Menu


class NewMenu(FlaskForm):
    name = StringField('Menu Item', validators=[DataRequired()])
    menu_category = [('Drink', 'Drink'), ('Appetizer, Appetizer'), ('Entree, Entree'), ('Dessert, Dessert'), ('Special, Special')]
    category = SelectField('Type', choices = menu_category, validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    description = StringField('Description')
