from marshmallow import Schema, validate, fields, ValidationError
import configurartion


class Validate_Schema(Schema):
    userid = fields.Number(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(required=True) 


def validate_json(json_data):
    try:
        Validate_Schema().load(json_data)
        configurartion.logger('Json format is correct')
        return True
    except ValidationError as x:
        configurartion.logger(f'Json validation error {x}', error=True)
        return False    