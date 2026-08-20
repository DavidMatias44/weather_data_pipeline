from pydantic import BaseModel


class Hourly(BaseModel):
    time: list[str]
    temperature_2m: list[float]
    precipitation_probability: list[int]


class APIResponse(BaseModel):
    latitude: float
    longitude: float
    elevation: int
    hourly: Hourly
