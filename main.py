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
    plt.plot(download_expected, color='green', label='Download Speed Esperado')
    plt.plot(upload_expected, color='orange', label='Upload Speed Esperado')
    plt.plot(download, '-o', color='blue', label='Current Download')
    plt.plot(upload, '-o', color='brown', label='Current Upload Speed')
    plt.plot(ping, color='purple', label='Ping')
    plt.title('Current Connection Speed VS. Connection Speed Expected \nthe tests runs every 5 minutes')
    plt.ylabel('Mbps')
    plt.xlabel('github.com/NilsonCCL/speedtest-graph')
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
    caption = 'github.com/NilsonCCL/speedtest-graph \n#Python #RaspberryPi #SpeedTest #Matplotlib'
    twitter.update_with_media('graph.png', caption)


while True:
    down_expected_list = []
    up_expected_list = []
    down_list = []
    up_list = []
    ping_list = []

    for _ in range(45):
        results_dict = make_speedtest()
        down_expected_list.append(100)
        up_expected_list.append(50)
        down_list.append(round(results_dict["download"] * 9.53674E-7, 2))
        up_list.append(round(results_dict["upload"] * 9.53674E-7, 2))
        ping_list.append(int(results_dict["ping"]))

        sleep(300)

    graph(down_list, up_list, down_expected_list, up_expected_list, ping_list)
