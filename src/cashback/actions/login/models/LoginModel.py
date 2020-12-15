from marshmallow import Schema, fields, validate, ValidationError

class LoginModel(Schema):
    email: str = fields.Email(required=True)
    password: str = fields.String(required=True)
