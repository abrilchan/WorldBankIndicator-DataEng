#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
from lib import dataframe_indicators as dfi

def growth_percentage(country_iso):

    dataframe_indicators = df_indicators()

    prev_year_population = dataframe_indicators.loc[country_iso]['Population'].shift(1)
    media_population_per_year = (dataframe_indicators.loc[country_iso]['Population']+prev_year_population)/2

    grow_rate_year_percentage = ((dataframe_indicators.loc[country_iso]['Population'] - prev_year_population) / media_population_per_year)*100

    return grow_rate_year_percentage