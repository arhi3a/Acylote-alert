import json
from playsound import playsound
from time import sleep

def data():
    from urllib.request import urlopen
    with urlopen('http://content.warframe.com/dynamic/worldState.php') as url:
        http_info = url.info()
        raw_data = url.read().decode(http_info.get_content_charset())
    return raw_data


raw_data = data()


def check(raw_data):
    t = json.loads(raw_data)
    t2 = (dict(t['PersistentEnemies'][0]))
    msg = t2['Discovered']
    print('Acylote found in: ', t2['LastDiscoveredLocation'])
    try:
        while msg == True:
            playsound('alert_sound.wav'), input('Press any key to stop')
    except KeyboardInterrupt:
        pass


def start():
    data()
    check(raw_data)
    sleep(60)
    start()

start()
