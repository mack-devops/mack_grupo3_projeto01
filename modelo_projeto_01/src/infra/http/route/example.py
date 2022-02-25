import flask
from flask import jsonify


import src.controller.apiv as apiv
import src.infra.http.auth as auth
from src.infra.utility.http import Http


def route(app: flask.app.Flask):
    @app.route('/data', methods=['GET'])
    @auth.requires_auth
    def request_get_data():
        try:
            response = apiv.get()

            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500

    @app.route('/data', methods=['POST'])
    @auth.requires_auth
    def request_post_data():
        try:
            response = apiv.post(request)

            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
