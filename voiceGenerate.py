import asyncio

import edge_tts

TEXT = "你好哟，我是智能语音助手，小伊"

OUTPUT_FILE = "test.mp3"


async def _main(TEXT,VOICE):
    VOICE = "zh-CN-XiaoyiNeural"
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(_main())
