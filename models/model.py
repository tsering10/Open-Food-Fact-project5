from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey


Base = declarative_base()

class Products(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'product'