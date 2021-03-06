from models.model import Category, Product, Store
from util import Session, get_unique_df_values, read_csv

# create a Session
sess = Session()


class DBFeed:
    """
    A class used to insert data into mysql database
    """

    def __init__(self, file_name):
        """
        Parameters
        ----------
        file_name : str
            The name of the csv file
       
        """
        self.file_name = file_name

    def populate_category(self):
        """ 
        Insert data into category table
        """
        df = read_csv(self.file_name)
        unique_category_list = get_unique_df_values(df, 'main_category')

        for c in unique_category_list:
            cat = Category(category_name=c)
            sess.add(cat)
            sess.commit()

    def populate_store(self):
        """
        Insert data into store table in the database
        """
        df = read_csv(self.file_name)
        unique_store_list = get_unique_df_values(df, 'stores_y')
        for store in unique_store_list:
            st = Store(store_name=store)
            sess.add(st)
            sess.commit()

    def populate_product(self):
        """
        Insert data into product table in the database
        """
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
            new_product = Product(product_name=product_name, bar_code=bar_code, url=url,
                                  nutrition_grade=nutrition_grade, energy=energy, proteins=proteins)
            new_category = sess.query(Category).filter(Category.category_name == category_names).first()
            new_store = sess.query(Store).filter(Store.store_name == store_names).first()
            if new_store is None:
                new_store = Store(store_name=store_names)
                sess.add(new_store)
            new_product.categorys.append(new_category)
            new_product.stores.append(new_store)
            sess.add(new_product)
            sess.commit()
            sess.close()
