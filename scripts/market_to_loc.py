import pandas as pd
import ast
import sys

cml = ast.literal_eval(
    open('../data/lookups/l_city_market_id.dict', 'r').read()
)

flights = pd.read_csv('../data/flights/fl_2013-01.csv')
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

print flights.head()


