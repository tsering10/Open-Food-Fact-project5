import pandas as pd
from models.model import Category, Product, Store
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
    # df = df[0:150]
    # print(df.head())
    df = df.replace({"-": None})
    df = df.replace({np.nan: None})
    # Here we map the nutrition grade into integers
    grade = {'a': 1,'b': 2,"c":3,'d':4,'e':5,None:6} 
    df['nutrition_grade_fr'] = [grade[item] for item in df['nutrition_grade_fr']] 

    #print(df.head())
    return df

class DBFeed():
    def __init__(self, file_name):
        self.file_name = file_name 

    def populate_category(self):
        df = read_csv(self.file_name)
        unique_category_list = Get_unique_df_values(df,'main_category')

        for c in unique_category_list:
            cat = Category(category_name = c)
            session.add(cat)
            session.commit()
    
    def populate_store(self):
        df = read_csv(self.file_name)

        unique_store_list = Get_unique_df_values(df,'stores_y')

        for store in unique_store_list:
            st = Store(store_name = store)
            session.add(st)
            session.commit()


    def populate_product(self):
        df = read_csv(self.file_name)

        for idx, row in df.iterrows():
            product_name = row['product_name']
            bar_code = row['code']
            url = row['url']
            nutrition_grade = row['nutrition_grade_fr']
            energy = row['energy']
            proteins = row['proteins']
           

            
            category_names = row['main_category']
            store_names = row['stores_y']

            new_product = Product(product_name = product_name, bar_code = bar_code, url = url, nutrition_grade = nutrition_grade, energy = energy, proteins = proteins)
            new_category = session.query(Category).filter(Category.category_name == category_names).first()
            new_store = session.query(Store).filter(Store.store_name == store_names).first()

            if new_store is None:
                new_store = Store(store_name = store_names)
                session.add(new_store)
            new_product.categorys.append(new_category)
            new_product.stores.append(new_store)
            session.add(new_product)
            session.commit()
            session.close()


            
# if __name__ == "__main__":
   
#     #generate database schema

#     db_engine = connect()
#     #file_name = '/home/tashitsering/Openfood project/open_food_data/open_food_data.csv'
#     file_name = "/Users/ttsering/Desktop/Openfood project/open_food_data/open_food_data1.csv"
#     print("loading start.............")
#     dbfill = DBFeed(file_name)
#     dbfill.populate_category()
#     dbfill.populate_store()
#     dbfill.populate_product()
#     print("loading done................")




    






