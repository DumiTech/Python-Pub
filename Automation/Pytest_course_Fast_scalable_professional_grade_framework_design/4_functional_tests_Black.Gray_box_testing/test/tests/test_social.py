import requests

def test_twitter_is_present():
    response = requests.get("http://techstepacademy.com/training-ground")
    assert "twitter" in response.text 
