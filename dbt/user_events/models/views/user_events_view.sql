{{ config(materialized='view') }}

with source_data as (

    SELECT
		"id"
		, "inserted_at_utc"
		, "amp_id"
		, "city"
		, "client_event_time"
		, "client_upload_time"
		, "country"
		, "data_type"
		, "date"
		, "device_id"
		, "event_time"
		, "event_type"
		, "group_first_event"
		, "group_ids"
		, "initial_li_fat_id"
		, "initial_rtd_cid"
		, "language"
		, "path"
		, "processed_time"
		, "region"
		, "server_received_time"
		, "server_upload_time"
		, "user_corporate_id"
		, "user_corporate_is_demo"
		, "user_corporate_status"
		, "user_id"
		, "user_properties_updated"
		, "user_role"
		, "user_signup_date"
		, "user_status"
	FROM
		user_events

)

select *
from source_data