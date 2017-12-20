import pandas as pd
import ast
import sys

cml = ast.literal_eval(
    open('../data/lookups/l_city_market_id.dict', 'r').read()
)

all_flights = pd.DataFrame()

offset = lambda t, id: (t - cml[id]['rawOffset']) % 86400

def hhmm_to_seconds(x):
    s = str(int(x))
    s = '0' * (4 - len(s)) + s
    return 60 * int(s[:2]) + int(s[2:])

for i in range(1, 9):
    flights = pd.read_csv('../data/flights/fl_2013-0%d.csv' % i)
    flights = flights[
        pd.notnull(flights['ARR_TIME']) &
        pd.notnull(flights['DEP_TIME']) &
        pd.notnull(flights['FL_DATE']) &
        (flights['ORIGIN_CITY_MARKET_ID'].isin(cml.keys())) &
        (flights['DEST_CITY_MARKET_ID'].isin(cml.keys()))
    ]
    flights['DEP_TIME'] = flights['DEP_TIME'].apply(hhmm_to_seconds)
    flights['ARR_TIME'] = flights['ARR_TIME'].apply(hhmm_to_seconds)
    flights['o_lat'] = flights['ORIGIN_CITY_MARKET_ID'].apply(lambda x: cml[x]['lat'])
    flights['o_lng'] = flights['ORIGIN_CITY_MARKET_ID'].apply(lambda x: cml[x]['lng'])
    flights['d_lat'] = flights['DEST_CITY_MARKET_ID'].apply(lambda x: cml[x]['lat'])
    flights['d_lng'] = flights['DEST_CITY_MARKET_ID'].apply(lambda x: cml[x]['lng'])
    flights['DEP_TIME'] = flights[['DEP_TIME', 'ORIGIN_CITY_MARKET_ID']].apply(lambda x: offset(*x), axis=1)
    flights['ARR_TIME'] = flights[['ARR_TIME', 'DEST_CITY_MARKET_ID']].apply(lambda x: offset(*x), axis=1)

    all_flights = all_flights.append(flights, ignore_index=True)

all_flights.to_csv('../data/flights/all_flights.csv')
