import requests

def test_get_successful_response():
    response = requests.get("http://techstepacademy.com/training-ground")
    assert response.status_code == 200
