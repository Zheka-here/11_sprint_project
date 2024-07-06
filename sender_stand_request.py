import configuration
import requests

def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))

