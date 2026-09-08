select
    min_temperature,
    max_temperature
from {{ ref('week_weather_report') }}
where min_temperature > max_temperature
