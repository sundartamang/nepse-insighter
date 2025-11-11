from flask import Blueprint
from werkzeug.exceptions import BadRequest
from utils.response import success_response, error_response
from constants.status_codes import BAD_REQUEST, INTERNAL_SERVER_ERROR
from api.fetch_data_from_api import get_anu_valuation

# Create a blueprint instance
nepse_insighter_api = Blueprint('nepse_insighter_api', __name__)

@nepse_insighter_api.route('/ansu/valuation', methods=['GET'])
def get_ansu_valuation_endpoint():
    try:
        response = get_anu_valuation()
        return success_response(response)
    except BadRequest as e:
        return error_response(e.description, BAD_REQUEST)
    except Exception as e:
        return error_response(f"An unexpected error occurred: {str(e)}", INTERNAL_SERVER_ERROR)
