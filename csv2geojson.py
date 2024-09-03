import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import json

def csv2geo(input, output):
    """
    Takes a csv file and converts to gejson using long and lat column for point location
    """
    gdf = gpd.read_file(input)
    gdf = gpd.GeoDataFrame(
        gdf, geometry=gpd.points_from_xy(gdf.longitude, gdf.latitude), crs="EPSG:4326")
    gdf.to_file(output, driver='GeoJSON')
