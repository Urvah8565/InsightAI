import pandas as pd
def profile_dataset(df):
    profile = {
        'rows':len(df),
        'columns':len(df.columns),
        'columns_info':{}
    }


    for column in df.columns:
        columns_info = {
            'dtype':str(df[column].dtype),
            'missing_values':int(df[column].isnull().sum())
        }


        if pd.api.types.is_numeric_dtype(df[column]):
            columns_info['statistics'] = {
                'mean':float(df[column].mean()),
                'min':float(df[column].min()),
                'max':float(df[column].max())
            }
        elif pd.api.types.is_string_dtype(df[column]) :
            columns_info['unique_values'] = int(df[column].nunique())

        profile['columns_info'][column] = columns_info

    return profile
       

