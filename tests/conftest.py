# tests/conftest.py

import os,sys
import tempfile

import pytest
from zerodeposit import create_app


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True, 
    })
    
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()
    
@pytest.fixture
def runner(app):
    return app.test_cli_runner()


def pytest_configure(config):
    import sys
    
    sys._called_from_test = True


def pytest_unconfigure(config):
    import sys
    
    del sys._called_from_test
    
