import pytest
from pydantic import ValidationError

from src.schemas import APIResponse, Hourly


def test_api_response_valid_data():
    valid_data = {
        "latitude": 34.0258,
        "longitude": -118.7804,
        "elevation": 1500,
        "hourly": {
            "time": ["2026-09-03T00:00", "2026-09-03T01:00"],
            "temperature_2m": [19.3, 18.7],
            "precipitation_probability": [5, 10],
        },
    }

    response = APIResponse(**valid_data)

    assert response.latitude == 34.0258
    assert response.longitude == -118.7804
    assert response.elevation == 1500
    assert isinstance(response.hourly, Hourly)
    assert response.hourly.temperature_2m == [19.3, 18.7]
    assert response.hourly.precipitation_probability == [5, 10]


def test_api_response_missing_required_field_raises_error():
    invalid_data = {"latitude": 34.0258, "longitude": -118.7804, "elevation": 1500}

    with pytest.raises(ValidationError):
        APIResponse(**invalid_data)


def test_api_response_invalid_data_type_raises_error():
    invalid_data = {
        "latitude": "not valid",
        "longitude": -118.7804,
        "elevation": 1500,
        "hourly": {
            "time": ["2026-09-03T00:00"],
            "temperature_2m": [19.3],
            "precipitation_probability": [5],
        },
    }

    with pytest.raises(ValidationError):
        APIResponse(**invalid_data)
