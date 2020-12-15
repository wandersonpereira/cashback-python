from marshmallow import Schema, fields, validate, ValidationError
import datetime

class OrderModel(Schema):
    code: str = fields.String(required=True)
    value: str = fields.Float(required=True)
    date: str = fields.String(missing=datetime.datetime.utcnow())
    document: str = fields.String(required=True)
    status: str = fields.String(missing='Em validação')