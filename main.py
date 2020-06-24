from models.model import *
from sqlalchemy.ext.declarative import declarative_base
from queries import display_categories,display_products,Get_product_store,display_better
from DBLoad import session
from flask import Flask, render_template, request, flash


app = Flask(__name__)



@app.route("/") 
def home():
    
    return render_template('index.html')

@app.route("/category",methods=['GET', 'POST']) 
def categorys():
    dico = display_categories(session)
    
    return render_template('category.html',dico=dico)


@app.route("/product_category", methods=['GET', 'POST'])

def products():
    #Get the selected category id
    global cp
    cp = request.args.get('cat_id')
    all_product = display_products(session,cp)
   

    return render_template("products.html", all_product = all_product)

@app.route("/recommendation", methods=['GET', 'POST'])

def recommendation():
    product_id = request.args.get("productID")
    select_store = Get_product_store(session,product_id)
    print("category id",cp)
    better_product = display_better(session,product_id,cp)

    return render_template("recommendation.html",select_store=select_store, better_product = better_product)

    # return render_template("recommendation.html",select_store=select_store, better_product =  better_product)


   
        









# @app.route("/recommendation", methods=['GET', 'POST'])

# def display_better_product()

        
if __name__ == "__main__":
    app.run(debug=True)
    #generate database schema

    # db_engine = connect()
    # file_name = '/home/tashitsering/Openfood project/open_food_data/open_food_data1.csv'
    # dbfill = DBFeed(file_name)
    # dbfill.populate_category()
    # dbfill.populate_store()
    # dbfill.populate_brand()
    # dbfill.populate_product()

