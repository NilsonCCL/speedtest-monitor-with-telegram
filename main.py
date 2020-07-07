import io
from PIL import Image
import matplotlib.pyplot as plt

import secrets

print(secrets.BOT)

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
        buf.close()


down_lista = []
up_lista = []

null = None
json = {"client": {"rating": "0",
                   "loggedin": "0",
                   "isprating": "3.7",
                   "ispdlavg": "0",
                   "ip": "170.239.109.156",
                   "isp": "Rede Unicon",
                   "lon": "-35.0145",
                   "ispulavg": "0",
                   "country": "BR",
                   "lat": "-8.1136"
                   },
        "bytes_sent": 71286784,
        "download": 88967165.01931961,
        "timestamp": "2020-07-07T09:27:07.293366Z",
        "share": null,
        "bytes_received": 112039076,
        "ping": 24.827,
        "upload": 56004818.92664351,
        "server": {"latency": 24.827,
                   "name": "Jaboat\u00e3o dos Guararapes",
                   "url": "http://speedtest.powertecprovider.com.br:8080/speedtest/upload.php",
                   "country": "Brazil",
                   "lon": "-35.0089",
                   "cc": "BR",
                   "host": "speedtest.powertecprovider.com.br:8080",
                   "sponsor": "Powertec",
                   "lat": "-8.1076",
                   "id": "27004",
                   "d": 0.9083732997346309
                   }
        }

down_lista.append(round(json["download"] * 9.53674E-7, 2))
up_lista.append(round(json["upload"] * 9.53674E-7, 2))

if (len(down_lista) > 48):
    down_lista.pop(0)
    up_lista.pop(0)

Grafico(down_lista, up_lista).plotar()
