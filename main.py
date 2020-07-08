import io
import json
import telepot
import subprocess
import numpy as np
from PIL import Image
from time import sleep
import matplotlib.pyplot as plt

with open('secrets.json', 'r') as f:
    secrets = json.load(f)

BOT = telepot.Bot(secrets['BOT'])
CHAT = secrets['CHAT']


class Grafico():
    def __init__(self, download, upload, download_expected, upload_expected):
        self.download = download
        self.upload = upload
        self.download_expected = download_expected
        self.upload_expected = upload_expected

    def plotar(self):
        plt.figure()
        plt.plot(self.download, '-o', color='blue', label='Download Speed')
        plt.plot(self.upload, '-o', color='brown', label='Upload Speed')
        plt.plot(self.download_expected, color='green', label='Download Speed Expected')
        plt.plot(self.upload_expected, color='orange', label='Upload Speed Expected')
        plt.title('Actual Download Speed VS. Expected Download Speed', )
        plt.ylabel('Mbps')
        plt.xlabel('''4 Hours Of Results
                      Test Runs Every 5 Minutes''')
        plt.legend()
        axes = plt.gca()
        plt.yticks(np.arange(0, 150, step=10))
        plt.grid(True)
        plt.xticks(color='w')
        plt.show()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        im = Image.open(buf)
        im.save('teste.png')
        BOT.sendPhoto(CHAT, open('teste.png', 'rb'))
        buf.close()


down_lista = []
up_lista = []
download_expected = []
upload_expected = []

null = None

for _ in range(48):
    j = json.loads(subprocess.check_output(['speedtest-cli', '--json']))

    down_lista.append(round(j["download"] * 9.53674E-7, 2))
    up_lista.append(round(j["upload"] * 9.53674E-7, 2))
    download_expected.append(100)
    upload_expected.append(50)

    if len(down_lista) > 48:
        down_lista.pop(0)
        up_lista.pop(0)
        download_expected.pop(0)
        upload_expected.pop(0)

    Grafico(down_lista, up_lista, download_expected, upload_expected).plotar()

    sleep(300)
