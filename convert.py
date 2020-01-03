import json
import tabula
import boto3
from urllib.parse import unquote

# Create an S3 client
s3 = boto3.resource('s3')

def handler(event, context):
    # Read pdf into DataFrame

    print(json.dumps(event))

    record = event['Records'][0]

    s3bucket = record['s3']['bucket']['name']
    s3object = record['s3']['object']['key']
    s3objectName = unquote(s3object[8:-4])

    print({ s3bucket })
    print({ s3objectName })
    print({ s3object })

    source_path = "/tmp"
    # source_path = "./reports-csv-out"

    # save file in tmp
    s3.Bucket(s3bucket).download_file(s3object, source_path + '/' + s3objectName + '.pdf')

    out_path = source_path + '/' + s3objectName + '.csv'

    # read table from temp pdf file
    tabula.convert_into(source_path + '/' + s3objectName + '.pdf', out_path, output_format="csv")

    # upload parsed csv
    s3.Bucket(s3bucket).upload_file(out_path, s3objectName + '.csv')

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
