from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey, DateTime,CHAR, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *


Base = declarative_base()

class Category(Base):
    __tablename__ = 'categorys'
    id = Column(Integer,primary_key=True,nullable=False)
    category_name = Column(String(50))
    # create a one-to-many relation with products table 
    products = relationship("Product")

    def __init__(self,category_name):
        self.category_name = category_name
        

class Product(Base):
    __tablename__='products'
    id = Column(Integer,primary_key=True,nullable=False)
    bar_code = Column(String(1500))
    product_name = Column(String(1500))
    language = Column(String(20))
    nutrition_grade = Column(CHAR(1))
    energy = Column(Float)
    fat = Column(Float)
    carbohydrates = Column(Float)
    sugars = Column(Float)
    fiber = Column(Float)
    proteins = Column(Float)
    salt = Column(Float)
    last_modified = Column(DateTime) 

    # category_id as a FK in products table 
    category_id = Column(Integer, ForeignKey('categorys.id'))

    def __init__(self,bar_code,product_name,language,nutrition_grade,energy,fat,carbohydrates,sugars,proteins,salt,last_modified):
        self.bar_code = bar_code
        self.product_name = product_name
        self.language = language
        self.nutrition_grade = nutrition_grade
        self.energy = energy
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.sugars = sugars
        self.proteins = proteins
        self.salt = salt
        self.last_modified = last_modified

# Created a product_store_association table that connects rows of products and rows of stores
product_store_association = Table(
    'ProductStore', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('store_id', Integer, ForeignKey('stores.id'))
)


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    store_name = Column(String(200))
     # added the products  property to Store and configured the product_store_association as the intermediary table.
    products = relationship("Product", secondary= product_store_association )

    def __init__(self, store_name):
        self.store_name = store_name


















