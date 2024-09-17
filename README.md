- so-vits-api，基于flask以api形式调用语音合成/语音转换
- [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc/tree/Moe-SVC?tab=readme-ov-file)

**注意，项目对各依赖的要求较为复杂，强烈建议使用[python3.9.0](https://github.com/avilliai/wReply/releases/tag/yirimirai-Bot) ，由于python版本问题产生的报错请自行搜索解决。**
# 部署项目
前置
安装[C艹 生成工具](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/)

1.在任意位置打开cmd或者git bash，执行
```
git clone https://github.com/avilliai/Moe-SVC-api.git
```
1.1 下载必要文件
- 下载[checkpoint_best_legacy_500.pt](https://ibm.ent.box.com/s/z1wgl1stco8ffooyatzdwsqn2psd9lrr) 并放入hubert文件夹
- 必要：下载[模型](https://huggingface.co/TachibanaKimika/so-vits-svc-4.0-models) 你也可以用自己的
- 把你的模型和配置文件放置在logs文件夹下(实际上你放别的地方也行，根据下一步建立索引即可)

1.2 建立模型索引
- 以记事本打开characters.yaml
```
riri:             #触发名，可自定义
  speaker: riri                #以模型配置文件即config里面的spk项为准，使用默认config.json则无需修改此项
  model: logs/G_riri_220.pth   #模型对应根目录的相对路径
  config: configs/config.json  #配置文件相对路径，使用默认config.json则无需修改此项
#如果你有多个模型，按同样方式构建索引即可
塔菲:             #触发名，可自定义
  speaker: taffy       #以模型配置文件即config里面的spk项为准，使用默认配置文件则无需修改此项
  model: logs/G_taffy_250.pth   #模型对应根目录的相对路径
  config: configs/config.json  #配置文件相对路径，使用默认配置文件则无需修改此项
```
- 模型和配置文件的索引需要正确。speaker必须以模型配套配置文件里面的spk值为准，如果没有配套config.json就用默认的configs/config.json，无需修改speaker和config

2.部署环境

双击 一键部署脚本.bat

3.启动

双击 启动脚本.bat
# 调用
## 现有项目对接
[Manyana](https://github.com/avilliai/Manyana)
- 将settings.yaml中voicegenerate设置为so-vits
- 将settings.yaml中speaker设置为你characters.yaml中的【自定义触发名】(不是spk那个)，这样ai回复的时候就直接能调用它了。
- (可选)在settings.yaml中so_vits_speakers，添加你自己上面characters.yaml设置的【自定义触发名】(不是spk那个)
## 自行调用
api接收三个参数，一般传两个即可，即
```
speaker      说话人，你characters.yaml中的自定义触发名
text         文本
(可选)voice   携带此参数时，则为语音转换，voice需要传递原始语音文件的绝对路径    
```
tts实例
```
import asyncio
import base64
import json

import httpx
async def eh():
    url = "http://127.0.0.1:5000/synthesize"  # 后端服务的地址
    params = {"text": "早上好，亲爱的，你觉得今天天气怎样", "speaker": "riri"}  # 请求参数
    async with httpx.AsyncClient(timeout=200) as client:
        r=await client.post(url, json=json.dumps(params))
        with open("raw.wav", "wb") as fb:
            fb.write(r.content)
asyncio.run(eh())
```

