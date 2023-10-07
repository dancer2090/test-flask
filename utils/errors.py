from flask import json
from werkzeug.exceptions import HTTPException


def handle_page_not_found(e):

    if e.code == 500:
        print(e)

    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response


def register_app_errors(app):
    app.register_error_handler(HTTPException, handle_page_not_found)