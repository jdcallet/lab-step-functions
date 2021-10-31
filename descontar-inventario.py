import boto3
import json
import os

tabla_inventario = os.environ["TABLA_INVENTARIO"]

dynamodb = boto3.resource("dynamodb")
tabla = dynamodb.Table(tabla_inventario)

def lambda_handler(event, context):
    print(event)
    respuesta_get_item = tabla.get_item(Key={"id": event["articulo"], "categoria": event["categoria_articulo"]})
    print(respuesta_get_item)
    nuevo_inventario = respuesta_get_item["Item"]["cantidad_disponible"] - 1
    data = {}
    data["id"] = respuesta_get_item["Item"]["id"]
    data["categoria"] = respuesta_get_item["Item"]["categoria"]
    data["cantidad_disponible"] = nuevo_inventario
    respuesta_put_item = tabla.put_item(
        Item=data
    )
    print(respuesta_put_item)
    data_orden = {}
    
