{{
	config(
		materialized='table',
		unique_key='time'
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
    valid_to
from {{ source('staging', 'raw_data') }}
