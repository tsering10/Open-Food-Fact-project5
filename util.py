import pandas as pd
import numpy as np
from sqlalchemy.orm import sessionmaker
from connect_mysql import connect

# create a configured "Session" 
Session = sessionmaker(bind=connect())


def get_unique_df_values(dataframe, col_name):
    """
    Get unique values from a dataframe
    """
    # Get unique value of a column
    unique_value_list = dataframe[col_name].unique().tolist()

    return unique_value_list


def read_csv(file_name):
    """
    read csv file and map nutrition grade into integer
    """
    df_original = pd.read_csv(file_name)
    df_original = df_original.replace({"-": None})
    df_original = df_original.replace({np.nan: None})
    # Here we map the nutrition grade into integers
    grade = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, None: 6}
    df_original['nutrition_grade_fr'] = [grade[item] for item in df_original['nutrition_grade_fr']]

    return df_original
