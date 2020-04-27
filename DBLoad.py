import pandas as pd



class CleanCSV():
    def __init__(self, file_name):
        self.file_name = file_name 

    def read_csv(self):
        df = pd.read_csv(self.file_name)
        print(df.shape)
        return df 

    def unique_category(self,df):
        unique_category_list = df['main_category'].unique().tolist()
        print(unique_category_list)
        return unique_category_list 
    
    def unique_store(self,df):
        unique_store_list = df['stores'].unique().tolist()
        print(unique_store_list)

    def unique_brand(self,df):
        unique_brand_list = df['brand'].unique().tolist()
        print(unique_brand_list)







class DBFeed():
    pass
    

    




if __name__ == "__main__":
    file_name = '/home/tashitsering/Openfood project/open_food_data/open_food_data.csv'
    dbfill = CleanCSV(file_name)
    df = dbfill.read_csv()
    dbfill.unique_brand(df)




    






