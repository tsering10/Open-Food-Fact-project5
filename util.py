import pandas as pd
from sqlalchemy.orm import sessionmaker
from connect_mysql import connect
import numpy as np



# create a configured "Session" 
Session = sessionmaker(bind=connect())

def Get_unique_df_values(df, col_name):
    """
    Get unique values from a dataframe
    """
    # Get unique value of a column
    unique_value_list = df[col_name].unique().tolist()
    return unique_value_list

def read_csv(file_name):
    df = pd.read_csv(file_name)
    df = df.replace({"-": None})
    df = df.replace({np.nan: None})
    
    # Here we map the nutrition grade into integers
    grade = {'a': 1,'b': 2,"c":3,'d':4,'e':5,None:6} 
    df['nutrition_grade_fr'] = [grade[item] for item in df['nutrition_grade_fr']] 

    return df 