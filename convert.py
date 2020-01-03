import json
import tabula
import boto3


# Create an S3 client
s3 = boto3.client('s3')

def handler(event, context):
    # Read pdf into DataFrame

    print(json.dumps(event))

    record = event['Records'][0]

    s3bucket = record['s3']['bucket']['name']
    s3object = record['s3']['object']['key']

    source_path = "/tmp"

    s3.Bucket(s3bucket).download_file(s3object, source_path + '/' + s3object)

    tabula.convert_into_by_batch("/tmp/reports-pdf-in", output_format='csv')

    try:
        s3.Bucket(s3bucket).upload_file(source_path + '/' + s3object, '/reports-csv-out/' + s3object)
    except Exception as e:
        print(e)

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
