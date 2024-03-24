import psycopg2
import logging
import json
import os

from environment import Environment
from api_handler import ApiHandler
from mongo_connector import MongoConnector
from postgres_connector import PostgresConnector
from validation.schemas import UserEvent as UserEventValidator
from models.user_event import UserEvent

from sqlalchemy.dialects.sqlite import insert
from psycopg2.extras import Json
psycopg2.extensions.register_adapter(dict, Json)

class Main():
	def __init__(self):
		# LOG CONFIG
		logging.basicConfig(
			format="[%(levelname)s] [%(asctime)s][%(filename)-15s][%(lineno)4d] : %(message)s",
			level=logging.INFO,
			force=True,
		)
		logging.getLogger("sqlalchemy").setLevel(logging.WARNING)
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.INFO)
		
		# OBJECTS
		self.environment = Environment(self.logger)
		self.api = ApiHandler(self.logger, self.environment)
		self.postgres_conn = PostgresConnector(self.logger, self.environment)
		# self.mongo_conn = MongoConnector(self.logger, self.environment)

	def json_insert(self):
		i = 0
		files = os.listdir('./data')
		for json_file in files:
			with open(f'./data/{json_file}','r') as file:
				user_events_data = json.load(file)
				if user_events_data != []:
					# Dates to update data into RDBMS
					dates_to_insert = {UserEventValidator.model_validate(user_event).dict()["date"] for user_event in user_events_data}
					# Flattening nested fields to insert into RDBMS
					user_events_validated = [UserEventValidator.model_validate(user_event).dict() for user_event in user_events_data]

					for user_event in user_events_validated:
						insert_stmt = insert(UserEvent).values(user_event)
						insert_stmt = insert_stmt.on_conflict_do_update(
							index_elements=[UserEvent.event_time, UserEvent.device_id],
							set_=dict(insert_stmt.excluded)
						)
						self.postgres_conn.execute_stmt(insert_stmt)
						i += 1
						if ((i % 200) == 0):
							self.logger.info(f"{json_file} >> {i} RECORDS IN TOTAL INSERTED INTO TABLE \"{UserEvent.__tablename__.upper()}\"...")
			# os.remove(f"./data/{json_file}")
		if ((i % 200) != 0):
			self.logger.info(f"{json_file} >> {i} RECORDS IN TOTAL INSERTED INTO TABLE \"{UserEvent.__tablename__.upper()}\"...")
	
	def start(self):
		print('Main program executed.')
		self.postgres_conn.connect(
			user=self.environment.POSTGRES_USER,
			pswd=self.environment.POSTGRES_PASSWORD,
			host='rdbms',
			port='5432',
			db=self.environment.POSTGRES_DB,
		)
		self.postgres_conn.create_tables()
		# self.api.request_month('2024-01-01','2024-02-01')
		self.json_insert()
		
if __name__ == "__main__":
	main = Main()
	main.start()