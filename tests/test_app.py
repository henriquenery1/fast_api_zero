from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_api_zero.app import app

def test_root_deve_retornar_ok_e_Hello_world():
	client = TestClient(app)
	
	response = client.get('/')

	assert response.status_code == HTTPStatus.OK
	assert response.json() == {"mesage":"Hello world!"}

