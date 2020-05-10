import pandas as pd
from models.model import Category, Product, Store, Brand
from sqlalchemy.orm import sessionmaker
from connect_mysql import connect
import numpy as np

# 3 - create a new session
Session = sessionmaker(bind=connect())
session = Session()




def Get_unique_df_values(df, col_name):
    """
    Get unique values from a dataframe
    """
    data = df 
    unique_value_list = data[col_name].unique().tolist()
    return unique_value_list

def read_csv(file_name):
    df = pd.read_csv(file_name)
    df = df[0:100]
    df = df.replace({np.nan: None})

    #print(df.head())
    return df

class DBFeed():
    def __init__(self, file_name):
        self.file_name = file_name 

    def populate_category(self):
        df = read_csv(self.file_name)
        unique_category_list = Get_unique_df_values(df,'main_category')
        print(unique_category_list)

        for c in unique_category_list:
            cat = Category(category_name = c)
            session.add(cat)
            session.commit()
    
    def populate_store(self):
        df = read_csv(self.file_name)
        unique_store_list = Get_unique_df_values(df,'stores')

        for store in unique_store_list:
            st = Store(store_name = store)
            session.add(st)
            session.commit()

    def populate_brand(self):
        df = read_csv(self.file_name)
        unique_brand_list = Get_unique_df_values(df,'brand')

        for bd in unique_brand_list:
            bran = Brand(brand_name=bd)
            session.add(bran)
            session.commit()


    def populate_product(self):
        df = read_csv(self.file_name) 

        for idx, row in df.iterrows():
            product_name = row['product_name']
            bar_code = row['code']
            url = row['url']
            language = row['language']
            nutrition_grade = row['nutrition_grade_fr']
            energy = row['energy']
            fat = row['fat']
            carbohydrates = row['carbohydrates']
            sugars = row['sugars']
            fiber = row['fiber']
            proteins = row['proteins']
            salt = row['salt']
            last_modified = row['last_modified_t']

            
            category_names = row['main_category']
            brand_names =  row['brand']
            store_names = row['stores']

            new_product = Product(product_name = product_name, bar_code = bar_code,url = url, language = language,nutrition_grade = nutrition_grade, energy = energy,fat = fat,carbohydrates = carbohydrates,sugars  = sugars,fiber = fiber,proteins = proteins,salt = salt,last_modified = last_modified)

            new_category = session.query(Category).filter(Category.category_name ==category_names).first()
            new_store = session.query(Store).filter(Store.store_name == store_names).first()
            new_brand = session.query(Brand).filter(Brand.brand_name == brand_names).first()

            if new_category and new_store and new_brand is None:
                new_category = Category(category_name =category_names)
                new_store = Store(store_name = store_names)
                new_brand = Brand(brand_name = brand_names)
                session.add(new_category)
                session.add(new_store)
                session.add(new_brand)
            new_product.categorys.append(new_category)
            new_product.stores.append(new_store)
            new_product.brands.append(new_brand)
            session.add(new_product)
            session.commit()
            

            
            
            
            
            
            
            
            
         







    




# if __name__ == "__main__":
#     file_name = '/home/tashitsering/Openfood project/open_food_data/open_food_data.csv'
#     dbfill = DBFeed(file_name)
#     dbfill.populate_category()




    






