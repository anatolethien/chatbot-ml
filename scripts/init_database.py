import tomllib as toml
from sqlalchemy import create_engine
import pandas as pd

with open('config.toml', 'rb') as config_file:
    config = toml.load(config_file)

POSTGRES_DB = config.get('POSTGRES_DB')
POSTGRES_USER = config.get('POSTGRES_USER')
POSTGRES_PASSWORD = config.get('POSTGRES_PASSWORD')
SERVER = '127.0.0.1'
PORT = '5432'
CONNECTION_STRING = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{SERVER}:{PORT}/{POSTGRES_DB}'

db = create_engine(CONNECTION_STRING)

print('Reading data from file...')
df = pd.read_csv(
    filepath_or_buffer='data/covid.csv'
)

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('-', '_')

print('Inserting data into database...')
df.to_sql(
    'covid',
    con=db,
    if_exists='replace',
    index=False
)

print(pd.read_sql_query('SELECT * FROM covid;', db))