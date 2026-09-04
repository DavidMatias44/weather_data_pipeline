from pydantic import ValidationError
from pytest import MonkeyPatch, raises

from src.config import Settings


def test_settings_valid_env(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("BASE_URL", "https://mock-api.com")
    monkeypatch.setenv("LATITUDE", "34.0258")
    monkeypatch.setenv("LONGITUDE", "-118.7804")
    monkeypatch.setenv("HOURLY", "temperature_2m,precipitation_probability")
    monkeypatch.setenv("TIMEZONE", "America/Denver")
    monkeypatch.setenv("FORECAST_DAYS", "16")
    monkeypatch.setenv("POSTGRES_DB", "db")
    monkeypatch.setenv("POSTGRES_USER", "user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "pass")
    monkeypatch.setenv("POSTGRES_HOST", "localhost")
    monkeypatch.setenv("POSTGRES_PORT", "5432")
    monkeypatch.setenv("POSTGRES_SCHEMA", "public")
    monkeypatch.setenv("POSTGRES_RAW_DATA_TABLE", "raw_weather")

    settings = Settings()

    assert settings.latitude == 34.0258
    assert settings.longitude == -118.7804
    assert settings.forecast_days == 16


def test_settings_invalid_env(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("BASE_URL", "https://mock-api.com")
    monkeypatch.setenv("LATITUDE", "200.0")
    monkeypatch.setenv("LONGITUDE", "-118.7804")
    monkeypatch.setenv("HOURLY", "temperature_2m,precipitation_probability")
    monkeypatch.setenv("TIMEZONE", "America/Denver")
    monkeypatch.setenv("FORECAST_DAYS", "16")
    monkeypatch.setenv("POSTGRES_DB", "db")
    monkeypatch.setenv("POSTGRES_USER", "user")
    monkeypatch.setenv("POSTGRES_PASSWORD", "pass")
    monkeypatch.setenv("POSTGRES_HOST", "localhost")
    monkeypatch.setenv("POSTGRES_PORT", "5432")
    monkeypatch.setenv("POSTGRES_SCHEMA", "public")
    monkeypatch.setenv("POSTGRES_RAW_DATA_TABLE", "raw_weather")

    with raises(ValidationError):
        Settings()
