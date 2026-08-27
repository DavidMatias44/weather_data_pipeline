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
    case
        when temperature < -9 then 'Frigid'
        when temperature <  0 then 'Freezing'
        when temperature <  7 then 'Very cold'
        when temperature < 13 then 'Cold'
        when temperature < 18 then 'Cool'
        when temperature < 24 then 'Comfortable'
        when temperature < 29 then 'Warm'
        when temperature < 35 then 'Hot'
        else 'Sweltering'
    end as temp_categorized,
    precip_prob,
    case
        when precip_prob <= 20 then 'None'
        when precip_prob <= 40 then 'Low'
        when precip_prob <= 60 then 'Moderate'
        when precip_prob <= 80 then 'High'
        else 'Imminent'
    end as precip_prob_categorized
from {{ ref('stg_weather_readings') }}
where time::date = current_date
