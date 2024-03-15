from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class Menu(db.Model):
  __tablename__ = 'menus'

  if environment == 'production':
    __table_args__ = {'schema': SCHEMA}

  id = Column(db.Integer, primary_key=True)
  business_id = Column(Integer, ForeignKey(add_prefix_for_prod('businesses.id')), nullable=False)
  name = Column(String(50), nullable=False)
  category = db.Column(db.Enum('Appetizer', 'Entree', 'Drink', 'Dessert', 'Special'), nullable=False)
  price = Column(Float(precision=2))
  description = Column(String(2000))

  businesses = relationship('Business', back_populates='menus')

  def to_dict(self):
    return {
      'business_id': self.business_id,
      'name': self.name,
      'category': self.category,
      'price': self.price,
      'description': self.description
    }
