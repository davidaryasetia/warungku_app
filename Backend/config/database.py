import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# load environtment variables
load_dotenv() 

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

print("Data env : ", DB_HOST, " ,", DB_PORT, " ,", DB_NAME, " ,", DB_USERNAME, " ,", DB_PASSWORD)

database_url_connection = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(database_url_connection)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)