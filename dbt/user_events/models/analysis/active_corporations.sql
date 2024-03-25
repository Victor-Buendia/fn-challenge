{{ config(materialized='table') }}

with source_data as (

    SELECT
		CAST(TO_CHAR("date", 'yyyy') AS INT) AS "year",
		CAST(TO_CHAR("date", 'ww') AS INT) AS week_of_year,
		COUNT(DISTINCT "user_corporate_id") AS active_corporations
	FROM
		{{ ref('user_events_view') }}
	WHERE
		user_corporate_status = 'active'
		AND EXTRACT(YEAR FROM "date") = 2024
		AND EXTRACT(MONTH FROM "date") = 1
	GROUP BY
		"year",
		week_of_year
	ORDER BY
		"year",
		week_of_year
)

select *
from source_data