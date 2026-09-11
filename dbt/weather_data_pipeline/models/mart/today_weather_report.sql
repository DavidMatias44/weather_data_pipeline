{{
    config(
        materialized='table'
    )
}}

select
    latitude,
    longitude,
    elevation,
    temperature,
    temp_categorized,
    precip_prob,
    precip_prob_categorized,
    to_char(time, 'HH24:MI') as hour_
from {{ ref('int_weather_enriched') }}
where
    time::date = {{ current_date_timezone() }}
    and is_current = 1
order by extract(hour from time)
