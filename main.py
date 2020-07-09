import io
import json
import tweepy
import telepot
import speedtest
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

with open('secrets.json', 'r') as f:
    secrets = json.load(f)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])
twitter = tweepy.API(auth)

BOT = telepot.Bot(secrets['BOT'])
CHAT = secrets['CHAT']


def graph(download_expected, upload_expected, download, upload, ping):
    plt.figure()
    plt.plot(download_expected, color='green', label='Download Speed Esperado')
    plt.plot(upload_expected, color='orange', label='Upload Speed Esperado')
    plt.plot(download, '-o', color='blue', label='Download Speed Atual')
    plt.plot(upload, '-o', color='brown', label='Upload Speed Atual')
    plt.plot(ping, color='purple', label='Ping')
    plt.title('Velocidade de Conexão Atual VS. Velocidade de Conexão Esperada \no teste roda a cada 5 minutos')
    plt.ylabel('Mbps')
    plt.xlabel('www.nilson.com.br')
    plt.legend()
    plt.yticks(np.arange(0, 160, step=10))
    plt.grid(True)
    plt.xticks(color='w')
    buf = io.BytesIO()
    plt.savefig('graph.png', format='png')
    plt.savefig(buf, format='png')
    buf.seek(0)
    send_image_to_telegram(buf)
    send_imagem_to_twitter()
    buf.close()
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


def send_image_to_telegram(buf):
    BOT.sendPhoto(CHAT, buf)


while True:
    down_expected_list = []
    up_expected_list = []
    down_list = []
    up_list = []
    ping_list = []

    for _ in range(1):
        results_dict = make_speedtest()
        down_expected_list.append(100)
        up_expected_list.append(50)
        down_list.append(round(results_dict["download"] * 9.53674E-7, 2))
        up_list.append(round(results_dict["upload"] * 9.53674E-7, 2))
        ping_list.append(int(results_dict["ping"]))

        sleep(1)

    graph(down_list, up_list, down_expected_list, up_expected_list, ping_list)
