import os
import pytest

from unittest import TestCase
from run import create_app


class TestTestingConfig(TestCase):
    app = create_app("testing")
    
    def test_app_is_testing(self):
        self.assertTrue(self.app.config['DEBUG'] is True)
        self.assertTrue(self.app.config['TESTING'] is True)


class TestDevelopmentConfig(TestCase):
    app = create_app("development")
    
    def test_app_is_development(self):
        self.assertTrue(self.app.config['DEBUG'] is True)
    


class TestProductionConfig(TestCase):
    app = create_app("production")
    
    def test_app_is_production(self):
        self.assertTrue(self.app.config['DEBUG'] is False)
        self.assertTrue(self.app.config['TESTING'] is False)