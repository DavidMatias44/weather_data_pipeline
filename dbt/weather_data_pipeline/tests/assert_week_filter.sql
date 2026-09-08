select
    date_day
from {{ ref('week_weather_report') }}
where date_day < current_date or date_day > current_date + interval '7' day
