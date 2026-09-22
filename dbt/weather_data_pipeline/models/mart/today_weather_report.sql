{{
    config(
        materialized='table'
    )
}}

select
    hour_,
    latitude,
    longitude,
    elevation,
    temperature,
    temp_categorized,
    precip_prob,
    precip_prob_categorized,
    valid_from,
    valid_to,
    is_current
from (
    select
        latitude,
        longitude,
        elevation,
        temperature,
        temp_categorized,
        precip_prob,
        precip_prob_categorized,
        valid_from,
        valid_to,
        is_current,
        row_number() over (partition by time order by valid_to desc) as rn,
        to_char(time, 'hh24:mi') as hour_
    from {{ ref('int_weather_enriched') }}
    where time::date = {{ current_date_timezone() }}
) as t1
where rn <= 3
order by hour_ asc, rn desc
