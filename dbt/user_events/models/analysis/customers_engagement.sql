{{ config(materialized='table') }}

with source_data as (

    SELECT
		TO_CHAR("date", 'yyyy-ww') AS week_of_year,
		COUNT(DISTINCT "user_id") AS active_users
	FROM
		{{ ref('user_events_view') }}
	GROUP BY
		week_of_year

)

select *
from source_data