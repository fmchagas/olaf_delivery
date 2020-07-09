import pytest
from olaf_delivery.app import create_app


@pytest.fixture(scope="module")
def app():
    """Insatance of Main flask app"""
    return create_app()
