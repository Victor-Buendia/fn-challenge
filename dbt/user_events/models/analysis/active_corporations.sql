{{ config(materialized='table') }}

with source_data as (

    SELECT
		TO_CHAR("date", 'yyyy-ww') AS week_of_year,
		COUNT(DISTINCT "user_corporate_id") AS active_corporations
	FROM
		{{ ref('user_events_view') }}
	WHERE
		user_corporate_status = 'active'
	GROUP BY
		week_of_year

)

select *
from source_data