import os

class Environment():
	def __init__(self,logger):
		self.logger = logger
		self.missing_vars = list()
		self.retrieve_env_variables()

	class MissingEnvironmentVariable(Exception):
		def __init__(self, env_names):
			message = f"EMPTY ENVIRONMENT VARIABLES \"{env_names}\". PLEASE CHECK YOUR .env FILE."
			super().__init__(message)

	def load_env(self, env_name):
		self.logger.debug(F"TRYING TO RETRIEVE ENV VARIABLE: {env_name.upper()}...")
		env_variable = os.environ.get(env_name)
		if env_variable in ["", None]:
			self.missing_vars.append(env_name.upper())
		self.logger.info(F"SUCCESSFULLY RETRIEVED ENV VARIABLE: {env_name.upper()}...")
		return env_variable

	def retrieve_env_variables(self):
		self.POSTGRES_DB = self.load_env('POSTGRES_DB')
		self.POSTGRES_USER = self.load_env('POSTGRES_USER')
		self.POSTGRES_PASSWORD = self.load_env('POSTGRES_PASSWORD')
		self.API_TOKEN = self.load_env('API_TOKEN')
		self.API_URL = self.load_env('API_URL')
		
		if self.missing_vars != []:
			raise self.MissingEnvironmentVariable(self.missing_vars)