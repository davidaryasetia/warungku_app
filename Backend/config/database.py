import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# load environtment variables
load_dotenv() 

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

print("Data env : ", DATABASE_HOST, " ,", DATABASE_PORT, " ,", DATABASE_NAME, " ,", DATABASE_USERNAME, " ,", DATABASE_PASSWORD)

database_url_connection = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(database_url_connection)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)