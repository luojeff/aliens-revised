import pandas as pd
import ast
import sys

cml = ast.literal_eval(
    open('../data/lookups/l_city_market_id.dict', 'r').read()
)

all_flights = pd.DataFrame()

for i in range(1, 9):
    flights = pd.read_csv('../data/flights/fl_2013-0%d.csv' % i)
    flights = flights[
        pd.notnull(flights['ARR_TIME']) &
        pd.notnull(flights['DEP_TIME']) &
        pd.notnull(flights['FL_DATE']) &
        (flights['ORIGIN_CITY_MARKET_ID'].isin(cml.keys())) &
        (flights['DEST_CITY_MARKET_ID'].isin(cml.keys()))
    ]
    flights['o_lat'] = flights['ORIGIN_CITY_MARKET_ID'].apply(lambda x: cml[x]['lat'])
    flights['o_lng'] = flights['ORIGIN_CITY_MARKET_ID'].apply(lambda x: cml[x]['lng'])
    flights['d_lat'] = flights['DEST_CITY_MARKET_ID'].apply(lambda x: cml[x]['lat'])
    flights['d_lng'] = flights['DEST_CITY_MARKET_ID'].apply(lambda x: cml[x]['lng'])

    all_flights = all_flights.append(flights, ignore_index=True)

all_flights.to_csv('all_flights.csv')


