import pytest
import requests


@pytest.mark.parametrize('ids_count', [
    0,
    1,
    2,
    10,
    100,
    500,
])
def test_valid_getting_by_group_ids(ids_count):
    # Генерируем group ids начиная с 2, поскольку группы с id == 1 не существует
    group_ids = ','.join([str(group_id) for group_id in range(2, ids_count + 2)])

    response = requests.get('https://api.vk.com/method/groups.getById?'
                            f'group_ids={group_ids}&'
                            'v=5.110&'
                            'access_token=15664b648ff26dc99890f7e7c77ed9722965752f94f8d724962be47dc1eb7dcca1a42a68c0ac30aba2ce3')

    assert response.status_code == 200
    assert len(response.json().get('response', [])) == ids_count


@pytest.mark.parametrize('ids_count', [
    501,
    1000
])
def test_overhead_getting_by_group_ids(ids_count):
    # Генерируем group ids начиная с 2, поскольку группы с id == 1 не существует
    group_ids = ','.join([str(group_id) for group_id in range(2, ids_count + 2)])

    response = requests.get('https://api.vk.com/method/groups.getById?'
                            f'group_ids={group_ids}&'
                            'v=5.110&'
                            'access_token=15664b648ff26dc99890f7e7c77ed9722965752f94f8d724962be47dc1eb7dcca1a42a68c0ac30aba2ce3')

    assert response.status_code == 200
    assert len(response.json().get('response', [])) == 500


@pytest.mark.parametrize('group_id', [
    1,
    501,
    1000
])
def test_getting_by_group_id(group_id):

    response = requests.get('https://api.vk.com/method/groups.getById?'
                            f'group_id={group_id}&'
                            'v=5.110&'
                            'access_token=15664b648ff26dc99890f7e7c77ed9722965752f94f8d724962be47dc1eb7dcca1a42a68c0ac30aba2ce3')
    assert response.status_code == 200
    response_body = response.json()
    if len(response_body.get('response', [])) == 1:
        assert response_body['response'][0].get('id') == group_id
