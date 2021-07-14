from flask import json

from app import app


def test_index0():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'{"data": 0}'


def test_index1():
    response = app.test_client().get('/1')
    assert response.status_code == 200
    assert response.data == b'{"data": 1}'


def test_index2():
    response = app.test_client().get('/2')
    assert response.status_code == 200
    assert response.data == b'{"data": 2}'


def test_index3():
    response = app.test_client().get('/3')
    assert response.status_code == 200
    assert response.data == b'{"data": 3}'


def test_index4():
    response = app.test_client().get('/4')
    assert response.status_code == 200
    assert response.data == b'{"data": 4}'


def test_add():
    temp = {
        "a":10,
        "b":20
    }
    response = app.test_client().post(
        '/add',
        data=json.dumps(temp),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['sum'] == temp["a"]+temp["b"]
