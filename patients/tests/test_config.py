import os
import unittest
from flask import current_app
from flask_testing import TestCase
from patients import create_app

class TestDevelopmentConfig(TestCase):
    def create_app(self):        
        app = create_app()
        app.config.from_object('patients.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        app = create_app()
        self.assertTrue(app.config['SECRET_KEY']== 'secret')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:mktj@localhost:5432/kompa_dev')
        
class TestProductionConfig(TestCase):
    def create_app(self):        
        app = create_app()
        app.config.from_object('patients.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        app = create_app()
        self.assertTrue(app.config['SECRET_KEY'] == 'secret')
        self.assertFalse(app.config['TESTING'])

if __name__ == '__main__':
    unittest.main()
