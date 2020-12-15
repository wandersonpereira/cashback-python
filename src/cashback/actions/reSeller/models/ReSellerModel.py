from marshmallow import Schema, fields, validate, ValidationError

class ReSellerModel(Schema):
    fullName: str = fields.String(required=True)
    email: str = fields.Email(required=True)
    document: str = fields.String(required=True)
    password: str = fields.String(required=True)
