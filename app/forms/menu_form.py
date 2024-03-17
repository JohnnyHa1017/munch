from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField
from wtforms.validators import DataRequired
from app.models import Menu


class NewMenu(FlaskForm):
    menu_item = StringField('Menu Item', validators=[DataRequired()])
    menu_category = [('Drink', 'Drink'), ('Appetizer, Appetizer'), ('Entree, Entree'), ('Dessert, Dessert'), ('Special, Special')]
    type = SelectField('Type', choices = menu_category, validators=[DataRequired()])
    menu_price = DecimalField('Price', places=2, validators=[DataRequired()])
    menu_description = StringField('Description')
