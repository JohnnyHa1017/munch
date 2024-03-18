from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField
from wtforms.validators import DataRequired
from app.models import Amenity

class CreateAmenities(FlaskForm):
    is_reservation = BooleanField('Reservation')
    is_delivery = BooleanField('Delivery')
    is_pickup = BooleanField('Pickup')
    is_vegetarian = BooleanField('Vegetarian')
    is_is_accepts_credit_card = BooleanField('Credit Card')
    is_free_wi_fi = BooleanField('Free Wifi')
    is_street_parking = BooleanField('Street parking')
    is_good_for_groups = BooleanField('Good for Groups')
    is_outdoor_seating = BooleanField('Outdoor Seating')
