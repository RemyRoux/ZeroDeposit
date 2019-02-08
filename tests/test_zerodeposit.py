# tests/test_zerodeposit.py

import pytest
from zerodeposit import create_app, get_current_rates
import mock

def test_get_current_rates():
    assert round(get_current_rates(),2) == round(1.13736,2)


def test_number_of_blocks(client):
    response = client.get('/')
    assert b'7' in response.data
    print(response.data)