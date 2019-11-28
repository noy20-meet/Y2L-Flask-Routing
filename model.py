from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Product(Base):
   __tablename__ = 'Products'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Float)
   Picture_Link  = Column(String)
   Description  = Column(String)

class Cart(Base):
   __tablename__ = 'Cart'
   id = Column(Integer, primary_key=True)
   productID = Column(Integer)


class User(Base):
   __tablename__ = 'user'
   id = Column(Integer, primary_key=True)
   user_name = Column(String)
   password = Column(Integer)