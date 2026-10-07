import pandas as pd 
from profiler import profile_dataset
def detect_column_types(df):
    column_types = {}


    for column in df.columns :
        if pd.api.types.is_numeric_dtype(df[column]):
            column_types[column] = 'numeric'

        elif pd.api.types.is_datetime64_any_dtype(df[column]):
            column_types[column] ='datetime'

        else :
            column_types[column] = 'categorical'

    return column_types

            
def convert_date_column(df) :
    df = df.copy()

    for column in df.columns:
        if df[column].dtype == 'object':
            converted  = pd.to_datetime(df[column],errors='coerce')

            if converted.notna().mean >= 0.8:
                df[column] = converted
    return df


def check_data_quality(df):
    quality = {
        'is_empty' :df.empty,
        'duplicate_rows':int(df.duplicated().sum()),
        'missing_values':int(df.isnull().sum().sum())

    }
    return quality


def analyze_dataset(df) :

    analyze = {
        'column_types':detect_column_types(df),
        'profile':profile_dataset(df),
        'quality':check_data_quality(df)
    }
    return analyze

  
    