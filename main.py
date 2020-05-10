from models.model import Category,Product
from sqlalchemy.ext.declarative import declarative_base
from queries import display_categories
from DBLoad import session

from flask import Flask, render_template, request, flash
app = Flask(__name__)



@app.route("/",methods=['GET', 'POST']) 
def home():
    dico = display_categories(session)
    return render_template('index.html',dico=dico)


        
if __name__ == "__main__":
    app.run()
    #generate database schema

    # db_engine = connect()
    # file_name = '/home/tashitsering/Openfood project/open_food_data/open_food_data.csv'
    # dbfill = DBFeed(file_name)
    # dbfill.populate_category()
    # dbfill.populate_store()
    # dbfill.populate_brand()
    # dbfill.populate_product()

