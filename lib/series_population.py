#!/usr/bin/env python
# coding: utf-8

import getting_data as gd
import pandas as pd 
import country_iso_series as iso

def get_population():
    url_grl ="http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&page="

    list_total_population = []
    pages = gd.obtain_pages(url_grl)
    indicators_numbers = gd.obtain_num_indicators(url_grl)

    for page in range(pages[-2]):
        for i_num in indicators_numbers:
            dics_data = gd.obtain_data()[page][1]
            list_total_population.append(dics_data[i_num]['value'])

    return pd.Series(list_total_population, index = iso.get_country_iso())