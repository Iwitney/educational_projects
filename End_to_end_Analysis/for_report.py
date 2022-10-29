# pip install gspread
# pip install psycopg2
import gspread as gspread
import psycopg2 as psycopg2
import pandas as pd
import psycopg2
import pandas.io.sql as sqlio
from sqlalchemy import create_engine
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials


class Postgres:
    def __init__(self,
                 user="postgres",
                 password="LM*25k10",
                 host="localhost",
                 port="5432",
                 database="postgres_db"):
        self.user = user
        self.pas = password
        self.host = host
        self.port = port
        self.db = database
        self.conn = psycopg2.connect(user=user,
                                     password=password,
                                     host=host,
                                     port=port,
                                     database=database)

    def get_df(self, sql):
        df = sqlio.read_sql_query(sql, self.conn)
        self.conn.close()
        return df

    def export_df(self, sql, df, table_name):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        self.conn.close()

        engine = create_engine(f'postgresql://{self.user}:{self.pas}@{self.host}:{self.port}/{self.db}')
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
        return print('Success!')


class GoogleSpreadsheet:
    def __init__(self,
                 my_mail='taygind@gmail.com',
                 json_keyfile='k-test-333621-e6507eb445df.json',
                 table_name='Report',
                 sheet='Sheet1'):
        self.mail = my_mail
        self.js_key = json_keyfile
        self.t_name = table_name
        self.sheet = sheet

    def export(self, df):
        # Authorization
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.js_key)
        gs = gspread.authorize(credentials)
        # Create empty table
        sheet = gs.create(self.t_name)
        sheet.share(self.mail, perm_type='user', role='writer')
        # Export report
        work_sheet = gs.open(self.t_name)
        table_id = work_sheet.id
        d2g.upload(df, table_id, self.sheet, credentials=credentials, row_names=True)

        return print('Success!')
