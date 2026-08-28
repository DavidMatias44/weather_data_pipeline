{{
    config(
        materialized='table'
    )
}}

select
    to_char(time, 'HH24:MI') as hour,
    latitude,
    longitude,
    elevation,
    temperature,
    temp_categorized,
    precip_prob,
    precip_prob_categorized
from {{ ref('int_weather_enriched') }}
where time::date = current_date
