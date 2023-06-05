import os
import aiohttp


from fastapi import FastAPI
import uvicorn
import requests


from schemas import Answer


TG_API = os.getenv("BOT_API_KEY")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")
URL = os.getenv("URL")


app = FastAPI()


@app.post("/")
async def read_root(obj: Answer):
    if obj.message.chat.id == int(ADMIN_ID):
        if obj.message.reply_to_message is not None:
            data = {
                'chat_id': obj.message.reply_to_message.forward_from.chat_id,
                'from_chat_id': obj.message.from_f.chat_id,
                'message_id': obj.message.message_id
            }  
            async with aiohttp.ClientSession() as session:
                async with session.post(f'https://api.telegram.org/bot{TG_API}/copyMessage', data = data) as response:
                    print(response.status)
    else:
        data = {
            'chat_id': ADMIN_ID,
            'from_chat_id': obj.message.from_f.chat_id,
            'message_id': obj.message.message_id
        }  
        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://api.telegram.org/bot{TG_API}/forwardMessage', data = data) as response:
                print(response.status)

    return {"ok": "ok"}


if __name__ == "__main__":
    requests.get(f'https://api.telegram.org/bot{TG_API}/setWebhook?url=https://{URL}/')
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
