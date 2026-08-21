from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_url: str = Field(alias="BASE_URL")
    latitude: float = Field(ge=-90, le=90, alias="LATITUDE")
    longitude: float = Field(ge=-180, le=180, alias="LONGITUDE")
    hourly: str = Field(alias="HOURLY")
    timezone: str = Field(alias="TIMEZONE")
    forecast_days: int = Field(ge=1, le=16, alias="FORECAST_DAYS")

    db_name: str = Field(alias="POSTGRES_DB")
    db_user: str = Field(alias="POSTGRES_USER")
    db_password: str = Field(alias="POSTGRES_PASSWORD")
    db_host: str = Field(alias="POSTGRES_HOST")
    db_port: int = Field(alias="POSTGRES_PORT")
    db_schema: str = Field(alias="POSTGRES_SCHEMA")
    db_raw_data_table: str = Field(alias="POSTGRES_RAW_DATA_TABLE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
