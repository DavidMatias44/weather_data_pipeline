import logging

from schemas import APIResponse

logger = logging.getLogger(__name__)


def flat_raw_data(raw_data: APIResponse) -> list[list[float | str | int]]:
    latitude = raw_data.latitude
    longitude = raw_data.longitude
    elevation = raw_data.elevation
    hourly = raw_data.hourly

    records = [
        [time, latitude, longitude, elevation, temperature, precipitation_prob]
        for time, temperature, precipitation_prob in zip(
            hourly.time, hourly.temperature_2m, hourly.precipitation_probability
        )
    ]

    logger.debug("Flattened %d records successfully", len(records))
    return records
