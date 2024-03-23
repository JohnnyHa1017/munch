from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField
from wtforms.validators import DataRequired
from app.models import Amenity

class CreateAmenities(FlaskForm):
    reservation = BooleanField('Reservation')
    delivery = BooleanField('Delivery')
    pickup = BooleanField('Pickup')
    vegetarian = BooleanField('Vegetarian')
    accepts_credit_card = BooleanField('Credit Card')
    free_wi_fi = BooleanField('Free Wifi')
    street_parking = BooleanField('Street parking')
    good_for_groups = BooleanField('Good for Groups')
    outdoor_seating = BooleanField('Outdoor Seating')
