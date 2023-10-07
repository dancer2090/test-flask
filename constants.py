from dotenv import load_dotenv
import os

load_dotenv()

# Environment variables
APP_PORT = os.environ.get('APP_PORT', '5000')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')
SECRET_KEY = os.environ.get('SECRET_KEY')

# Project constants
MIGRATION_DIR = os.path.join('db', 'migrations')
