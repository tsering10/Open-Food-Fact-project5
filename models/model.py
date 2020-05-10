from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey, DateTime,CHAR, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from connect_mysql import connect


Base = declarative_base()


products_categorys_association = Table(
    'products_categorys', Base.metadata,
    Column('category_id', Integer, ForeignKey('categorys.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    PrimaryKeyConstraint('category_id', 'product_id'),
)


# # Created a product_stores_association table that connects rows of products and rows of stores
products_stores_association = Table(
    'products_stores', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('store_id', Integer, ForeignKey('stores.id')),
    PrimaryKeyConstraint('product_id', 'store_id'),
)



products_brands_association = Table(
    'products_brands', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id'),primary_key=True),
    Column('brand_id', Integer, ForeignKey('brands.id'),primary_key=True),
    PrimaryKeyConstraint('product_id', 'brand_id'),
)



class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(500))
    

    def __init__(self, category_name):
        self.category_name =  category_name

        
class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    store_name = Column(String(200))
     
    def __init__(self, store_name):
        self.store_name = store_name
        
class Brand(Base):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True)
    brand_name = Column(String(200))
    
    def __init__(self, brand_name):
        self.brand_name = brand_name




class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True,nullable=False)
    product_name = Column(String(500))
    bar_code = Column(String(1500))
    url = Column(String(2500))
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


    categorys = relationship("Category", secondary = products_categorys_association)
    stores = relationship("Store", secondary = products_stores_association)
    brands = relationship("Brand", secondary = products_brands_association)
    
    def __init__(self, product_name, bar_code,url, language, nutrition_grade,energy,fat,carbohydrates,sugars,fiber,proteins,salt,last_modified):
        self.product_name = product_name
        self.bar_code = bar_code
        self.url = url
        self.language = language
        self.nutrition_grade  =  nutrition_grade 
        self.energy = energy 
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.sugars = sugars
        self.fiber = fiber
        self.proteins = proteins
        self.salt = salt
        self.last_modified = last_modified 
        
        

Base.metadata.create_all(connect())



