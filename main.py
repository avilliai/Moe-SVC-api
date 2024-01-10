import asyncio
import json
import os
from shutil import copyfile

import requests
import yaml
from flask import Flask, request, jsonify, send_file
import random


def random_str(random_length=6,chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789@$#_%'):
    """
    生成随机字符串作为验证码
    :param random_length: 字符串长度,默认为6
    :return: 随机字符串
    """
    string = ''

    length = len(chars) - 1
    # random = Random()
    # 设置循环每次取一个字符用来生成随机数
    for i in range(7):
        string +=  ((chars[random.randint(0, length)]))
    return string


app = Flask(__name__)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    # 解析请求中的参
    data = request.get_json()
    data=json.loads(data)
    text=data.get("text")
    speaker=data.get("speaker")
    #print(data)
    with open('characters.yaml', 'r', encoding='utf-8') as f:
        result2 = yaml.load(f.read(), Loader=yaml.FullLoader)
        #print(result2)
    if speaker in result2:
        #print("data")
        speaker1=result2.get(speaker)
        print(speaker1,type(speaker1))
        #url="https://api.pearktrue.cn/api/aivoice/?speak=月婷&text="+text
        voicM=2
        if "voice" not in data:
            if voicM==1:
                url = "https://api.vvhan.com/api/song?txt=" + text+"&per=6"
                r = requests.get(url)
                p = random_str()+".mp3"
                with open("raw/" + p , "wb") as fb:
                    fb.write(r.content)
            else:
                p=random_str()+".mp3"
                prf="raw/"+p
                command=f"edge-tts --voice zh-CN-XiaoyiNeural --text {text} --write-media {prf}"
                os.system(command)
                trim = 0
        else:
            voicepath=data.get("voice")
            p = str(voicepath).split("/")[-1]
            copyfile(voicepath, "raw/"+p)
            trim=20
        model = speaker1.get("model")
        config = speaker1.get("config")
        speaker222 = speaker1.get("speaker")
        name = p
        print(p)
        waveform = "wav"

        command = f"python inference_main.py -m {model} -c {config} -s {speaker222} -n {name} -wf {waveform} -t {trim} -eak 10"
        # 拼接你的指令字符串
        if "venv" in os.listdir():
            os.system("cd venv/Scripts")
            os.system("call activate.bat")
            os.system("cd ../..")

            os.system(command)
        else:
            os.system(command)

        return send_file("results/"+p.replace(".mp3",".wav"), as_attachment=True)
    # 将生成的音频返回给客户端
    #return out
    #return jsonify({'audio': audio.tolist()})
if __name__ == '__main__':
    app.run(debug=False,host='127.0.0.1', port=9082)