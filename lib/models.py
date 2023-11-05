#!/usr/bin/env python3

# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create the SQLite database and engine
engine = create_engine('sqlite:///inventory.db')
Base = declarative_base()

# Define the Product, Supplier, and Order tables
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer)
    quantity = Column(Integer, default=0)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship('Supplier', back_populates='products')

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)
    products = relationship('Product', back_populates='supplier')

class Order(Base):
    __tablename__ = 'orders'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    order_date = Column(Date, primary_key=True)
    quantity = Column(Integer)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()