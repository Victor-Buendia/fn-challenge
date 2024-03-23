from pymongo import MongoClient

class MongoConnector():
	def __init__(self, logger, environment):
		self.logger = logger
		self.env = environment

		self.connection_string = 'mongodb://nosql:27017/'
		self.connect()

		self.db = self.client['users']
		self.collection = self.db['user_events']

	def connect(self):
		self.logger.debug(f"ATTEMPTING TO CONNECT TO MONGODB AT {self.connection_string}")
		self.client = MongoClient(self.connection_string)
		self.logger.info(f"SUCCESSFULLY CONNECTED TO MONGODB AT {self.connection_string}")

	def insert_data(self, document):
		print(document['date'])
		existing_docs = self.retrieve_data(_filter={'date': document['date']})
		print(existing_docs)
		self.collection.insert_one(document)
		self.logger.debug(f"SUCCESSFULLY INSERTED DOCUMENT INTO MONGODB IN COLLECTION {self.collection}")

	def retrieve_data(self, _filter={}):
		return self.collection.find(_filter)