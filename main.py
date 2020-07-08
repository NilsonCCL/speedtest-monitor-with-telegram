import io
import json
import telepot
import speedtest
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

with open('secrets.json', 'r') as f:
    secrets = json.load(f)

BOT = telepot.Bot(secrets['BOT'])
CHAT = secrets['CHAT']


class Grafico():
    def __init__(self, download, upload, download_expected, upload_expected, ping):
        self.download = download
        self.upload = upload
        self.download_expected = download_expected
        self.upload_expected = upload_expected
        self.ping = ping

    def plotar(self):
        plt.figure()
        plt.plot(self.download, '-o', color='blue', label='Download Speed')
        plt.plot(self.upload, '-o', color='brown', label='Upload Speed')
        plt.plot(self.download_expected, color='green', label='Download Speed Expected')
        plt.plot(self.upload_expected, color='orange', label='Upload Speed Expected')
        plt.plot(self.ping, color='purple', label='Ping')
        plt.title('Velocidade de Conexão Atual VS. Velocidade de Conexão Esperada', )
        plt.ylabel('Mbps')
        plt.xlabel('www.nilson.com.br')
        plt.legend()
        plt.yticks(np.arange(0, 160, step=10))
        plt.grid(True)
        plt.xticks(color='w')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        BOT.sendPhoto(CHAT, buf)
        buf.close()
        plt.close('all')


while True:
    down_list = []
    up_list = []
    down_expected_list = []
    up_expected_list = []
    ping_list = []

    for _ in range(48):
        s = speedtest.Speedtest()
        s.download()
        s.upload()
        results_dict = s.results.dict()

        down_list.append(round(results_dict["download"] * 9.53674E-7, 2))
        up_list.append(round(results_dict["upload"] * 9.53674E-7, 2))
        down_expected_list.append(100)
        up_expected_list.append(50)
        ping_list.append(int(results_dict["ping"]))

        Grafico(down_list, up_list, down_expected_list, up_expected_list, ping_list).plotar()
        sleep(60)
