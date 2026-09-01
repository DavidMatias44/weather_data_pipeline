{{
    config(
        materialized='table'
    )
}}

select
    time::date as date_day,
    latitude,
    longitude,
    elevation,
    round(avg(temperature::numeric), 2) as avg_temperature,
    min(temperature) as min_temperature,
    max(temperature) as max_temperature,
    round(avg(precip_prob), 2) as avg_precip_prob,
    min(precip_prob) as min_precip_prob,
    max(precip_prob) as max_precip_prob
from {{ ref('int_weather_enriched') }}
where time::date between current_date and current_date + interval '7' day
group by 1, 2, 3, 4
