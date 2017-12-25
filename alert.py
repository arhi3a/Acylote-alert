import json
import time
import requests
import tweepy

names = {"/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent": 'Malice',
         "/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent": 'Angst',
         "/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent": 'Torment',
         "/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent": 'Violence',
         "/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent": 'Mania',
         }

dts = {"/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent": 0,
       "/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent": 0,
       "/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent": 0,
       "/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent": 0,
       "/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent": 0,
       }

nods = {'/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent': '',
        }

region = {'/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent': '',
          '/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent': '',
          '/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent': '',
          '/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent': '',
          '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent': '',
          }

hp = {'/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent': '',
      '/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent': '',
      '/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent': '',
      '/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent': '',
      '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent': '',
      }

rank = {'/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent': '',
        '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent': '',
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
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'])
        dts[name] += 1
        nods[name] = t2['LastDiscoveredLocation']
        region[name] = str(t2['Region'])
        hp[name] = str(t2['HealthPercent'] * 100)
        rank[name] = str(t2['Rank'])
    else:
        dts[name] -= dts[name]
        nods[name] = ''
        region[name] = ''
        hp[name] = ''
        rank[name] = ''


def check2(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][1]))
    msg = t2['Discovered']
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'])
        dts[name] += 1
        nods[name] = t2['LastDiscoveredLocation']
        region[name] = str(t2['Region'])
        hp[name] = str(t2['HealthPercent'] * 100)
        rank[name] = str(t2['Rank'])
    else:
        dts[name] -= dts[name]
        nods[name] = ''
        region[name] = ''
        hp[name] = ''


def check3(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][2]))
    msg = t2['Discovered']
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'])
        dts[name] += 1
        nods[name] = t2['LastDiscoveredLocation']
        region[name] = str(t2['Region'])
        hp[name] = str(t2['HealthPercent'] * 100)
        rank[name] = str(t2['Rank'])
    else:
        dts[name] -= dts[name]
        nods[name] = ''
        region[name] = ''
        hp[name] = ''


def check4(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][3]))
    msg = t2['Discovered']
    name = (t2['AgentType'])
    if msg:
        print(names[name], ' found in: ', t2['LastDiscoveredLocation'])
        dts[name] += 1
        nods[name] = t2['LastDiscoveredLocation']
        region[name] = str(t2['Region'])
        hp[name] = str(t2['HealthPercent'] * 100)
        rank[name] = str(t2['Rank'])
    else:
        dts[name] -= dts[name]
        nods[name] = ''
        region[name] = ''
        hp[name] = ''


def checker():
    answ = ''
    if dts['/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent'] == 1:
        answ += 'Malice Found' + ' ' + nods[
            '/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent'] + ' ' + \
                region[
                    '/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent'] + ' ' + \
                hp['/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent'] + ' ' + \
                rank[
                    '/Lotus/Types/Enemies/Acolytes/HeavyAcolyteAgent'] + ' ' + '(' + time.ctime() + ')' + ' ' + '\n'
    if dts['/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent'] == 1:
        answ += 'Angst Found' + ' ' + nods[
            '/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent'] + ' ' + \
                region['/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent'] \
                + ' ' + hp[
                    '/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent'] + ' ' + \
                rank[
                    '/Lotus/Types/Enemies/Acolytes/StrikerAcolyteAgent'] + ' ' + '(' + time.ctime() + ')' + ' ' + '\n'
    if dts['/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent'] == 1:
        answ += 'Torment Found' + ' ' + nods[
            '/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent'] + ' ' + \
                region['/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent'] \
                + ' ' + hp[
                    '/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent'] + ' ' + \
                rank[
                    '/Lotus/Types/Enemies/Acolytes/ControlAcolyteAgent'] + ' ' + '(' + time.ctime() + ')' + ' ' + '\n'
    if dts['/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent'] == 1:
        answ += 'Violence Found' + ' ' + nods[
            '/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent'] + ' ' + \
                region['/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent' \
                       ''] + ' ' + hp[
                    '/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent'] + \
                ' ' + rank[
                    '/Lotus/Types/Enemies/Acolytes/DuellistAcolyteAgent'] + \
                ' ' + '(' + time.ctime() + ')' + ' ' + '\n'
    if dts['/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent'] == 1:
        answ += 'Mania Found' + ' ' + nods[
            '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent'] + ' ' + \
                region[
                    '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent'] + ' ' + \
                hp[
                    '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent'] + \
                ' ' + rank[
                    '/Lotus/Types/Enemies/Acolytes/RogueAcolyteAgent'] + \
                ' ' + '(' + time.ctime() + ')' + ' ' + '\n'
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


def db():
    answ = checker()
    with open('data.txt', 'a') as f:
        f.write(answ)


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
    db()
    # main()  # Delete this to remove twitter notification
    time.sleep(60)
    start()


start()

### Tiwtter guide: http://nodotcom.org/python-twitter-tutorial.html
### World stats: http://content.warframe.com/dynamic/worldState.php
# Data.txt format: Name cnt Nod region hp rank time (Day(week):month:day:hour(
# GMT0):year)
