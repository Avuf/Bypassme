from pyrogram import Client

from aiohttp import web
from plugins import web_server

PORT = "8080"

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="mybot",
            api_id=int(25271844),
            api_hash="4cebb9b44a78851588f0d48f2e68a386",
            bot_token="6603231946:AAFl2XnXTzUTj-HilY8Ws09YxDTFT33oc0k",
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        print("Bot Started💝")
     #   app = web.AppRunner(await web_server())
      #  await app.setup()
     #   bind_address = "0.0.0.0"
    #    await web.TCPSite(app, bind_address, PORT).start()
      

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


app = Bot()
app.run()
