#!/usr/bin/env python
# coding: utf-8

import requests

def obtain_pages(main_url):
    json_data = requests.get(main_url+'1').json()
    pages = range(1, json_data[0]['pages']+1)
    return pages

def obtain_num_indicators(main_url):
    json_data = requests.get(main_url+'1').json()
    indicators_numbers = range(json_data[0]['per_page'])
    return indicators_numbers

def obtain_data():
    url_grl ="http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&page="
    pages = obtain_pages(url_grl)

    urls = []
    all_pages_data = []

    for page in pages:
        urls.append(url_grl+str(page))

    for url in urls:
        all_pages_data.append(requests.get(url).json())

    return all_pages_data

print(obtain_data())
