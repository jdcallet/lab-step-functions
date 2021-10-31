import boto3
import json
import os

from boto3.dynamodb.conditions import Attr

tabla_ordenes = os.environ["TABLA_ORDENES"]

dynamodb = boto3.resource("dynamodb")
tabla = dynamodb.Table(tabla_ordenes)

def lambda_handler(event, context):
    print(event)
    event["estado"] = "Procesando"
    respuesta_put_item = tabla.put_item(
        Item=event, ConditionExpression=Attr("id").not_exists()    
    )
    print(respuesta_put_item)
    
