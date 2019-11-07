import pathlib


BASE_DIR = pathlib.Path(__file__).parent.parent

# DB settings
POSTGRES_USER = 'api_user'
POSTGRES_PASSWORD = 'psg_pass'
POSTGRES_DB = 'shelter_api'
# POSTGRES_HOST = 'postgres'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
