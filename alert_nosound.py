import json
from time import sleep
import requests


def data():
    from urllib.request import urlopen
    with urlopen('http://content.warframe.com/dynamic/worldState.php') as url:
        http_info = url.info()
        raw_data = url.read().decode(http_info.get_content_charset())
    return raw_data


def error():
    z = requests.get('http://content.warframe.com/dynamic/worldState.php')
    z = z.status_code
    if z != requests.codes.ok:
        print(z, 'Response error')
    else:
        print(z)


raw_data = data()


def check(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][0]))
    msg = t2['Discovered']
    print(msg)
    if msg:
        print('Acylote found in: ', t2['LastDiscoveredLocation'])


def check2(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][1]))
    msg = t2['Discovered']
    print(msg)
    if msg:
        print('Acylote found in: ', t2['LastDiscoveredLocation'])


def start():
    print('Checking')
    data()
    error()
    check(raw_data)
    check2(raw_data)
    sleep(60)
    start()


start()
