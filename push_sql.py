import pandas as pd
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime, Date, create_engine

TABLE_NAME = "auto24"

#Danych połączenia SQL
db_host = "sql125.lh.pl"
db_user = "serwer274744_streamlit"
db_password = "bazabazA3#"
db_name = "serwer274744_streamlit"

# Utworzenie połączenia za pomocą SQLAlchemy
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", echo=True)
metadata = MetaData()
print(engine)

#create table
table = Table(TABLE_NAME, metadata,
    Column('row_id', Integer, primary_key=True, autoincrement=True),
    Column('id', String(255)),
    Column('visit', Integer),
    Column('sold', Integer),
    Column('update', DateTime),
    Column('data', Date))
metadata.create_all(engine)


#Send to database
def push(data_frame, table_name):
    data_frame.to_sql(
        name = table_name,
        con = engine,
        index = False,
        if_exists = 'append' #append,replace,fail
        )
