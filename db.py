import pymongo,os
from dotenv import load_dotenv

load_dotenv()
MONGODB = os.environ.get("MONGODB")

class Users:
    def __init__(self) -> None:
        pass

