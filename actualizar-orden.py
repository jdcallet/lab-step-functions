import boto3
import json
import os

from boto3.dynamodb.conditions import Attr

tabla_ordenes = os.environ["TABLA_ORDENES"]

dynamodb = boto3.resource("dynamodb")
tabla = dynamodb.Table(tabla_ordenes)

def lambda_handler(event, context):
    print(event)
    data = {}
    data["id"] = event["id"]
    data["articulo"] = event["articulo"]
    data["categoria_articulo"] = event["categoria_articulo"]
    data["metodo_pago"] = event["metodo_pago"]
    data["id_comprador"] = event["id_comprador"]
    data["nombre_comprador"] = event["nombre_comprador"]
    data["afiliado"] = event["afiliado"]
    data["estado"] = "Completada"
    respuesta_put_item = tabla.put_item(
        Item=data    
    )
    print(respuesta_put_item)
