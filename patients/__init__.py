from flask import Flask, jsonify

app = Flask(__name__)

app.config.from_object('patients.config.DevelopmentConfig')

@app.route('/patients/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'sucess',
        'message': 'pong!'
    })
