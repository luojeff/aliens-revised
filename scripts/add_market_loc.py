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
    g = gmaps.geocode(s)[0]['geometry']['location']
    timezone = gmaps.timezone((g['lat'], g['lng']))
    g.update({
        'rawOffset': timezone['rawOffset'],
        'timeZoneName': timezone['timeZoneName']
    })
    return g
i = 0
for index, row in df.iterrows():
    try:
        lookup[int(row['Code'])] = get_lat_lng(row['Description'])
        print "%d / 600" % i
        i += 1
    except:
        i += 1
        continue

f = open('../data/lookups/' + filename.split('.')[0] + '.dict', 'w')
f.write(str(lookup))
f.close()
