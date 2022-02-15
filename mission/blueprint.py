from flask import Blueprint, jsonify

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/ping', methods=['GET',])
def jg():
        j = {
            'statusCode' : 200,
            'message' : "Hello, World!"}
        return jsonify(j)

@bp.route('/api/v1/custom', methods=['GET',])
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
