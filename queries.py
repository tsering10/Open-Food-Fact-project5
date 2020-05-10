from models.model import Category, Product, Store, Brand


#print(session.query(Product).all())

def display_categories(session):
    Categorys = session.query(Category).all()
    cat_names = [category.category_name for category in Categorys]
    cat_id = [category.id for category in Categorys]

    dictionary = dict(zip(cat_id, cat_names))

    return dictionary 
        


