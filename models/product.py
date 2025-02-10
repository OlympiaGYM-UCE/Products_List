from mongoengine import Document, fields

class Product(Document):
    nombre = fields.StringField(required=True)
    cantidad = fields.IntField(required=True, min_value=0)
    precio = fields.FloatField(required=True, min_value=0)