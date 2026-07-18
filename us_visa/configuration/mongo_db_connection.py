import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging


import os 
from us_visa.constants import  MONGODB_URL_KEY, DATABASE_NAME
import pymongo
import certifi

ca = certifi.where()

class MongoDBClieent:

    client = None

    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClieent.clinet is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Enviroment key: {mongo_db_url} is not set.")
                MongoDBClieent.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
            self.client = MongoDBClieent.clinet
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection is successfull")
        except Exception as e:
            raise USvisaException(e,sys)



