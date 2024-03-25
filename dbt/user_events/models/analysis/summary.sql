{{ config(materialized='table') }}

with daily_users as (

    SELECT DISTINCT
		"date",
		"user_id",
		"user_corporate_id",
		COUNT("event_time") AS events_count
	FROM
		{{ ref('user_events_view') }}
	WHERE
		EXTRACT(YEAR FROM "date") = 2024
		AND EXTRACT(MONTH FROM "date") = 1
	GROUP BY
		"date",
		"user_id",
		"user_corporate_id"
),

summary as (
	SELECT
		CAST(TO_CHAR("date", 'yyyy') AS INT) AS "year",
		CAST(TO_CHAR("date", 'ww') AS INT) AS week_of_year,
		"user_id",
		"user_corporate_id",
		AVG(events_count) AS avg_events_count,
		MAX(events_count) AS max_events_count,
		MIN(events_count) AS min_events_count
	FROM
		daily_users
	GROUP BY
		"year",
		week_of_year,
		"user_id",
		"user_corporate_id"
	ORDER BY
		"year",
		week_of_year
)

select *
from summary