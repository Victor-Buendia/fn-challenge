import requests
import json
import os

from utils import get_str_dates

class ApiHandler():
	def __init__(self,logger,environment):
		self.logger = logger
		self.env = environment
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
		data_to_return = list()

		for day in dates_to_fetch:
			data = self.request_day(request_date=day)
			with open(f"./data/{day}.json",'w') as file:
				json.dump(data, fp=file, indent=2)
			if data != []:
				data_to_return.extend(data)
		return data_to_return
	