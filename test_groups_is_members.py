import pytest
import requests


@pytest.mark.parametrize('user_id, expected_result', [
    ('603890148', {"response": [{"member": 1, "user_id": 603890148}]}),
    ('1', {"response": [{"member": 0, "user_id": 1}]}),
    ('603890148,1', {"response": [{"member": 1, "user_id": 603890148}, {"member": 0, "user_id": 1}]}),
])
def test_user_is_member(user_id, expected_result):

    response = requests.get('https://api.vk.com/method/groups.isMember?'
                            f'user_ids={user_id}&'
                            f'group_id=27429141&'
                            'v=5.110&'
                            'access_token=15664b648ff26dc99890f7e7c77ed9722965752f94f8d724962be47dc1eb7dcca1a42a68c0ac30aba2ce3')
    print(response.text)
    assert response.status_code == 200
    assert response.json() == expected_result
