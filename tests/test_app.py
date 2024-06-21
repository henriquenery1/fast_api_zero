from http import HTTPStatus


def test_root_deve_retornar_ok_e_Hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world!'}
