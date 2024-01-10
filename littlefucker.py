import asyncio
import base64
import json

import httpx
import requests


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