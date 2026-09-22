{{
    config(
        materialized='table'
    )
}}

select
    rn,
    time::date as date_day,
    latitude,
    longitude,
    elevation,
    is_current,
    min(temperature) as min_temperature,
    round(avg(temperature::numeric), 2) as avg_temperature,
    max(temperature) as max_temperature,
    min(precip_prob) as min_precip_prob,
    round(avg(precip_prob), 2) as avg_precip_prob,
    max(precip_prob) as max_precip_prob
from (
    select
        time,
        latitude,
        longitude,
        elevation,
        temperature,
        precip_prob,
        is_current,
        row_number() over (partition by time order by valid_to desc) as rn
    from {{ ref('int_weather_enriched') }}
    where
        time::date between {{ current_date_timezone() }}
        and {{ current_date_timezone() }} + interval '7' day
) as t1
where rn <= 3
group by 2, 1, 3, 4, 5, 6
