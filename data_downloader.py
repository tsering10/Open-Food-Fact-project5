#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import pandas as pd
import requests
from tqdm import tqdm
import math
import time
import os 
from functools import reduce
import numpy as np
from datetime import datetime



class Download_data():

    """ 
    This is a class for getting json data from openfoodfacts API. 
       
    """
    
    
    def download_json(self,CATEGORIES_LIST):
        """Return json of all the information for each category"""


        data = []

        for category in tqdm(CATEGORIES_LIST):
            # looping over each category and get its json 
            url_base = 'https://fr.openfoodfacts.org/categorie'
            url_end = 'json'
            url = "{}/{}.{}".format(url_base,category,url_end)
            # make  request to the url 
            response = requests.get(url)
            products = response.json()
            time.sleep(1)
            # get the count number of product 
            count = products["count"]
            # get the number of pages and get the required information 
            url_page = math.ceil(int(count)/20)
            print(url_page)
            # loop over each page 
            for x in range(1,url_page+1):
                url_new = f'{url_base}/{category}/{x}.{url_end}'
                r = requests.get(url_new)
                products = r.json()

                for i in range(len(products['products'])):
                    # create a empty dictionary to store data
                    res = {}
                    res['main_category'] = products['products'][i].get('pnns_groups_2')
                    res['code'] = products['products'][i].get('code')
                    res['url'] = products['products'][i].get('url')
                    res['product_name'] = products['products'][i].get('product_name')
                    res['nutrition_grade_fr'] = products['products'][i].get('nutrition_grade_fr')
                    res['stores'] = products['products'][i].get('stores')
                    res['energy'] = products['products'][i]['nutriments'].get('energy_100g')
                    res['proteins'] = products['products'][i]['nutriments'].get('proteins_100g')
                    # append the dictionary to a list 
                    data.append(res)
        
        
         # create a dataframe 
        df = pd.DataFrame(data)

        
        # Clean some data as the data are not normalized. 
        # In one of the columns i.e stores, a single cell had multiple comma seperated values.
        df = df.replace({np.nan: "-"})
        # We start with creating a new dataframe from the series with code as the index
        df_store = pd.DataFrame(df.stores.str.split(",").tolist(),index=df.code).stack()
        #We now want to get rid of the secondary index
        # To do this, we will make code as a column 
        df_store = df_store.reset_index([0, 'code'])
        # The final step is to set the column names as we want them
        df_store.columns = ['code', 'stores']
        # merge the separate row dataframe with the original dataframe
        df_new = df.merge(df_store, how='inner', left_on='code', right_on='code')
        # select the needed columns
        df_new = df_new[['main_category', 'code', 'url', 'product_name', 'nutrition_grade_fr','energy', 'proteins', 'stores_y']]

        return df_new
        
        
    
    def save_dataframe_csv(self,df):
        """ 
        The function to the dataframe as a csv file. 
  
        Parameters: 
            df (dataframe): the dataframe to be saved. 
           
        """
        
        # get the current directory
        cwd = os.getcwd()
        dir = os.path.join(cwd,"open_food_data")
        if os.path.exists(dir):
                print(dir + ' : exists and saving the file as open_food_data.csv')
                # saving the file as a csv file 
                df.to_csv(dir+'/open_food_data.csv',index=False,encoding='utf-8-sig')

        else:
            os.mkdir(dir)
            # saving the file as csv file 
            print('saving the data as open_food_data.csv')
            df.to_csv(dir+'/open_food_data.csv',index=False,encoding='utf-8_sig')



if __name__ == "__main__":
    t = Download_data()
    CATEGORIES_LIST = [
    'Bœuf',
    'Flocons',
    'Pizzas',
    'Jus de fruits pur jus',]
    
    d = t.download_json(CATEGORIES_LIST)
    t.save_dataframe_csv(d)
        

    
   

