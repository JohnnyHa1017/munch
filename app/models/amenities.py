from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Amenity(db.Model):
    __tablename__ = 'amenities'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(db.Integer, primary_key=True)
    business_id = Column(db.Integer, ForeignKey('businesses.id'), nullable=False)
    reservation = Column(db.Boolean, default=False)
    delivery = Column(db.Boolean, default=False)
    pickup = Column(db.Boolean, default=False)
    vegetarian = Column(db.Boolean, default=False)
    accepts_credit_card = Column(db.Boolean, default=False)
    free_wi_fi = Column(db.Boolean, default=False)
    street_parking = Column(db.Boolean, default=False)
    good_for_groups = Column(db.Boolean, default=False)
    outdoor_seating = Column(db.Boolean, default=False)

    businesses = relationship('Business', back_populates='amenities')

    def to_dict(self):
        return {
            'business_id': self.business_id,
            'reservation': self.reservation,
            'delivery': self.delivery,
            'pickup': self.pickup,
            'vegetarian' : self.vegetarian,
            'accepts_credit_card': self.accepts_credit_card,
            'free_wi_fi': self.free_wi_fi,
            'street_parking': self.street_parking,
            'good_for_groups':self.good_for_groups,
            'outdoor_seating': self.outdoor_seating
        }