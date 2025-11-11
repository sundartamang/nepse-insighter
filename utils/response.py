from flask import jsonify
from constants.status_codes import OK, BAD_REQUEST

def success_response(data=None, message="Data fetched successfully", status_code=OK):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status_code


def error_response(message, status_code=BAD_REQUEST):
    return jsonify({
        "status": "error",
        "message": message,
    }), status_code
