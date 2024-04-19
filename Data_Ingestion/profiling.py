
import pandas as pd


def data_profiling(df: pd.DataFrame, file_name: str) -> pd.DataFrame:
    """
    Perform data profiling on the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to be profiled.
        file_name (str): The name of the file from which the DataFrame is sourced.

    Returns:
        pd.DataFrame: A DataFrame containing profiling information.
    """
    try:
        row_count_series = row_count(df)
        parameters_series = get_column_series(df, file_name)
        data_type_series = get_data_types(df)
        null_count_series = null_count(df)
        duplicate_count_series = duplicate_count(df)

        df_profile = pd.concat([parameters_series, row_count_series, data_type_series, null_count_series, duplicate_count_series], axis=1)
        df_profile.set_index(parameters_series.name, inplace=True)

        return df_profile
    except Exception as e:
        print(f"An error occurred during data profiling: {str(e)}")
        return pd.DataFrame()


    

def row_count(df):
    """
    Calculate the row count for each column in the DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.Series: A Series containing the row count for each column.
    """
    row_count_by_columns = []
    for column in df.columns:
        count = df[column].count()
        row_count_by_columns.append(count)
    series = pd.Series(row_count_by_columns, index=df.columns, name='row_count')
    return series


def get_column_series(dataframe, file_name):
    """
    Extracts column names from a DataFrame and returns a Series.

    Args:
        dataframe (pandas.DataFrame): Input DataFrame.
        file_name (str): Name of the file from which the DataFrame was created.

    Returns:
        pandas.Series: Series containing column names with index set to column names.
        
    Raises:
        TypeError: If `dataframe` is not a pandas DataFrame.
    """
    # Check if dataframe is a pandas DataFrame
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument 'dataframe' must be a pandas DataFrame.")
    
    # Extract column names
    column_names = dataframe.columns.tolist()
    
    # Create a series with index and name
    series_name = f"Columns_{len(column_names)}_from_{file_name}"
    column_series = pd.Series(column_names, index=column_names, name=series_name)
    
    return column_series



def get_data_types(df):
    """
    Get the data types of columns in a DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame.

    Returns:
        pandas.Series: Series containing the data types of columns.
    """
    column_data_types = df.dtypes
    return pd.Series(column_data_types, name='data_type')

# def data_type(df):
#     column_data_types = df.dtypes
#     series = pd.Series(column_data_types,name = 'data_type')
#     return series

def null_count(df):
    """
    Calculates the count of null values in each column of the DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.Series: A Series containing the count of null values for each column.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    null_count_ = df.isnull().sum()
    return null_count_.rename('null_count')



def duplicate_count(df):
    """
    Count duplicate rows in a DataFrame.

    Parameters:
    - df (pandas.DataFrame): Input DataFrame.

    Returns:
    - pandas.Series: A Series containing the count of duplicate rows for each column.

    Raises:
    - ValueError: If df is not a pandas DataFrame.
    """

    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input 'df' must be a pandas DataFrame.")

    # Count duplicate rows for each column
    duplicate_count_ = df.apply(lambda x: x.duplicated().sum())

    # Create a Series with the count of duplicate rows
    series = pd.Series(duplicate_count_, name="duplicate_count")

    return series

