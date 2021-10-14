
# # import urllib.request, json 
# from urllib import urlopen
# import json

# 
# with urllib.request.urlopen(addr+inp.replace(" ",'%20')) as url:
#     data = json.loads(url.read().decode())

# addr = "http://9cd2-103-151-184-6.ngrok.io/ls"# ch
# import requests
# inp = input("")
# print(addr)
# url = requests.get(addr)
# htmltext = url.text
# print(htmltext)

# from urllib import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
import json
# url = input("paste url")
url = "https://c882-103-151-184-6.ngrok.io/"

while True:
    cmd = input("enter lines").replace(" ","%20")
    res = urllib.request.urlopen(url+"run/"+cmd).read().decode()
    # print(type(res))
    res = res.replace("!@#$","\\n")
    data = json.loads(res)
    print(data)