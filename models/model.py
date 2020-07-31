from sqlalchemy import Column, Integer, String, Float, PrimaryKeyConstraint, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from connect_mysql import connect

Base = declarative_base()

products_categorys_association = Table(
    'products_categorys', Base.metadata,
    Column('category_id', Integer, ForeignKey('categorys.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    PrimaryKeyConstraint('category_id', 'product_id'),
)

# Created a product_stores_association table that connects rows of products and rows of stores
products_stores_association = Table(
    'products_stores', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('store_id', Integer, ForeignKey('stores.id')),
    PrimaryKeyConstraint('product_id', 'store_id'),
)


class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(500))

    def __init__(self, category_name):
        self.category_name = category_name


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    store_name = Column(String(200))

    def __init__(self, store_name):
        self.store_name = store_name


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False)
    product_name = Column(String(500))
    bar_code = Column(String(1500))
    url = Column(String(2500))
    nutrition_grade = Column(Integer)
    energy = Column(Float)
    proteins = Column(Float)
    # Relationships
    categorys = relationship("Category", secondary=products_categorys_association)
    stores = relationship("Store", secondary=products_stores_association)

    def __init__(self, product_name, bar_code, url, nutrition_grade, energy, proteins):
        self.product_name = product_name
        self.bar_code = bar_code
        self.url = url
        self.nutrition_grade = nutrition_grade
        self.energy = energy
        self.proteins = proteins


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(500))
    bar_code = Column(String(1500))
    url = Column(String(2500))
    nutrition_grade = Column(Integer)
    energy = Column(Float)
    proteins = Column(Float)
    store_name = Column(String(200))

    def __init__(self, product_name, bar_code, url, nutrition_grade, energy, proteins, store_name):
        self.product_name = product_name
        self.bar_code = bar_code
        self.url = url
        self.nutrition_grade = nutrition_grade
        self.energy = energy
        self.proteins = proteins
        self.store_name = store_name


Base.metadata.create_all(connect())
