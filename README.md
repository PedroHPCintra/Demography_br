# Demography_br :brazil:

This repository is dedicated to demographic analysis of brazilian data. Last update: 2022-10-04

## Prerequisites

Make sure to have the following libraries installed before running any code:

- ```geopandas``` [https://geopandas.org/en/stable/](https://geopandas.org/en/stable/)
- ```geopy``` [https://github.com/geopy/geopy](https://github.com/geopy/geopy)
- ```pandarallel``` [https://github.com/nalepae/pandarallel](https://github.com/nalepae/pandarallel)
- ```s2``` [https://pypi.org/project/s2/](https://pypi.org/project/s2/)
- ```shapely``` [https://github.com/shapely/shapely](https://github.com/shapely/shapely)

## Content

This repository contains three files for now.

The Python code for calculating the distance from all census tracts to the closest hospital of each one of them: **Distance_from_health_facilities.py**

A csv file containing the number of households in each census tract according to the [2010 Census](https://www.ibge.gov.br/estatisticas/sociais/populacao/9662-censo-demografico-2010.html?edicao=10410&t=resultados): **Domicilios_particulares_e_coletivos_por_setor_censitario_2010.csv**.

| index | region code | number of colective and private households |
|:--:|:--:|:--:|
| 0 | 160005505000001 | 513 |
| 1 | 160005505000003 | 220 |

Make sure to check the documentation of the [2010 Census](https://www.ibge.gov.br/estatisticas/sociais/populacao/9662-censo-demografico-2010.html?edicao=10410&t=resultados) to see the definition of a colective and private household.

A folder **Data_distances** contains another 9 csv files (compressed as .zip) with the results of running **Distance_from_health_facilities.py**, it has the distances from each census tract to the nearest hospital. They are named according to the first and last indexes for census tracts that are included, for example the part1 and part2 are named **Census_tract_Brasil_distances_from_health_facilities_part1_0_to_34999.zip**, **Census_tract_Brasil_distances_from_health_facilities_part2_35000_to_69999.zip** because the first goes from index 0 to 34999, the second goes from index 35000 to 69999, and so on. Once you combine all nine files in one you have the full csv of size 316454 of distances from health facilities to census tracts.

| index | region code | zone type | code municipality | code state | minimum_dist | geometry |
|:-----:|:-----------:|:---------:|:-----------------:|:----------:|:------------:|:--------:|
| 0 | 110009812000003 | RURAL | 1100098.0 | 11 | 1.7195346365794169 | MULTIPOLYGON (((-60.8957500655381... |
| 1 | 110009815000001 | URBANO | 1100098.0 | 11 | 0.198243016483891 | MULTIPOLYGON (((-60.74999357721507... |
