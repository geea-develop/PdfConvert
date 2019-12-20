import json
import tabula
import shutil
import os


def handler(event, context):
    # Read pdf into DataFrame

    tabula.convert_into_by_batch("reports-pdf-in", output_format='csv')

    source_path="reports-pdf-in"
    source_files = os.listdir(source_path)
    destination_path = 'reports-csv-out'
    for file in source_files:
        if file.endswith('.csv'):
            shutil.move(os.path.join(source_path, file), os.path.join(destination_path, file))

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
