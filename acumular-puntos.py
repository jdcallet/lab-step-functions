import boto3
import json
import os

from boto3.dynamodb.conditions import Attr

tabla_compradores = os.environ["TABLA_COMPRADORES"]

dynamodb = boto3.resource("dynamodb")
tabla = dynamodb.Table(tabla_compradores)

def lambda_handler(event, context):
    print(event)
    respuesta_get_item = tabla.get_item(Key={"id": event["id_comprador"]})
    print(respuesta_get_item)
    if "Item" in respuesta_get_item.keys():
        puntos = respuesta_get_item["Item"]["puntos"] + 100
        data = {}
        data["id"] = event["id_comprador"]
        data["puntos"] = puntos
        respuesta_put_item = tabla.put_item(
            Item=data
        )
        print(respuesta_put_item)
    
    else:
        data["id"] = event["id_comprador"]
        data["puntos"] = 0
        respuesta_put_item = tabla.put_item(
            Item=data
        )
        print(respuesta_put_item)
    