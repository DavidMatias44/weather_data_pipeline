select
    min_precip_prob,
    max_precip_prob
from {{ ref('week_weather_report') }}
where min_precip_prob > max_precip_prob
