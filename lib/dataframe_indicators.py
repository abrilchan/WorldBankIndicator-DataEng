#!/usr/bin/env python
# coding: utf-8

import getting_data as gd
import pandas as pd 
import country_iso_series as iso
import series_population as sp
import series_years as sy
import series_countries as sc

dict_data = {
    'Country' : pd.Series(sc.get_country_value()),
    'Year' : pd.Series(sy.get_years()),
    'Population' : pd.Series(sp.get_population())
}

def df_indicators():
    population_country_year_df = pd.DataFrame(dict_data)
    return population_country_year_df
