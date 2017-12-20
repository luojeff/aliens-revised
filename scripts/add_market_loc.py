import pandas as pd
import googlemaps
import sys

gcp_key =  open('gcp.key', 'r').read()

gmaps = googlemaps.Client(key=gcp_key)

filename = 'l_city_market_id.csv'

df = pd.read_csv('../data/lookups/' + filename)
df = df.sample(n=600)
lookup = {}

def get_lat_lng(s):
    geocode_result = gmaps.geocode(s)
    return geocode_result[0]['geometry']['location']
i = 0
for index, row in df.iterrows():
    try:
        print i
        lookup[int(row['Code'])] = get_lat_lng(row['Description'])
        i += 1
    except:
        continue

f = open('../data/lookups/' + filename.split('.')[0] + '.dict', 'w')
f.write(str(lookup))
f.close()
