import pytest
import requests
import json

@pytest.fixture
def supply_url():
    return "http://localhost:5000"


def test_basic_url(supply_url):
    url = supply_url + "/"
    print(url)
    response = requests.get(url)
    response_body = response.json()
    assert response.status_code == 200
    assert response_body == "Please use /std URI to view content"

def test_post_request(supply_url):
    url = supply_url + "/std"
    headers = {'Content-Type': 'application/json'}
    payload = { 'name': 'User1', 'ranklevel': '25'}
    response = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert response.status_code == 200
    print(response.text)

def test_invalid_entry(supply_url):
    url = supply_url + "/User2"
    response = requests.get(url)
    assert response.status_code == 404
    print(response.text)

