from http import HTTPStatus


def test_root_deve_retornar_ok_e_Hello_world(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world!'}


def test_deve_retornar_usuario_criado(client):
    response = client.post(
        '/users', json={'username': 'str', 'email': 'test@email.com', 'password': '123'}
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'id': 1, 'username': 'str', 'email': 'test@email.com'}
