from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Amenity(db.Model):
    __tablename__ = 'amenities'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey(add_prefix_for_prod('businesses.id')), nullable=False)
    reservation = Column(Boolean)
    delivery = Column(Boolean)
    pickup = Column(Boolean)
    vegetarian = Column(Boolean)
    accepts_credit_card = Column(Boolean)
    free_wi_fi = Column(Boolean)
    street_parking = Column(Boolean)
    good_for_groups = Column(Boolean)
    outdoor_seating = Column(Boolean)

    businesses = relationship('Business', back_populates='amenities')

    def to_dict(self):
        return {
            'id': self.id,
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
