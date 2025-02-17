import geopandas as gpd
import numpy as np


# Read the GeoJSON file into a GeoDataFrame
gdf = gpd.read_file(r'C:\GitHub\TeamShrub-iNat-Map-2024\iNat_2024.geojson')


# counts species of given name
def species_count(species, data):
    count = 0
    for index, row in data.iterrows():
        if species == row['scientific_name']:
            count = count + 1
    print(count)
    return(count)
    
# adds count to new count column (righ tnow ID)
def add_count(species, data):
    for index, row in gdf.iterrows():
        if species == row['scientific_name']:
            gdf.loc[index, 'Count'] = species_count(species, data)
        #print("Count:", count)  # Output the count

def list_species(data):
    species_list = []
    for index, row in data.iterrows():
        if row['scientific_name'] in species_list:
            species_list = species_list
        else:
            species_list.append(row['scientific_name'])
    return species_list


def count_all(data):
    all_species = list_species(gdf)
    for i in all_species:
        add_count(i, data)


#species_count("Achillea_millefolium", gdf)
count_all(gdf)

gdf.to_file('iNat_2024.geojson', driver='GeoJSON')

