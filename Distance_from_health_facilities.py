import warnings
warnings.filterwarnings('ignore')
import geopandas as gpd
from s2 import s2
from shapely.wkt import loads
from geopy.distance import geodesic
from pandarallel import pandarallel
import numpy as np

n_0 = 0
n_f = 316545

print('Importing files...')

health = gpd.read_file('health_facilities_locations.csv', GEOM_POSSIBLE_NAMES="geometry",
                            KEEP_GEOM_COLUMNS="NO")

census_tract = gpd.read_file('census_tract_2010.csv', GEOM_POSSIBLE_NAMES="geometry",
                            KEEP_GEOM_COLUMNS="NO")

pandarallel.initialize()
def latlon(p):
    return (p.x, p.y)

def distance(p1, p2):  
    return geodesic(latlon(p1), latlon(p2)).kilometers

def distance_from_points(p1, p2s):
    return min((distance(p1, p2) for p2 in p2s.tolist()))

print(f'Truncating data from {n_0} to {n_f-1}')

test = census_tract.iloc[n_0:n_f]

print('Calculating distances...')

test['minimum_dist'] = test['geometry'].centroid.parallel_apply(lambda x: distance_from_points(x, health['geometry']))

test.to_csv(f'Brasil_distances_from_health_facilities_resolution_census_tract_{n_0}_to_{n_f-1}.csv')

print('\n')
print('Done! File saved')
