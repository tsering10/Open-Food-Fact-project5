import pandas as pd

class DBFeed():
    def __init__(self, file_name):
        self.file_name = file_name

    def read_csv(self):
        df = pd.read_csv(self.file_name)
        return df 

    




if __name__ == "__main__":
    file_name = '/home/tashitsering/Openfood project/open_food_data/open_food_data.csv'
    dbfill = DBFeed(file_name)
    dbfill.read_csv()




    






