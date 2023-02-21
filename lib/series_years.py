#!/usr/bin/env python
# coding: utf-8

from . import getting_data as gd
import pandas as pd 
from . import series_countries as iso

def get_years():
    url_grl ="http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&page="

    list_years = []
    pages = gd.obtain_pages(url_grl)
    indicators_numbers = gd.obtain_num_indicators(url_grl)

    for page in range(pages[-2]):
        for i_num in indicators_numbers:
            dics_data = gd.obtain_data()[page][1]
            list_years.append(dics_data[i_num]['date'])

    return pd.Series(list_years, index = iso.get_country_iso())