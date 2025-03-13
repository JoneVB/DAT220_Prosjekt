import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "local_secret_key"  # Change this for security
    DATABASE_PATH = os.path.join(BASE_DIR, 'instance', 'database.db')
