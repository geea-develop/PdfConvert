# PdfConvert SLS PYTHON

Create Project

    sls create -p my-serverless-project -t aws-python3

Add Python Requirements

    sls plugin install -n serverless-python-requirements

Invoke Function Locally

    serverless invoke local --function ConvertToCsv

Invoke Function Locally

    serverless invoke local --function functionName --data "hello world"

Invoke Function Locally

    serverless invoke local --function functionName --data '{"a":"bar"}'

Invoke Function Locally

    serverless invoke local --function functionName --path lib/data.json

---
>.
---
***DONT RUN THIS*** 

sls remove