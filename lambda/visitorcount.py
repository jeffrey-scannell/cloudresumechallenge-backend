import json
import boto3

client = boto3.client('dynamodb')
client = boto3.resource("dynamodb")
table = client.Table("visitorcount")

def lambda_handler(event, context):
    response = table.get_item(
        Key = {'name' : 'count'}
    )
    count = response["Item"]["visitor_count"]
    new_count = int(count)+1
    response = table.update_item(
        Key = {'name' : 'count'},
        UpdateExpression="SET visitor_count = :c",
        ExpressionAttributeValues={':c': new_count},
        ReturnValues="UPDATED_NEW"
        )
    return {'count':new_count}