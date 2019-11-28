from model import Product,Base,Cart

from sqlalchemy.pool import SingletonThreadPool

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///lecture.db',poolclass=SingletonThreadPool)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product(name, price, Picture_Link,Description):

    product = Product(
        name=name,
        price=price,
        Picture_Link=Picture_Link,
        Description=Description)
    session.add(product)
    session.commit()

def update_product(id, price):
   
   product_object = session.query(
       Product).filter_by(
       id=id).first()
   product_object.price = price
   session.commit()

def delete_student(their_id):

   session.query(Product).filter_by(
       id=their_id).delete()
   session.commit()

def query_all():

   products = session.query(
      Product).all()
   return products

def query_by_id(their_id):

   product = session.query(
       Product).filter_by(
       id=their_id).first()
   return product

def add_To_Cart(productID):

    carts = Cart(
        productID=productID)
    session.add(carts)
    session.commit()




