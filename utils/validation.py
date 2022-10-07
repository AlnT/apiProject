"""API respond validation"""
import json

from requests import Response


class Validation():
    """Status code validation method"""
    @staticmethod
    def val_status_code(responce: Response, status_code):
        assert status_code == responce.status_code

    """Mandatory fields validation"""
    @staticmethod
    def val_json_token(response: Response, expected):
        token = response.json()
        assert list(token) == expected

    """Mandatory fields value validation"""
    @staticmethod
    def val_json_value(response: Response, field_name, expected):
        assert response.json().get(field_name) == expected

