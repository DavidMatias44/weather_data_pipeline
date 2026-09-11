{% macro current_date_timezone() %}
    (current_timestamp at time zone '{{ var("default_timezone", "America/Denver") }}')::date
{% endmacro %}
