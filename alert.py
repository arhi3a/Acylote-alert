import json
import time
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



def check(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][0]))
    msg = t2['Discovered']
    print(msg)
    if msg:
        print('Angst found in: ', t2['LastDiscoveredLocation'])



def check2(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][1]))
    msg = t2['Discovered']
    print(msg)
    if msg:
        print('Malice found in: ', t2['LastDiscoveredLocation'])
    return raw_data, t, t2


def start():
    print('Checking')
    data()
    raw_data = data()
    time.sleep(3)
    check(raw_data)
    check2(raw_data)
    time.sleep(60)
    start()


start()
