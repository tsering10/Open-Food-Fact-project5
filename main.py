from models.model import *
from sqlalchemy.ext.declarative import declarative_base
from queries import display_categories,display_products,Get_product_store,display_better,insert_favorite,display_favorite
from DBLoad import sess
from flask import Flask, render_template, request, flash,session
from flask import redirect

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/") 
def home():
    return render_template('index.html')

@app.route("/category",methods=['GET', 'POST']) 
def categorys():
    dico = display_categories(sess)
    
    return render_template('category.html',dico=dico)


@app.route("/product_category", methods=['GET', 'POST'])

def products():
    # Get the selected category id
    cp = request.args.get('cat_id')
    session['catID'] = cp
    if 'catID' in session:
        catID = session['catID']
        all_product = display_products(sess,catID)
        return render_template("products.html", all_product = all_product)

@app.route("/recommendation", methods=['GET', 'POST'])

def recommendation():
    if not session.get("catID") is None:
        cID = session.get("catID")
        product_id = request.args.get("productID")
        select_store = Get_product_store(sess,product_id)
        better_product = display_better(sess,product_id,cID)
        if better_product is None or len(better_product) == 0:
            return render_template("nobetterproduct.html",select_store=select_store)
        else:
            return render_template("recommendation.html",select_store=select_store, better_product = better_product)


@app.route("/favorite",methods=['GET', 'POST']) 
def favorite():

    if not session.get("catID") is None:
        cID = session.get("catID")
        barcode = request.args.get("barcode")
        better_product = display_better(sess, barcode,cID)
        # calling function insert_favorite to save the recommended product in database
        insert_favorite(sess,better_product)
        
    fav_products = display_favorite(sess)

    return render_template("favorite.html",fav_products=fav_products)
 
   
        








        
if __name__ == "__main__":
    app.run(debug=True)
    # db_engine = connect()
    # file_name = '/home/tashitsering/Openfood project/open_food_data/open_food_data1.csv'
    # dbfill = DBFeed(file_name)
    # dbfill.populate_category()
    # dbfill.populate_store()
    # dbfill.populate_brand()
    # dbfill.populate_product()

