import json
import time
import requests
import tweepy

names = {"/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent": 'Malice',
         "/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent": 'Angst',
         "/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent": 'Torment',
         }

dts = {"/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent": 0,
       "/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent": 0,
       "/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent": 0,
       }


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
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'])
        dts[name] += 1
    else:
        dts[name] -= dts[name]


def check2(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][1]))
    msg = t2['Discovered']
    print(msg)
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'])
        dts[name] += 1
    else:
        dts[name] -= dts[name]


def check3(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][2]))
    msg = t2['Discovered']
    print(msg)
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'])
        dts[name] += 1
    else:
        dts[name] -= dts[name]


def checker():
    answ = ''
    if dts['/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent'] == 1:
        answ += ' Malice Found '
    if dts['/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent'] == 1:
        answ += ' Angst Found '
    if dts['/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent'] == 1:
        answ += ' Torment Found'
    return answ


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def main():
    if checker() != '':
        print('MSG SENT')
        # Fill in the values noted in previous step here
        cfg = {
            "consumer_key": "$",
            "consumer_secret": "$",
            "access_token": "$-$",
            "access_token_secret": "$",
        }

        api = get_api(cfg)
        tweet = "test!"
        status = api.update_status(status=checker())
        # Yes, tweet is called 'status' rather confusing
    else:
        pass


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
    print(dts)
    main()  # Delete this to remove twitter notification
    time.sleep(60)
    start()


start()

### Tiwtter guide: http://nodotcom.org/python-twitter-tutorial.html
### World stats: http://content.warframe.com/dynamic/worldState.php
