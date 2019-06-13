from math import sin, cos, sqrt, atan2, radians
from craigslist import CraigslistHousing
import mpu
import csv
import argparse

# stole 90% of this from: 
# https://www.dataquest.io/blog/apartment-finding-slackbot/ 
# https://github.com/MarksCode/Craigslist-Apartment-Finder 



def writeCSV(apts):
    keys = apts[0].keys()
    with open('Apts.csv', 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(apts)



parser = argparse.ArgumentParser('python3 apartmentFinder.py')
parser.add_argument('CRAIGSLIST_SITE', help='site to search', type=str)
parser.add_argument('LIMIT', help='site to search', type=int, default=20)
parser.add_argument('CATEGORY', help='category to search (e.g. apa)', nargs='?', type=str, default='apa')
parser.add_argument('MAX_PRICE', help='max price', nargs='?', type=int, default=5000)
parser.add_argument('MIN_PRICE', help='min price', nargs='?', type=int, default=0)
parser.add_argument('CENTER_ONE_LAT', help='Lat and Long of where you work', nargs='?', type=float, default=-1)
parser.add_argument('CENTER_ONE_LONG', help='Lat and Long of where you work', nargs='?', type=float, default=-1)
parser.add_argument('CENTER_TWO_LAT', help='Lat and Long of center of city (or whatever)', nargs='?', type=float, default=-1)
parser.add_argument('CENTER_TWO_LONG', help='Lat and Long of center of city (or whatever)', nargs='?', type=float, default=-1)
args = parser.parse_args()

cl = CraigslistHousing(site=args.CRAIGSLIST_SITE, category=args.CATEGORY,
                                     filters={'max_price': args.MAX_PRICE, "min_price": args.MIN_PRICE})

CENTER_ONE = (args.CENTER_ONE_LAT, args.CENTER_ONE_LONG)
CENTER_TWO = (args.CENTER_TWO_LAT, args.CENTER_TWO_LONG)

results = cl.get_results(sort_by='newest', geotagged=True, limit=args.LIMIT)

apts = []

for result in results:
    apt = {
        "name" : result["name"],
        "price" : result["price"],
        "bedrooms" : result["bedrooms"],
        "where" : result["where"],
        "geotag" : result["geotag"],
        "url" : result["url"]
    }

    if (apt["geotag"]):
      if (CENTER_ONE[0] != -1):
          apt["center_one_distance"] = mpu.haversine_distance(result["geotag"], CENTER_ONE)

      if (CENTER_TWO[0] != -1):
          apt["center_two_distance"] = mpu.haversine_distance(result["geotag"], CENTER_TWO)

    apts.append(apt)
    
writeCSV(apts)
