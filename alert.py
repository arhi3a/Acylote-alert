import json
import time
import requests

names = {"/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent": 'Malice',
         "/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent": 'Angst',
         "/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent": 'Torment',
         }
timestp = ((time.localtime()[1], 'Month',
            time.localtime()[2], 'Day', time.localtime()[3], 'Hours',
            time.localtime()[4], 'Minutes'))

cla = []
cnt1 = []
cnt2 = []

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
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'],
              timestp)
        cla.append(1)
    else:
        cla.clear()

def check2(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][1]))
    msg = t2['Discovered']
    print(msg)
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'],
              timestp)
        cnt1.append(1)
    else:
        cnt1.clear()


def check3(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][2]))
    msg = t2['Discovered']
    print(msg)
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'],
              timestp)
        cnt2.append(1)
    else:
        cnt2.clear()

def checker():
    if len(cla) == 1:
        print('Tweet 1')
    if len(cnt1) == 1:
        print('Tweet 2')
    if len(cnt2) == 1:
        print('Tweet 3')

def start():
    print('Checking')
    data()
    time.sleep(3)
    raw_data = data()
    check(raw_data)
    time.sleep(1)
    check2(raw_data)
    time.sleep(1)
    check3(raw_data)
    time.sleep(1)
    print(cla, cnt1, cnt2)
    checker()
    time.sleep(60)
    start()


start()
