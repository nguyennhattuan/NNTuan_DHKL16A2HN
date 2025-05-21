import boto3 
from botocore.client import Config 
 
s3 = boto3.client('s3', 
    endpoint_url='http://localhost:9000',
    aws_access_key_id='tuan1234', 
    aws_secret_access_key='Tuan1234@', 
    config=Config(signature_version='s3v4'), 
    region_name='us-east-1') 
 
s3.download_file('iot-lab-demo', 'healthcare-dataset-stroke-data.csv', 'Data_NguyenNhaTuan_077.csv') 
print("Download thành công!") 