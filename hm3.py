from pprint import pprint

import requests

import time

import datetime

class Request:

    # request = Request()

    def method(self):
        stop = 0
        while stop == 0:
            url = "https://api.stackexchange.com/2.3/questions"
            headers = {'Accept': 'application/json'}
            now = int(time.time())
            period = now - (2 * 86400)
            page_number = 1
            params = {"page": page_number, "pagesize": "100", "fromdate": period, "order": "desc", "sort": "creation",
                  "tagged": "Python", "site": "stackoverflow"}
            resp = requests.get(url, params=params, headers=headers)
            a = resp.json()
            list_of_queries = a["items"]
            for n in range(len(list_of_queries)):
                unix_time = list_of_queries[n]['creation_date']
                print(datetime.datetime.fromtimestamp(unix_time))
                print(list_of_queries[n]['title'])
                print()
            page_number +=1
            if a["has_more"] == False: stop = 1
        return
request = Request()
request.method()