import pandas

filename = 'l_city_market_id.csv'

df = pandas.read_csv('../data/lookups/' + filename)

lookup = {}

for index, row in df.iterrows():
    lookup[int(row['Code'])] = row['Description']

f = open(filename.split('.')[0] + '.dict', 'w')
f.write(str(lookup))
f.close()
