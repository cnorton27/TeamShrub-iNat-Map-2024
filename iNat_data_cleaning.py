import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import json
import csv2geojson  #imports functions from csv2geojson.py

csv = r"C:\Users\ciara\OneDrive\Documents\GitHub\TeamShrub-iNat-Map-2024\iNatObservations.csv"
output = "iNat_2024.geojson"
#csv2geojson.csv2geo(csv, output)

# add more processing steps here ...