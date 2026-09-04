from src.schemas import APIResponse, Hourly
from src.transform import flat_raw_data


def test_flat_raw_data() -> None:
    mock_hourly = Hourly(
        time=["2026-09-03T00:00", "2026-09-03T01:00"],
        temperature_2m=[19.3, 18.7],
        precipitation_probability=[5, 10]
    )
    mock_raw_data = APIResponse(
        latitude=34.0258,
        longitude=-118.7804,
        elevation=1500,
        hourly=mock_hourly
    )

    res = flat_raw_data(raw_data=mock_raw_data)

    assert len(res) == 2
    assert res[0] == ["2026-09-03T00:00", 34.0258, -118.7804, 1500, 19.3, 5]
    assert res[1] == ["2026-09-03T01:00", 34.0258, -118.7804, 1500, 18.7, 10]
