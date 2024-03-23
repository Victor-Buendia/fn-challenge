{{ config(materialized='table') }}

with daily_users as (

    SELECT
		"date",
		COUNT("user_id") AS active_users,
		COUNT("user_corporate_id") AS active_corporations
	FROM
		{{ ref('user_events_view') }}
	GROUP BY
		date

),

summary as (
	SELECT
		TO_CHAR("date", 'yyyy-ww') AS week_of_year,
		AVG(active_users) AS avg_active_users,
		MAX(active_users) AS max_active_users,
		MIN(active_users) AS min_active_users,
		AVG(active_corporations) AS avg_active_corporations,
		MAX(active_corporations) AS max_active_corporations,
		MIN(active_corporations) AS min_active_corporations
	FROM
		daily_users
	GROUP BY
		week_of_year
)

select *
from summary