from models.model import *
from sqlalchemy.orm import sessionmaker
from connect_mysql import connect
from sqlalchemy import and_
from sqlalchemy import distinct, desc
from  sqlalchemy.sql.expression import func, select


# # 3 - create a new session
# Session = sessionmaker(bind=connect())
# session = Session()


def display_categories(session):
    """
    Query to display all the categories in the database 
    """
    Categorys = session.query(Category).all()
    cat_names = [category.category_name for category in Categorys]
    cat_id = [category.id for category in Categorys]

    all_category = [{'id':cat_id,'name': cat_names } for cat_id, cat_names in zip(cat_id, cat_names)]

   
    return all_category

def display_products(session,cp):
    """
    Query to display all the products based on the category selected by a user
    """
    result = session.query(Product.product_name,Product.bar_code, Product.url,Product.nutrition_grade,Product.energy,Product.proteins).distinct(Product.product_name,Product.bar_code,Product.url,Product.nutrition_grade,Product.energy,Product.proteins).filter(
        products_categorys_association.c.product_id == Product.id).filter(products_categorys_association.c.category_id == Category.id).filter(Category.id == cp).order_by(Product.id.asc())
    
    p_name = [p.product_name for p in result ]
    p_code = [p.bar_code for p in result ]
    p_url = [p.url for p in result ]
    p_nutrition_grade = [p.nutrition_grade for p in result ]
    p_energy = [p.energy for p in result ]
    p_protein = [p.proteins for p in result ]

    # Create a dictionary of the queried products attributes
    all_product = [{'name': p_name, 'code': p_code, 'url': p_url,'nutrition grade': p_nutrition_grade,'energy':p_energy,'protein':p_protein} for p_name,p_code,p_url,p_nutrition_grade,p_energy,p_protein in zip(p_name,p_code,p_url,p_nutrition_grade,p_energy,p_protein)]
    
    return all_product


def Get_product_store(session,product_id):

    """
    Query to select products and stores from many to many table
    """

    product_store_result = session.query(Product.product_name,Product.bar_code,Product.url,Product.nutrition_grade,Product.energy,Product.proteins,Store.store_name).filter(products_stores_association.c.product_id == Product.id).filter(products_stores_association.c.store_id == Store.id).filter(Product.bar_code == product_id)

    return product_store_result

def display_better(session,product_id,cp):
    """
    Query to display better product than the one selected by a user from the database
    """
    current_product = Get_product_store(session,product_id)
    for grade in current_product:
        current_grade = grade.nutrition_grade
        if grade.nutrition_grade == 1:
            return current_product.order_by(func.rand()).limit(1).all()
          
        else:
            recomment_product = session.query(Product.product_name,Product.bar_code,Product.url,Product.nutrition_grade,Product.energy,Product.proteins,Store.store_name).filter(
                products_categorys_association.c.product_id == Product.id).filter(products_categorys_association.c.category_id == Category.id).filter(
                products_stores_association.c.product_id == Product.id).filter(products_stores_association.c.store_id == Store.id).filter(Category.id == cp).filter(Product.nutrition_grade < current_grade)
            return recomment_product.order_by(func.rand()).limit(1).all()

def insert_favorite(session,better_product):
    """
    Query to insert the recommended product into the database
    """
    unique_list =[]
    barcodes = session.query(Favorite).all()
    for code in barcodes:
        unique_list.append(code.bar_code)
    for bp in better_product:
        if bp.bar_code not in unique_list:
            fav = Favorite(bp.product_name,bp.bar_code,bp.url,bp.nutrition_grade,bp.energy,bp.proteins,bp.store_name)
            session.add(fav)
    session.commit()


def display_favorite(session):
    """
    Query to display favorite products in the database 
    """
    favs = session.query(Favorite).all()
    return favs
 


 
 
 
 
  



# select_stores(session)
# select_brands(session)
# get_product(session,1)
# select_stores(session,'Steak Haché 5%')
# display_better(session,'3245411954277',cp=1) #0
# display_better(session,'3181232120043',cp=1) # 1

# display_better(session,'Steak Haché Pur Bœuf 15%')

# insert_favorite(session)



