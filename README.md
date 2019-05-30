# Craigslist Apartment Finder : REDUX

Finds apartments on craiglist

Based on [this](https://github.com/MarksCode/Craigslist-Apartment-Finder)
and [this](https://www.dataquest.io/blog/apartment-finding-slackbot/)

## Dependencies

[Python Craigslist](https://pypi.org/project/python-craigslist/)

[MPU](https://pypi.org/project/mpu/)

## Use

```
usage: python3 apartmentFinder.py CRAIGSLIST_STIE LIMIT [CATEGORY] [MAX_PRICE] [MIN_PRICE] [CENTER_ONE_LAT] [CENTER_ONE_LONG] [CENTER_TWO_LAT] [CENTER_TWO_LONG] 

positional arguments:
  CRAIGSLIST_SITE  Craigslist site to search on (e.g. Columbus)
  LIMIT 	   Max number of apartments to return	
  CATEGORY         Category to search in (e.g. 'apa' for apartments)
  MAX_PRICE        Maximum tolerable price
  MIN_PRICE        Minimum tolerable price
  CENTER_ONE_LAT   Latitude of first location to be referenced for distance
  CENTER_ONE_LONG  Longitude of first location to be referenced for distance
  CENTER_TWO_LAT   Latitude of second location to be referenced for distance
  CENTER_TWO_LONG  Longitude of second location to be referenced for distance

```

### Example Command

`python3 apartmentFinder.py columbus 1000 apa 1500 500 40.140393 -82.99645 39.968066 -83.005278`	

Finds apartments in Columbus, limited to a thousand, with a max price of 500 and a min price of 1500, returning the distance from JPMorgan Chase in Polaris (40..., -82...) and the center of Columbus (39..., -83...)
