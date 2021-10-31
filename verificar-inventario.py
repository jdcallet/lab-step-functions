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
    if respuesta_get_item["Item"]:
        if respuesta_get_item["Item"]["cantidad_disponible"] > 0:
            print("Producto disponible")
            return {"en_inventario": True}
        else:
            print("Producto no disponible")
            return {"en_inventario": False}
    

