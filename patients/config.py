import os

class BaseConfig:
    """ Base Configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret'
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """ Development Configuration """
    SQLALCHEMY_DATABASE_URI ='postgresql://usuario:senha@localhost:5432/dev.db'
    DEBUG = True
 

class ProductionConfig(BaseConfig):
    """Production Configuration"""
    SQLALCHEMY_DATABASE_URI ='postgresql://usuario:senha@localhost:5432/prod.db'
    



    
