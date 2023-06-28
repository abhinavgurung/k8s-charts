import logging
import requests


from flask import Blueprint, jsonify, request, g, make_response

requests_view = Blueprint('requests', __name__)


@requests_view.route("/test", methods=["GET"])
def get_test():
    logging.warning("got api request")
    info = {
        "school" : 'Federal University Of Technology Owerri',
        "department" : "Biochemistry",
        'level': "500L"
    }
    return jsonify(info) # returning a JSON response

