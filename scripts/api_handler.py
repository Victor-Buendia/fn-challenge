import requests
import json
import os

from utils import get_str_dates
from validation.schemas import UserEvent as UserEventValidator
from models.user_event import UserEvent
from colors import COLORS

class ApiHandler():
	def __init__(self,logger,environment,postgres_connection):
		self.logger = logger
		self.env = environment
		self.postgres_conn = postgres_connection
		self.base_url = f"{self.env.API_URL}"
		os.makedirs('./data', exist_ok=True)

	def request_day(self, request_date: str) -> list[dict]:
		headers = {
			"api-token": self.env.API_TOKEN
		}
		url = f"{self.base_url}?date={request_date}"

		response = requests.request("GET", url, headers=headers)
		if response.status_code == 200:
			loaded_data = json.loads(response.text)
			self.logger.info(f"{len(loaded_data)} RECORDS RETRIEVED FOR DAY {request_date}")
			return loaded_data
		else:
			self.logger.info(f"NO DATA RETRIEVED FOR DAY {request_date}")
			return []

	def request_month(self, start_date: str, end_date: str) -> list[dict]:
		dates_to_fetch = get_str_dates(start=start_date, end=end_date)
		total_inserted_data_counter = 0

		for day in dates_to_fetch:
			inserted_data_counter = 0
			user_events_data = self.request_day(request_date=day)
			user_events_validated = [UserEventValidator.model_validate(user_event).dict() for user_event in user_events_data]
			if len(user_events_validated) > 0:
				for user_event in user_events_validated:
					inserted_data_counter += self.postgres_conn.insert_on_conflict(
						Table=UserEvent,
						pks=[UserEvent.event_time, UserEvent.device_id],
						data=user_event
					)
					if ((inserted_data_counter+total_inserted_data_counter) % 200) == 0:
						self.logger.info(f"{COLORS['GREEN']}{inserted_data_counter+total_inserted_data_counter} TOTAL RECORDS INGESTED ALREADY...{COLORS['WHITE']}\n")
				total_inserted_data_counter += inserted_data_counter
				self.logger.info(f"DATA FROM DAY [{COLORS['PURPLE']}{day}{COLORS['WHITE']}] INSERTED << {inserted_data_counter} >> RECORDS SUCCESSFULLY AT (${self.postgres_conn.get_address})")
	