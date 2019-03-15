import json
import random
from time import sleep

import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


disable_warnings(InsecureRequestWarning)
post_lager = "http://s-kv-center-v20:44330/api/Lager"
orders_url = 'http://s-kv-center-v20:44330/api/Orders'
get_orders = 'http://s-kv-center-v20:44330/api/Orders?' \
             'TicketToken=NThmOTVkN2IwODU1MjE3MzZiNzVmNzI5OGExYjZhOGU6eyJpZCI6MX0'
get_lager_url = "http://s-kv-center-v20:44330/api/Lager?filialId=2382"
headers = {'Content-Type': 'application/json-patch+json',
           'Accept': 'text/plain'}
add_lager_data = {
                "ticketToken": "NThmOTVkN2IwODU1MjE3MzZiNzVmNzI5OGExYjZhOGU6eyJpZCI6MX0",
                "filialId": 2382,
                "lager": {
                    "id": 1,
                    "count": 1
                }
            }

create_order_data = {
                      "customerPhone": "+380930768886",
                      "email": "mrsirling@gmail.com",
                      "ticketToken": "NThmOTVkN2IwODU1MjE3MzZiNzVmNzI5OGExYjZhOGU6eyJpZCI6MX0",
                      "filialId": 2382,
                      "readyDate": "2019-03-13T19:30:00+02:00",
                      "sendingSMS": True
                    }

change_order_status_data = {
                              "orderNumber": 1416,
                              "status": "2f916855-834b-47c0-bd26-c615a411dfdf",
                              "ticketToken": "NThmOTVkN2IwODU1MjE3MzZiNzVmNzI5OGExYjZhOGU6eyJpZCI6MX0"
                            }


def get_lager_id():
    r = requests.get(get_lager_url)
    item_id = list()
    response = r.json()
    for lager in response['lagers']:
        if lager['remnant'] > 0:
            for item in lager['items']:
                if item.get('count') >= 1:
                    item_id.append(item.get('id'))
    add_lager_data['lager']['id'] = int(random.choice(item_id))


def get_last_order(url):
    r = requests.get(url=url, verify=False)
    if r.status_code == 200:
        print("Order number: {}, status is: {}".format(r.json()[0]['number'], r.json()[0]['statusName']))
    else:
        print("Request failed. Error = {}".format(r.status_code))
        print(r.text)


def add_lager(url, payload):
    r = requests.post(url=url, data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        print("Post passed")
        print(r.text)
    else:
        print("Lager append failed. Error = {}".format(r.status_code))
        print(r.text)


def create_order(url, payload):
    r = requests.post(url, json.dumps(payload), headers=headers)
    if r.status_code == 200:
        print("All is good. Status = {}".format(r.status_code))
        print(r.text)
    else:
        print("Request failed. Error = {}".format(r.status_code))
        print(r.text)
    change_order_status_data['orderNumber'] = r.json()['order']['number']


def change_order_status(url, payload):
    r = requests.put(url, json.dumps(payload), headers=headers)
    if r.status_code == 200:
        print("All is good. Status = {}".format(r.status_code))
        print(r.text)
    else:
        print("Request failed. Error = {}".format(r.status_code))
        print(r.text)


get_lager_id()
add_lager(post_lager, add_lager_data)
sleep(5)
create_order(orders_url, create_order_data)
sleep(5)
get_last_order(get_orders)
change_order_status(orders_url, change_order_status_data)
get_last_order(get_orders)
