import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

TABLE_NAME = "auto24"

#Danych połączenia SQL
db_host = "sql125.lh.pl"
db_user = "serwer274744_streamlit"
db_password = "bazabazA3#"
db_name = "serwer274744_streamlit"

# Utworzenie połączenia za pomocą SQLAlchemy
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", echo=True)
print(engine)

#READ SQL
# df = pd.read_sql_table('dane', engine, columns=['id', 'visit'])
df = pd.read_sql_query(
    f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    row_id INT PRIMARY KEY AUTO_INCREMENT,
    id VARCHAR(50),
    visit SMALLINT UNSIGNED,
    sold SMALLINT UNSIGNED,
    update DATE,
    data DATE)"""
    , engine)


#Send to database
def push(data_frame, table_name):
    data_frame.to_sql(
        name = table_name,
        con = engine,
        index = False,
        if_exists = 'append' #append,replace,fail
        )
push(df, TABLE_NAME)
