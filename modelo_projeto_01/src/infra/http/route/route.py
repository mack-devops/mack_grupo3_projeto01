import flask
from flask import jsonify
from flask import request
import src.controller.apiv as apiv
import src.infra.http.auth as auth
from src.infra.utility.http import Http


def route(app: flask.app.Flask):
    @app.route('/', methods=['GET'])
    def get_status_api():
        return 'API Online'

    @app.route('/getAll', methods=['GET'])
    @auth.requires_auth
    def getAll():
        try:
            response = apiv.getAll()
            return jsonify(response), 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)
            return jsonify(response), 500

    @app.route('/getByIdAndName', methods=['GET'])
    @auth.requires_auth
    def getByIdAndName():
        try:
            response = apiv.getByIdAndName()
            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)
            return jsonify(response), 500

    @app.route('/getAverageValuebyManufacturer', methods=['GET'])
    @auth.requires_auth
    def getAverageValuebyManufacturer():
        try:
            response = apiv.getAverageValuebyManufacturer()
            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)
            return jsonify(response), 500

    @app.route('/getAverageValuebyManufacturerFiltredByValue', methods=['POST'])
    @auth.requires_auth
    def getAverageValuebyManufacturerFiltredByValue():
        try:
            # recebendo todos os parametros no body
            request_data = request.get_json()
            # capturando o parametro car_make
            p_car_make = request_data['car_make']
            response = apiv.getAverageValuebyManufacturerFiltredByValue(p_car_make)
            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)
            return jsonify(response), 500

    @app.route('/getAverageValueByCity', methods=['GET'])
    @auth.requires_auth
    def getAverageValueByCity():
        try:
            response = apiv.getAverageValueByCity()
            return response, 200
        except Exception as err:
            response = Http.handle_generic_http_error(err)
            return jsonify(response), 500

    @app.route('/getAverageValueByCityFiltredByValue', methods=['POST'])
    @auth.requires_auth
    def getAverageValueByCityFiltredByValue():
        try:
            # recebendo todos os parametros no body
            request_data = request.get_json()
            # capturando o parametro car_make
            p_city = request_data['city']
            response = apiv.getAverageValueByCityFiltredByValue(p_city)
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
