import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)  
    app.config.from_object('patients.config.DevelopmentConfig')
    db.init_app(app)
        

    #register blueprints
    from patients.api.patients import patients_blueprint
    app.register_blueprint(patients_blueprint)

    #flask cli shell context
    app.shell_context_processor({'app': app, 'db': db})
    return app

    





