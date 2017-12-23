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

chck= []

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
        return chck.append(1)
    else:
        return chck.append(0)


def check2(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][1]))
    msg = t2['Discovered']
    print(msg)
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'],
              timestp)
        return chck.append(1)
    else:
        return chck.append(0)

def check3(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][2]))
    msg = t2['Discovered']
    print(msg)
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'],
              timestp)
        return chck.append(1)
    else:
        return chck.append(0)



def start():
    print('Checking')
    data()
    raw_data = data()
    time.sleep(3)
    check(raw_data)
    check2(raw_data)
    check3(raw_data)
    time.sleep(60)
    start()


start()
