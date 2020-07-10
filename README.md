<p align="center">
    <img align="center" src="https://ik.imagekit.io/nilson/graph_C6DJab2qX.png" alt="speedtest-graph">
</p>
<p align="center">
<a href="https://github.com/nilson-santos/speedtest-graph/blob/master/LICENSE"><img src="https://ik.imagekit.io/nilson/license_npETnzBm2.svg" alt="License"></a>
</p>


---
## 📑Index
- [About](-About)
- [Technologies used](-Technologies-used)
- [Installing dependencies](-Installing-dependencies)
- [How to use](-How-to-use)
---
## 📄About

<p>
The <b>Speedtest Graph</b> project is a bot developed in Python3 and aims to serve speed measurement graphs from the Internet and send to Twitter.
</p>

---
## 🛠Technologies used
- [Python](https://www.python.org/)
- [Speedtest](https://www.speedtest.net/)
- [Twitter](https://twitter.com/)
---
## 📦Installing dependencies
```bash
    pip install speedtest-cli
    
    pip install numpy
    
    pip install matplotlib
    
    pip install tweepy
```
---
## 📦How to use

```bash
    # clone directory
    git clone https://github.com/nilson-santos/speedtest-graph
```
```bash
    # enter into directory
    cd speedtest-graph
```

   You need to create a json file with Twitter keys
   "secrets.json" must contain. get your keys [here](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens)


```json
    {
        "consumer_key": "**************************",
        "consumer_secret": "**************************************************",
        "access_token": "**********-****************************************",
        "access_token_secret": "**************************************************"
    }
```
```bash
    # run the project
    python main.py
```
---
<p align="center">
developed by Evanilson Andrade dos Santos - Nilson Santos
</p>
<p align="center">
www.nilson.com.br
</p>