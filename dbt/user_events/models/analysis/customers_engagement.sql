{{ config(materialized='table') }}

with source_data as (

    SELECT
		TO_CHAR("date", 'yyyy-ww') AS week_of_year,
		COUNT(DISTINCT "user_id") AS active_users
	FROM
		{{ ref('user_events_view') }}
	WHERE
		EXTRACT(YEAR FROM "date") = 2024
		AND EXTRACT(MONTH FROM "date") = 1
	GROUP BY
		week_of_year
	ORDER BY
		week_of_year
)

select *
from source_data