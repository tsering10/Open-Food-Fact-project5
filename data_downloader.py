#!/usr/bin/env python3
# -*- coding: Utf-8 -*

import pandas as pd
import requests
from tqdm import tqdm
import math
import time
import os 
from constants import *


class Download_data():
    
    
    def download_json(self,CATEGORIES_LIST):
        """Return json of all the information for each category"""


        data = []

        for category in tqdm(CATEGORIES_LIST):
            # looping over each category and get its json 
            url_base = 'https://fr.openfoodfacts.org/categorie'
            url_end = 'json'
            url = "{}/{}.{}".format(url_base,category,url_end)
            # make a request to the url 
            response = requests.get(url)
            products = response.json()
            time.sleep(1)
            # get the count number of product 
            count = products["count"]
            # get the number of pages and get the required information 
            url_page = math.ceil(count/20)
            print(url_page)
            # loop over each page 
            for x in range(1,url_page+1):
                url_new = f'{url_base}/{category}/{x}.{url_end}'
                r = requests.get(url_new)
                products = r.json()

                for i in range(0,len(products['products'])):

                    res = {}
                    #res['main_category'] = category 
                    res['main_category'] = products['products'][i].get('pnns_groups_2')
                    res['code'] = products['products'][i].get('code')
                    res['url'] = products['products'][i].get('url')
                    res['product_name'] = products['products'][i].get('product_name')
                    res['brand'] = products['products'][i].get('brands')
                    res['language'] = products['products'][i].get('languages_tags')[0].split(':')[-1]
                    res['nutrition_grade_fr'] = products['products'][i].get('nutrition_grade_fr')
                    res['stores'] = products['products'][i].get('stores')
                    res['energy_100g'] = products['products'][i]['nutriments'].get('energy_100g')
                    res['fat_100g'] = products['products'][i]['nutriments'].get('fat_100g')
                    res['carbohydrates_100g'] = products['products'][i]['nutriments'].get('carbohydrates_100g')
                    res['sugars_100g'] = products['products'][i]['nutriments'].get('sugars_100g')
                    res['fiber_100g'] = products['products'][i]['nutriments'].get('fiber_100g')
                    res['proteins_100g'] = products['products'][i]['nutriments'].get('proteins_100g')
                    res['salt_100g'] = products['products'][i]['nutriments'].get('salt_100g')
                    res['last_modified_t'] = products['products'][i].get('last_modified_t')
                    # append the dictionary to a list 
                    data.append(res)
        return data
    
    
    def save_dataframe_csv(self,data):
        """save the dataframe as a csv file"""
        #create dataframe
        df = pd.DataFrame(data)

        # get the current directory
        cwd = os.getcwd()
        dir = os.path.join(cwd,"open_food_data")
        if os.path.exists(dir):
                print(dir + ' : exists and saving the file as open_food_data.csv')
                # saving the the final consulation file as csv file 
                df.to_csv(dir+'/open_food_data.csv',index=False)

        else:
            os.mkdir(dir)
            #print(os.getcwd)
            # saving the the final consulation file as csv file 
            print('saving the data as open_food_data.csv')
            df.to_csv(dir+'/open_food_data.csv',index=False)



if __name__ == "__main__":
    t = Download_data()
    d = t.download_json(CATEGORIES_LIST)
    t.save_dataframe_csv(d)
        

    
   

