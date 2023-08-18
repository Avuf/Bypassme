import pyrogram
from pyrogram import Client
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ChatJoinRequest, Message
import bypasser
import os
import ddl
import requests
import threading 
from texts import HELP_TEXT
from bypasser import ispresent, SITES_TEXT, gdtot3, GDTot_Crypt
import requests
from requests import get as rget
import base64
from urllib.parse import unquote, urlparse, parse_qs, quote
import time
import cloudscraper
from bs4 import BeautifulSoup, NavigableString, Tag
from lxml import etree
from cloudscraper import create_scraper
from uuid import uuid4
import hashlib
import json
from dotenv import load_dotenv
load_dotenv()
from asyncio import sleep as asleep
import PyBypass
import os
from pyrogram import Client
from pyrogram.types import Message 
from cloudscraper import create_scraper
from os import path
from http.cookiejar import MozillaCookieJar
from lxml import etree
from re import findall, match, search, sub
from uuid import uuid4
import time
import datetime
from database import db
from info import CHANNEL_TWO, CHANNEL_ONE, ADMINS, is_requested_one, is_requested_two, broadcast_messages
from bypasser import *
from pyrogram.enums import MessageEntityType, ChatMemberStatus
from pyrogram.errors import RPCError, FloodWait, UserNotParticipant
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
        logging.info("Bot stopped. Bye.")


app = Bot()
app.run()
