import requests


def all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) > 0, 'Нет объектов'
    return response


def get_object():
    obj_id = new_object()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{obj_id}').json()
    assert response['id'] == obj_id
    return response


def post_an_object():
    body = {
        "name": "Created Object",
        "data": {
            "color": "QA",
            "size": "Manual"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    assert response.status_code == 200, 'Статус код неверный'
    assert response.json()['id'] is not None, 'ID отсутствует'
    print(response)


def new_object():
    body = {
        "name": "Test Object",
        "data": {
            "color": "AQA",
            "size": "Automation"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(obj_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')


def put_object():
    obj_id = new_object()
    body = {
        "name": "Blue Curacao",
        "data": {
            "color": "in the Middle on the Night",
            "size": "little big"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{obj_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Blue Curacao'
    print(response)
    clear(obj_id)


def patch_object():
    obj_id = new_object()
    body = {
        "name": "Patch name"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{obj_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Patch name'
    print(response)
    clear(obj_id)


def delete_an_object():
    obj_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    assert response.status_code == 200, 'Статус код неверный'
