# Demography_br :brazil:

This repository is dedicated to demographic analysis of brazilian data. Last update: 2022-10-03

## Prerequisites

Make sure to have the following libraries installed before running any code:

- ```geopandas``` [https://geopandas.org/en/stable/](https://geopandas.org/en/stable/)
- ```geopy``` [https://github.com/geopy/geopy](https://github.com/geopy/geopy)
- ```pandarallel``` [https://github.com/nalepae/pandarallel](https://github.com/nalepae/pandarallel)
- ```s2``` [https://pypi.org/project/s2/](https://pypi.org/project/s2/)
- ```shapely``` [https://github.com/shapely/shapely](https://github.com/shapely/shapely)

## Files

This repository contains two files for now.

The Python code for calculating the distance from all census tracts to the closest hospital of each one of them: **Distance_from_health_facilities.py**

A csv file containing the number of households in each census tract according to the [2010 Census](https://www.ibge.gov.br/estatisticas/sociais/populacao/9662-censo-demografico-2010.html?edicao=10410&t=resultados): **Domicilios_particulares_e_coletivos_por_setor_censitario_2010.csv**.

| index | region code | number of colective and private households |
|:--:|:--:|:--:|
| 0 | 160005505000001 | 513 |
| 1 | 160005505000003 | 220 |

Make sure to check the documentation of the [2010 Census](https://www.ibge.gov.br/estatisticas/sociais/populacao/9662-censo-demografico-2010.html?edicao=10410&t=resultados) to see the definition of a colective and private household.
