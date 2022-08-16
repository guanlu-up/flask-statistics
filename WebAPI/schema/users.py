from marshmallow import Schema, fields


class UserSchema(Schema):

    id = fields.Integer()
    username = fields.String()
    is_admin = fields.Boolean()

    create_time = fields.DateTime()
    update_time = fields.DateTime()


class UserExtensionSchema(Schema):
    school = fields.String()
    interest = fields.String()
