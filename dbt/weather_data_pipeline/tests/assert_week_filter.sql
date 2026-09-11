select date_day
from {{ ref('week_weather_report') }}
where
    date_day < {{ current_date_timezone() }}
    or date_day > {{ current_date_timezone() }} + interval '7' day
