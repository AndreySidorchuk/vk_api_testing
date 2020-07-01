import pytest
import requests


@pytest.mark.parametrize('user_ids, expected_status', [
    ('603890148', 200),
    ('a', 200),
])
def test_users_getting(user_ids, expected_status):

    response = requests.get('https://api.vk.com/method/users.get?'
                            f'user_ids={user_ids}&'
                            'fields=photo_50,city,verified&'
                            'name_case=Nom&'
                            'v=5.110&'
                            'access_token=15664b648ff26dc99890f7e7c77ed9722965752f94f8d724962be47dc1eb7dcca1a42a68c0ac30aba2ce3')
    assert response.status_code == expected_status
