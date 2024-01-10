import asyncio
import base64
import json

import httpx
import requests

url="http://grouptalk.c2c.qq.com/?ver=0&rkey=3062020101045b30590201010201010204c94f794e042439305033746c5a4341516d48754f5f757279725f48686151555f5530624f347235746f300204659e65df041f0000000866696c6574797065000000013100000005636f64656300000001310400&filetype=1&voice_codec=1"
r=requests.get(url)
with open("raw.silk", "wb") as fb:
    fb.write(r.content)
    print("ok")
    input()
# 发送请求到后端服务
url = "http://127.0.0.1:5000/synthesize" # 后端服务的地址
params = {"text": "早上好，亲爱的，你觉得今天天气怎样","speaker": "riri"} # 请求参数
r = requests.post(url,json=json.dumps(params)) # 发送post请求
input()
#print(response.text)

        # 请求参数
async def eh():
    url = "http://127.0.0.1:5000/synthesize"  # 后端服务的地址
    params = {"text": "早上好，亲爱的，你觉得今天天气怎样", "speaker": "riri"}  # 请求参数
    async with httpx.AsyncClient(timeout=200) as client:
        r=await client.post(url, json=json.dumps(params))
        with open("raw.wav", "wb") as fb:
            fb.write(r.content)
asyncio.run(eh())