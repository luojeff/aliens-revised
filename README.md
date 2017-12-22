# aliens-revised

## Process
Using [flight data provided by the Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236), we were able to get records of every flight for the past few years. By left-joining this data on the `CityMarketID` attributes of every flight's origin and destination airport with BTS's city market ID lookup table, we found the city string for every airport of each flight. Using Google Maps API Geocoding, we could find the `lat`/`lng` for every flight's takeoff and destination. Using this data, we could isolate the timezone for the flight and adjust the timestamps on flights from BTW, which are initially given in local time.

## Required packages before running:
pandas
numpy
matplotlib
seaborn
plotly
IPython
sklearn

## Contributors
Jeffrey Luo<br>
Jason Kao<br>
Max Zlotskiy<br>
Khyber Sen
