from queries import display_categories, display_products, get_product_store, display_better, insert_favorite, \
    display_favorite
from DBLoad import sess
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/category", methods=['GET', 'POST'])
def category():
    category_dic = display_categories(sess)
    return render_template('category.html', dico=category_dic)


@app.route("/product_category", methods=['GET', 'POST'])
def products():
    # Get the selected category id
    cp = request.args.get('cat_id')
    session['catID'] = cp
    if 'catID' in session:
        cat_id = session['catID']
        all_product = display_products(sess, cat_id)
        return render_template("products.html", all_product=all_product)


@app.route("/recommendation", methods=['GET', 'POST'])
def recommendation():
    if not session.get("catID") is None:
        c_id = session.get("catID")
        product_id = request.args.get("productID")
        select_store = get_product_store(sess, product_id)
        better_product = display_better(sess, product_id, c_id)
        if better_product is None or len(better_product) == 0:
            return render_template("nobetterproduct.html", select_store=select_store)
        else:
            return render_template("recommendation.html", select_store=select_store, better_product=better_product)


@app.route("/favorite", methods=['GET', 'POST'])
def favorite():
    barcode = request.args.get("barcode")
    better_product = get_product_store(sess, barcode)
    # calling function insert_favorite to save the recommended product in database
    insert_favorite(sess, better_product)
    fav_products = display_favorite(sess)
    return render_template("favorite.html", fav_products=fav_products)


if __name__ == "__main__":
    app.run(debug=True)
