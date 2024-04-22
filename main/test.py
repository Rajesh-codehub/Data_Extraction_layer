import boto3
import pandas as pd
import json
from botocore.exceptions import ClientError

def read_from_s3_cloud(json_path):
    """
    Read a CSV file from Amazon S3 using credentials provided in a JSON file.

    Parameters:
    - json_path (str): Path to the JSON file containing AWS credentials and S3 information.

    Returns:
    - DataFrame: Pandas DataFrame containing the data read from the CSV file.

    Raises:
    - FileNotFoundError: If the JSON file specified by json_path does not exist.
    - KeyError: If any required key is missing in the JSON data.
    - botocore.exceptions.ClientError: If there is an error accessing the S3 object.
    """

    # Read AWS credentials and S3 information from the JSON file
    with open(json_path, "r") as jsondata:
        creds = json.load(jsondata)

    # Extract necessary information
    service_name = creds.get('service_name')
    region_name = creds.get('region_name')
    aws_access_key_id = creds.get('access_key')
    aws_secret_access_key = creds.get('secret_key')
    bucket_name = creds.get('bucket_name')
    file_path = creds.get('file_path')
    file_format = creds.get('file_format')

    # Validate required keys are present
    required_keys = ['service_name', 'region_name', 'access_key', 'secret_key', 'bucket_name', 'file_path', 'file_format']
    missing_keys = [key for key in required_keys if key not in creds]
    if missing_keys:
        raise KeyError(f"Missing required keys in JSON data: {', '.join(missing_keys)}")

    # Create an S3 resource
    s3 = boto3.resource(
        service_name=service_name,
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Read the CSV file into a pandas DataFrame
    object_key = f"{file_path}.{file_format}"

    try:
        # Get the S3 object
        obj = s3.Object(bucket_name, object_key)
        
        # Read the object's content into a DataFrame
        with obj.get()['Body'] as f:
            df = pd.read_csv(f)
            print("Processing done")
    except ClientError as e:
        error_message = f"Error accessing S3 object: {e.response['Error']['Message']}"
        raise ClientError(error_message) from e

    return df

# Example usage:
# df = read_from_s3_cloud("credentials.json")


json_path = "C:/Users/rajes/portfolio/projects/Data_Extraction/Credentials/s3_creds.json"

# with open(json_path, "r") as jsondata:
#     creds = json.load(jsondata)
# service_name = creds['service_name']
# region_name = creds['region_name']
# aws_access_key_id = creds['access_key']
# aws_secret_access_key = creds['secret_key']
# bucket_name = creds['bucket_name']
# file_path = creds['file_path']
# file_format = creds['file_format']



# # Create an S3 resource
# s3 = boto3.resource(service_name = service_name,region_name = region_name,aws_access_key_id = aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# # List all buckets
# for bucket in s3.buckets.all():
#     print(bucket.name)

# # Read the CSV file into a pandas DataFrame
# bucket_name = bucket_name
# object_key = f"{file_path}.{file_format}"

# # Create an S3 object
# obj = s3.Object(bucket_name, object_key)

# # Read the object's content into a DataFrame
# with obj.get()['Body'] as f:
#     df = pd.read_csv(f)

# # Print the DataFrame type and head
# print(type(df))
# print(df.head())

# df.to_csv('C:/Users/rajes/portfolio/projects/Data_Extraction/Data_files/vikings.csv',index=False)

# def read_from_s3_cloud(input_path):
#     with open(json_path, "r") as jsondata:
#         creds = json.load(jsondata)
#     service_name = creds['service_name']
#     region_name = creds['region_name']
#     aws_access_key_id = creds['access_key']
#     aws_secret_access_key = creds['secret_key']
#     bucket_name = creds['bucket_name']
#     file_path = creds['file_path']
#     file_format = creds['file_format']

#     # Create an S3 resource
#     s3 = boto3.resource(service_name = service_name,region_name = region_name,aws_access_key_id = aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

#     # Read the CSV file into a pandas DataFrame
#     bucket_name = bucket_name
#     object_key = f"{file_path}.{file_format}"

#     # Create an S3 object
#     obj = s3.Object(bucket_name, object_key)

#     # Read the object's content into a DataFrame
#     with obj.get()['Body'] as f:
#         df = pd.read_csv(f)
#         print("process Done")
#     return df

read_from_s3_cloud(json_path)
