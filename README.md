# Local Auth System with DynamoDB

This project provides a setup to locally run and test an authentication system using a mock website. It leverages DynamoDB Local for database interactions, allowing you to simulate an environment close to production without connecting to AWS cloud services.

## Prerequisites

Before you start, ensure you have DynamoDB Local installed on your machine. For instructions on how to install DynamoDB Local, refer to the [official AWS documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html).

## Getting Started

### Initializing DynamoDB Local

First, start your DynamoDB Local instance. Once it's running, create the necessary table with the following command:

```bash
aws dynamodb create-table \
    --table-name AgoroAuthTable \
    --attribute-definitions AttributeName=PK,AttributeType=S AttributeName=SK,AttributeType=S \
    --key-schema AttributeName=PK,KeyType=HASH AttributeName=SK,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --endpoint-url http://localhost:8000
```
This command sets up AgoroAuthTable with the necessary key schema for your authentication data.
Verifying Table Creation

To confirm that your table has been successfully created in DynamoDB Local, run:

```
aws dynamodb list-tables --endpoint-url http://localhost:8000
```
You should see AgoroAuthTable listed among the tables in your local DynamoDB instance.
Running the Mock Website

Navigate to the directory containing your mock website files (index.html and app.js). Start a simple HTTP server on port 8081:

```
python -m http.server 8081
```
Now, you can open http://localhost:8081 in your web browser to interact with your mock website and test the authentication flow.
Verifying Data in DynamoDB

After inputting data through the mock website, you can verify that the information has been correctly saved to AgoroAuthTable by scanning the table:

```
aws dynamodb scan --table-name AgoroAuthTable --endpoint-url http://localhost:8000
```
This command returns all items in AgoroAuthTable, allowing you to inspect the saved authentication data.
