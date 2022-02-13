from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/ping', methods=['GET',])
    def jg():
        jj = {
            'statusCode' : 200,
            'message' : "Hello, World!"}
        return jsonify(jj)
    return app

def create_app():
    app = Flask(__name__)

    @app.route('/api/v1/custom', methods=['GET',])
    def jg2():
        jj = {
            'statusCode' : 200,
            'message' : "Good",
            'body' : {
                'gps' : {
                    'latitude' : 12.4,
                    'longitude' : 243.1
                }
            }
        }
        return jsonify(jj)
    return app
