import boto3
import logging
from botocore.exceptions import ClientError
import pandas
import io


def download_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        obj = s3_client.get_object(Bucket=bucket, Key=file_name)
        # # obj = s3_client.download_file(file_name, bucket, object_name)
        # initial_df = pandas.read_csv(obj['Body'])
        # print('response after downloading file from bucket', initial_df)
    except ClientError as e:
        logging.error(e)
        return False
    return obj


def search(name, row):
    nested_list = []
    for item in row:
        if isinstance(item, str):
            item = item.split(', ')
            nested_list.append(item)
    # Using list comprehension to convert a list of lists to a flat list
    flat_list = [item for elem in nested_list for item in elem]
    if name in flat_list:
        return True


def fetch_movie_details_with_key(name):
    csv_file = download_file('movies.csv', 'vemitta-datascrape')
    df = pandas.read_csv(io.BytesIO(csv_file['Body'].read()), encoding='utf8')
    # User list comprehension to create a list of lists from Dataframe rows
    list_of_rows = [list(row) for row in df.values]
    # Print list of lists i.e. rows
    for list_row in list_of_rows:
        if search(name, list_row):
            break
        else:
            continue


fetch_movie_details_with_key('Tim Robbins')
