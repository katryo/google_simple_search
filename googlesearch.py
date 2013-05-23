#! /usr/bin/python
# -*- coding:utf-8 -*-
from urllib import request
from urllib import parse
import http.client
import pdb
import json
import codecs


def simple_search(query):
    query = 'ninjaslayer'
    API_KEY = 'AIzaSyBdhBTUc5W5Aco3YGPwOlS_rYM0LBKl_jo'
    NUM = 1
    url = 'https://www.googleapis.com/customsearch/v1?'
    params = {'key': API_KEY,
              'q': query,
              'cx': '013036536707430787589:_pqjad5hr1a',
              'alt': 'json',
              'lr': 'lang_en',
              }
    start = 1
    results = []

    for i in range(0, NUM):
        params['start'] = start
        request_url = url + parse.urlencode(params)
        response = request.urlopen(request_url)
        results.append(response)
#pdb.set_trace()
    original_json = results[0]
    obj = json.load(original_json)
    results = obj
    return results

simple_search('aa')
