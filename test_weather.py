from model import get_weather
from unittest.mock import patch, MagicMock
from httpx import HTTPStatusError, RequestError

# test review with success (status 200)
@patch('model.client.get')
def test_get_weather_success(mock_get):
    fake_response = MagicMock()
    fake_response.json.return_value = {
            "name": "haifa",
            "main": {"temp": 30.0},
            "weather": [{"description": "clear sky"}]
        }
    mock_get.return_value = fake_response
    print("!!!The testing start!!!\n")
    get_weather("Haifa")
    print("!!!Testing successful!!!\n")

# Review test with 'The requested page is not found' failure (status 404)
@patch('model.client.get')
def test_get_weather_city_not_found(mock_get):
    fake_response = MagicMock()
    fake_response.status_code = 404

    fake_response.raise_for_status.side_effect = HTTPStatusError(
        "name of City not found", request = MagicMock(), response = fake_response
    )
        
    mock_get.return_value = fake_response
    print("!!!We starting testing for status 404 start!!!\n")
    get_weather("Haifa")
    print("!!!Testing (404) successful!!!\n")

# Specifies that calling the function will throw an HTTPStatusError error.
@patch('model.client.get')
def test_get_weather_unauthorized_access(mock_get):
    fake_response = MagicMock()
    fake_response.status_code = 401

    fake_response.raise_for_status.side_effect = HTTPStatusError(
        "Unauthorized", request = MagicMock(), response = fake_response
    )
        
    mock_get.return_value = fake_response
    print("!!!We starting testing for status 401 start!!!\n")
    get_weather("Haifa")
    print("!!!Testing (401) successful!!!\n")

@patch('model.client.get')
def test_get_weather_RequestError(mock_get):
    fake_response = MagicMock()
    
    mock_get.side_effect = RequestError("NO-INTERNET-CONNECTION", request = MagicMock())
        
   # mock_get.return_value = fake_response
    print("!!!We starting testing for Request Error!!!\n")
    get_weather("Haifa")
    print("!!!Testing (RequestError) successful!!!\n")

def run_all_tests():
    print("Now we will run tests to verify the code's validity:")
    test_get_weather_success()
    test_get_weather_city_not_found()
    test_get_weather_unauthorized_access()
    test_get_weather_RequestError()
    print("<<<<We have completed all the tests.>>>>")