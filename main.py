import json
import tweepy
import speedtest
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

with open('secrets.json', 'r') as f:
    secrets = json.load(f)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])
twitter = tweepy.API(auth)


def graph(download_expected, upload_expected, download, upload, ping):
    plt.figure()
    plt.plot(download_expected, color='green', label='Expected Download Speed')
    plt.plot(upload_expected, color='orange', label='Expected Upload Speed')
    plt.plot(download, '-o', color='blue', markersize=3, label='Current Download Speed')
    plt.plot(upload, '-o', color='brown', markersize=3, label='Current Upload Speed')
    plt.plot(ping, color='purple', label='Ping in Milliseconds')
    plt.title('Current Connection Speed VS. Expected Connection Speed \nthe tests runs every 5 minutes')
    plt.ylabel('Mbps')
    plt.xlabel('github.com/nilson-santos/speedtest-graph')
    plt.legend()
    plt.yticks(np.arange(0, 160, step=10))
    plt.grid(True)
    plt.xticks(color='w')
    plt.savefig('graph.png', format='png')
    send_imagem_to_twitter()
    plt.close('all')


def make_speedtest():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    return s.results.dict()


def send_imagem_to_twitter():
    caption = 'github.com/nilson-santos/speedtest-graph \n#Python #RaspberryPi #SpeedTest #Matplotlib ' \
              '#opticalfiber #telecom'
    twitter.update_with_media('graph.png', caption)


while True:
    down_expected_list = []
    up_expected_list = []
    down_list = []
    up_list = []
    ping_list = []

    for _ in range(48):
        results_dict = make_speedtest()
        down_expected_list.append(100)
        up_expected_list.append(50)
        down_list.append(round(results_dict["download"] * 9.53674E-7, 2))
        up_list.append(round(results_dict["upload"] * 9.53674E-7, 2))
        ping_list.append(int(results_dict["ping"]))

        sleep(300)

    graph(down_expected_list, up_expected_list, down_list, up_list, ping_list)
