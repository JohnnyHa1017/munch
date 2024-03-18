from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey(add_prefix_for_prod('businesses.id')), nullable=False)
    user_id = Column(Integer, ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    review = Column(String(2000), nullable=False)
    star = Column(Integer, nullable=False)

    users = relationship('User', back_populates='reviews')
    businesses = relationship('Business', back_populates='reviews')
    review_images = relationship('ReviewImage', back_populates='reviews', cascade='all, delete-orphan')

    def to_dict(self):
        return {
        'user_id': self.user_id,
        'business_id': self.business_id,
        'review': self.review,
        'star': self.star
        }
