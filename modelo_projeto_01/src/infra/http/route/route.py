import flask
from flask import jsonify
import src.controller.apiv as apiv
import src.infra.http.auth as auth
from src.infra.utility.http import Http


def route(app: flask.app.Flask):
    @app.route('/', methods=['GET'])
    def get_status_api():
        return 'API Online'

    @app.route('/getAll', methods=['GET'])
    @auth.requires_auth
    def get_all():
        try:
            response = apiv.getAll()
            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)
            return jsonify(response), 500

    @app.route('/getByIdAndName', methods=['GET'])
    @auth.requires_auth
    def get_by_id_and_name():
        try:
            response = apiv.getByIdAndName()
            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)
            return jsonify(response), 500

            

    @app.route('/data', methods=['POST'])
    @auth.requires_auth
    def request_post_data():
        try:
            response = apiv.post()

            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)

            return jsonify(response), 500
