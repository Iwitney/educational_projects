import pandas as pd
from datetime import timedelta
from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.python import get_current_context

data = '/var/lib/airflow/airflow.git/dags/a.batalov/vgsales.csv'

default_args = {
    'owner': 'k-tajgind-18',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2022, 4, 2),
    'schedule_interval': '0 12 * * *'
}

@dag(default_args=default_args, catchup=False)
def ktay_airflow():
    @task(retries=3)
    def get_data():
        df = pd.read_csv(data)
        year = 1994 + hash(f'k-tajgind-18') % 23
        df = df.query('Year==@year')
        return df

    @task(retries=4, retry_delay=timedelta(10))
    def top_world_sales(df):
        top_world_sales = df.groupby('Name', as_index=False)\
            .agg({'Global_Sales': 'sum'})\
            .sort_values('Global_Sales', ascending=False)\
            .head(1)['Name'].values[0]
        return top_world_sales

    @task()
    def top_genre_europe(df):
        top_genre_europe = df.groupby('Genre', as_index=False)\
            .agg({'EU_Sales': 'sum'})\
            .sort_values('EU_Sales', ascending=False)\
            .head(1)['Genre'].values[0]
        return top_genre_europe

    @task()
    def top_quantity_platform_NA(df):
        top_quantity_platform_NA = df.query('NA_Sales>1')\
            .groupby('Platform', as_index=False)\
            .agg({'Name': 'count'})\
            .sort_values('Name', ascending=False)\
            .head(1)['Platform'].values[0]
        return top_quantity_platform_NA

    @task()
    def top_Jp_publisher(df):
        top_Jp_publisher = df.groupby('Publisher', as_index=False)\
            .agg({'JP_Sales': 'mean'})\
            .sort_values('JP_Sales', ascending=False)\
            .head(1)['Publisher'].values[0]
        return top_Jp_publisher

    @task()
    def count_games_Eu_better_Jp(df):
        count_games_Eu_better_Jp = df.groupby('Name', as_index=False)\
            .agg({'EU_Sales': 'sum', 'JP_Sales': 'sum'})\
            .query('EU_Sales>JP_Sales')\
            .shape[0]
        return count_games_Eu_better_Jp

    @task()
    def print_data(tws, tge, tqpna, tjp, cgebj):

        context = get_current_context()
        date = context['ds']
        year = 1994 + hash(f'k-tajgind-18') % 23

        print(f'''Анализ проведен {date}''')
        print(f'''Самая продаваемая игра в {year} году во всем мире: {tws}.''')
        print(f'''Игры {tge} жанра были самыми продаваемыми в Европе в {year} году.''')
        print(f'''На {tqpna} платформе было больше всего игр, \
            которые продались более чем миллионным тиражом в Северной Америке в {year} году.''')
        print(f'''У издателя {tjp} самые высокие средние продажи в Японии в {year} году.''')
        print(f'''{cgebj} игр продались лучше в Европе, чем в Японии в {year} году.''')

    df = get_data()
    tws = top_world_sales(df)
    tge = top_genre_europe(df)
    tqpna = top_quantity_platform_NA(df)
    tjp = top_Jp_publisher(df)
    cgebj = count_games_Eu_better_Jp(df)

    print_data(tws, tge, tqpna, tjp, cgebj)

ktay_airflow = ktay_airflow()