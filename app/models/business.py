from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Business(db.Model):
  __tablename__ = 'businesses'

  if environment == "production":
    __table_args__ = {'schema': SCHEMA}

  id = Column(db.Integer, primary_key=True)
  owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  title = Column(String(50), nullable=False)
  address = Column(String(50), nullable=False)
  city = Column(String(30), nullable=False)
  state = Column(String(20), nullable=False)
  country = Column(String(20), nullable=False)
  price_rating = Column(Integer, nullable=False)
  category = Column(String(255), nullable=False)
  lat = Column(Float)
  lng = Column(Float)
  phone_number = Column(String(20), nullable=False, unique=True)
  description = Column(String(2000))

  users = relationship('User', back_populates='businesses', cascade='all, delete')
  menus = relationship('Menu', back_populates='businesses', cascade='all, delete')
  amenities = relationship('Amenity', back_populates='businesses', cascade='all, delete')
  reviews = relationship('Review', back_populates='businesses', cascade='all, delete')
  business_images = relationship('BusinessImage', back_populates='businesses', cascade='all, delete')

  def to_dict(self):
    return {
      'owner_id': self.owner_id,
      'title': self.title,
      'address': self.address,
      'city': self.city,
      'state': self.state,
      'country': self.country,
      'price_rating': self.price_rating,
      'category': self.category,
      'lat': self.lat,
      'lng': self.lng,
      'phone_number': self.phone_number,
      'description': self.description
    }