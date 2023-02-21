#!/usr/bin/env python
# coding: utf-8

import getting_data as gd
import pandas as pd 

def get_country_iso():
    url_grl ="http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&page="

    list_iso3 = []
    pages = gd.obtain_pages(url_grl)
    indicators_numbers = gd.obtain_num_indicators(url_grl)

    for page in range(pages[-2]):
        for i_num in indicators_numbers:
            dics_data = gd.obtain_data()[page][1]
            list_iso3.append(dics_data[i_num]['countryiso3code'])

    return list_iso3