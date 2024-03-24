import logging

from environment import Environment
from api_handler import ApiHandler
from postgres_connector import PostgresConnector

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
		self.postgres_conn = PostgresConnector(self.logger, self.environment)
		self.api = ApiHandler(self.logger, self.environment, self.postgres_conn)

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
		self.api.request_month('2024-01-01','2024-02-01')
		
if __name__ == "__main__":
	main = Main()
	main.start()