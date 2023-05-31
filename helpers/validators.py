from functools import wraps
import json
from flask import abort, make_response, request
from sqlalchemy import inspect


def ValidModel(Model):
    """
    Decorator that checks if the required fields for the model were provided in the request,
    otherwise returns an error message with the list of missing required fields.
    """
    def get_required_fields():
        required_fields = []
        for column in Model.__table__.columns:
            if not column.nullable and not column.primary_key:
                required_fields.append(column.name)
        return required_fields

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if request.method == 'POST' or request.method == 'PUT':
                    if not request.data:
                        # 400 is the HTTP status code for "Bad request" message. It can be changed to any other
                        abort(400, 'No data provided')

                    json_data = json.loads(request.data)
                    if not json_data:
                        return make_response(f'body must contain JSON with this fields : {", ".join(get_required_fields())}', 400)

                    if not all(key in inspect(Model).columns for key in json_data.keys()):
                        modelKeys = set(inspect(Model).columns.keys())
                        extra_keys = ", ".join(
                            set(json_data.keys()) - set(inspect(Model).columns.keys()))
                        return make_response(f'Body contains extra fields: {extra_keys}. Fields allowed : {modelKeys}', 400)
                    required_fields = get_required_fields()
                    missing_fields = set(required_fields) - \
                        set(json_data.keys())
                    if missing_fields:
                        return make_response(f'Required fields not provided: {", ".join(missing_fields)}.', 400)

                    return make_response(func(*args, **kwargs))
            except json.JSONDecodeError as e:
                return make_response(f'body must contain JSON with this fields : {", ".join(get_required_fields())}', 400)
        return wrapper
    return decorator
