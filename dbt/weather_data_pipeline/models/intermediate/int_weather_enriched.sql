{{
    config(
        materialized='table'
    )
}}

select
    id,
    time,
    latitude,
    longitude,
    elevation,
    temperature,
    precip_prob,
    valid_from,
    case
        when temperature < -9 then 'Frigid'
        when temperature < 0 then 'Freezing'
        when temperature < 7 then 'Very cold'
        when temperature < 13 then 'Cold'
        when temperature < 18 then 'Cool'
        when temperature < 24 then 'Comfortable'
        when temperature < 29 then 'Warm'
        when temperature < 35 then 'Hot'
        else 'Sweltering'
    end as temp_categorized,
    case
        when precip_prob <= 20 then 'None'
        when precip_prob <= 40 then 'Low'
        when precip_prob <= 60 then 'Moderate'
        when precip_prob <= 80 then 'High'
        else 'Imminent'
    end as precip_prob_categorized,
    coalesce(valid_to, '9999-12-31 23:59:59'::timestamp) as valid_to,
    case
        when valid_to is null then 1
        else 0
    end as is_current
from {{ ref('stg_weather_readings') }}
