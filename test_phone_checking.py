import pytest
import requests

MANY_REQUESTS_PER_SECOND_ERROR_CODE = 6


@pytest.mark.parametrize('phone', [
    '+79277977567'
])
def test_valid_phone(phone):

    response = requests.get('https://api.vk.com/method/auth.checkPhone?'
                            f'phone={phone}&'
                            'v=5.110&'
                            'access_token=15664b648ff26dc99890f7e7c77ed9722965752f94f8d724962be47dc1eb7dcca1a42a68c0ac30aba2ce3')

    assert response.status_code == 200
    assert response.json() == {'response': 1}


@pytest.mark.parametrize('phone, expected_error_code', [
    ('+79210000000000', 100),
    ('ggfgh', 100),
])
def test_invalid_phone(phone, expected_error_code):

    response = requests.get('https://api.vk.com/method/auth.checkPhone?'
                            f'phone={phone}&'
                            'v=5.110&'
                            'access_token=15664b648ff26dc99890f7e7c77ed9722965752f94f8d724962be47dc1eb7dcca1a42a68c0ac30aba2ce3')
    assert response.status_code == 200

    assert response.json().get('error', {}).get('error_code') in (expected_error_code, MANY_REQUESTS_PER_SECOND_ERROR_CODE)
