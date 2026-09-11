select precip_prob
from {{ ref('int_weather_enriched') }}
where precip_prob < 0 or precip_prob > 100
