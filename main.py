import io
import json
import telepot
import subprocess
from PIL import Image
from time import sleep
import matplotlib.pyplot as plt

with open('secrets.json', 'r') as f:
    secrets = json.load(f)

BOT = telepot.Bot(secrets['BOT'])
CHAT = secrets['CHAT']

class Grafico():
    def __init__(self, download, upload):
        self.download = download
        self.upload = upload

    def plotar(self):
        plt.figure()
        plt.plot(self.download, '-o', color='green', label='Download Speed')
        plt.plot(self.upload, '-o', color='blue', label='Upload Speed')
        plt.title('Actual Download Speed VS. Expected Download Speed', )
        plt.ylabel('Mbps')
        plt.xlabel('''4 Hours Of Results
                      Test Runs Every 5 Minutes''')
        plt.legend()
        axes = plt.gca()
        axes.set_ylim([0, 150])
        plt.grid(True)
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

null = None

for _ in range(4):
    j = json.loads(subprocess.check_output(['speedtest-cli', '--json']))

    down_lista.append(round(j["download"] * 9.53674E-7, 2))
    up_lista.append(round(j["upload"] * 9.53674E-7, 2))

    if len(down_lista) > 48:
        down_lista.pop(0)
        up_lista.pop(0)

    Grafico(down_lista, up_lista).plotar()

    sleep(60)
