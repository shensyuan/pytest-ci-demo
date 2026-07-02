from unittest.mock import patch, Mock
from src.data_service import DataService


def test_get_data_from_cache():
    service = DataService()
    service.cache["foo"] = "cached_value"
    result = service.get_data("foo")
    assert result == "cached_value"


@patch("src.data_service.requests.get")
def test_get_data_from_api(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1}
    mock_get.return_value = mock_response

    service = DataService(api_url="https://test.api")
    result = service.get_data("key1")

    assert result == {"id": 1}
    assert service.cache["key1"] == {"id": 1}
    mock_get.assert_called_once_with("https://test.api/data/key1")


@patch("src.data_service.requests.get")
def test_get_data_api_fails(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    service = DataService()
    import pytest
    with pytest.raises(Exception, match="Failed to get data for key: bad"):
        service.get_data("bad")


@patch("src.data_service.requests.post")
def test_save_data_success(mock_post):
    mock_response = Mock()
    mock_response.status_code = 201
    mock_post.return_value = mock_response

    service = DataService(api_url="https://test.api")
    result = service.save_data("k", "v")

    assert result is True
    mock_post.assert_called_once_with(
        "https://test.api/data",
        json={"k": "v"},
    )


@patch("src.data_service.requests.post")
def test_save_data_fails(mock_post):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_post.return_value = mock_response

    service = DataService()
    result = service.save_data("k", "v")

    assert result is False


@patch("src.data_service.requests.get")
def test_get_external_config_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"theme": "dark"}
    mock_get.return_value = mock_response

    service = DataService(api_url="https://test.api")
    result = service.get_external_config()

    assert result == {"theme": "dark"}
    mock_get.assert_called_once_with("https://test.api/config")


@patch("src.data_service.requests.get")
def test_get_external_config_fails(mock_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    service = DataService()
    result = service.get_external_config()

    assert result == {}
