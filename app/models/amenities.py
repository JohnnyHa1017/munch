from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Amenity(db.Model):
    __tablename__ = 'amenities'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey(add_prefix_for_prod('businesses.id')), nullable=False)
    reservation = Column(Boolean, default=False)
    delivery = Column(Boolean, default=False)
    pickup = Column(Boolean, default=False)
    vegetarian = Column(Boolean, default=False)
    accepts_credit_card = Column(Boolean, default=False)
    free_wi_fi = Column(Boolean, default=False)
    street_parking = Column(Boolean, default=False)
    good_for_groups = Column(Boolean, default=False)
    outdoor_seating = Column(Boolean, default=False)

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
