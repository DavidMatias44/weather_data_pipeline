{{
	config(
		materialized='table',
		unique_key='time'
	)
}}

select
    time,
    latitude,
    longitude,
    elevation,
    temperature,
    precip_prob,
    updated_at
from {{ source('staging', 'raw_data') }}
