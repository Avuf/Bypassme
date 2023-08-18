import pyrogram
from pyrogram import Client
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ChatJoinRequest
import bypasser
import os
import ddl
import requests
from threading import Thread
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
# bot
bot_token = os.environ.get("TOKEN", "6603231946:AAFl2XnXTzUTj-HilY8Ws09YxDTFT33oc0k")
api_hash = os.environ.get("HASH", "4cebb9b44a78851588f0d48f2e68a386") 
api_id = os.environ.get("ID", "25271844")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)  
log_channel = os.environ.get("LOG_CHANNEL", "-1001321271473")
temp = {}  

@app.on_message(filters.command(["start"]))
async def send_start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        if log_channel:
            try:
                await app.send_message(log_channel, text="#NewUserLinkBypass"f'\nFirst Name: {message.from_user.first_name}\nUser ID: {message.from_user.id}\nUsername:  @{message.from_user.username}\nUser Link: {message.from_user.mention}')        
            except Exception as error:
                print(error)
    buttons = [
            [
                InlineKeyboardButton("❤‍🔥Update❤‍🔥", url='https://t.me/TellyBotzz'),
                InlineKeyboardButton("❤‍🔥Developer❤‍🔥", url='https://t.me/Legend_Shivam_7')
            ],
            [
                InlineKeyboardButton("⚡Request⚡", url='https://t.me/Legend_Shivam_7Bot')
            ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(f"**__👋 Hi **{message.from_user.mention}**, i am Link Bypasser Bot, just send me any supported links and i will bypass it\n\nSend /sites to see supported sites__**", reply_markup=reply_markup)
    

@app.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Fetching stats..')
    total_users = await db.total_users_count()
    await rju.edit(f"Total Users: <code>{total_users}</code>")

@app.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Broadcasting your messages...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        if not done % 20:
            try:
                await sts.edit(f"Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")     
            except:
                pass
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Broadcast Completed:\nCompleted in {time_taken} seconds.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}")


@app.on_message(filters.text)
async def receive(client: Client, message: pyrogram.types.messages_and_media.message.Message):
    global temp  
    try:
        if not await is_requested_one(client, message):
            if temp.get('LINK_ONE') is not None:  # Use get method to avoid KeyError
                ONE = temp['LINK_ONE']
            else:
                temp['LINK_ONE'] = (await app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
                ONE = temp['LINK_ONE']
            btn = [[
                InlineKeyboardButton(
                    "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🎗", url=ONE)
            ]]
            try:
                if not await is_requested_two(client, message):
                    if temp.get('LINK_TWO') is not None:  # Use get method to avoid KeyError
                        TWO = temp['LINK_TWO']
                    else:
                        temp['LINK_TWO'] = (await app.create_chat_invite_link(chat_id=CHANNEL_TWO, creates_join_request=True)).invite_link 
                        TWO = temp['LINK_TWO']
                    btn.append(
                        [
                            InlineKeyboardButton(
                                "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🎗", url=TWO)
                        ]
                    )
            except Exception as e:
                print(e)
            await app.send_message(
                chat_id=message.from_user.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(btn),
                parse_mode=enums.ParseMode.MARKDOWN
            )
            return

        if not await is_requested_two(client, message):
            if temp.get('LINK_TWO') is not None:  # Use get method to avoid KeyError
                TWO = temp['LINK_TWO']
            else:
                temp['LINK_TWO'] = (await app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
                TWO = temp['LINK_TWO']
            btn = [[
                InlineKeyboardButton(
                    "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🎗", url=TWO)
            ]]
            try:
                if not await is_requested_one(client, message):
                    if temp.get('LINK_ONE') is not None:  # Use get method to avoid KeyError
                        ONE = temp['LINK_ONE']
                    else:
                        temp['LINK_ONE'] = (await app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
                        ONE = temp['LINK_ONE']
                    btn.append(
                        [
                            InlineKeyboardButton(
                                "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🎗", url=ONE)
                        ]
                    )
            except Exception as e:
                print(e)
            await app.send_message(
                chat_id=message.from_user.id,
                text="**Please Join My Updates Channel to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(btn),
                parse_mode=enums.ParseMode.MARKDOWN
            )
            return
    except Exception as e:
        print(e)
    bypass = Thread(target=lambda:loopthread(message),daemon=True)
    bypass.start()

def handleIndex(ele,message,msg):
    result = bypasser.scrapeIndex(ele)
    try: app.delete_messages(message.chat.id, msg.id)
    except: pass
    for page in result: app.send_message(message.chat.id, page, reply_to_message_id=message.id, disable_web_page_preview=True)
   

@app.on_message(filters.command(["sites"]))
def send_sites(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, SITES_TEXT,
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡Request⚡", url='https://t.me/Legend_Shivam_7Bot')]]), reply_to_message_id=message.id)


@app.on_message([filters.document, filters.photo, filters.video])
async def docfile(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    global temp  # Use the global temp dictionary

    try:
        if message.document.file_name.endswith("dlc"):
            bypass = threading.Thread(target=lambda: docthread(message), daemon=True)
            bypass.start()
            return
    except:
        pass
    bypass = Thread(target=lambda:loopthread(message),daemon=True)
    bypass.start()

@app.on_chat_join_request(
    filters.chat(CHANNEL_ONE) | filters.chat(CHANNEL_TWO)
)
async def join_reqs(_, join_req: ChatJoinRequest):
    user_id = join_req.from_user.id
    try:
        if join_req.chat.id == CHANNEL_ONE:
            await db.add_req_one(user_id)
        else:
            await db.add_req_two(user_id)
    except Exception as e:
        print(f"Error adding join request: {e}")


@app.on_message(filters.command('purge_one') & filters.private & filters.user(ADMINS))
async def purge_req_one(bot, message):
    r = await message.reply("`processing...`")
    await db.delete_all_one()
    await r.edit("**Req db Cleared**" )


@app.on_message(filters.command('purge_two') & filters.private & filters.user(ADMINS))
async def purge_req_two(bot, message):
    r = await message.reply("`processing...`")
    await db.delete_all_two()
    await r.edit("**Req db Cleared**" )

def loopthread(message,otherss=False):

    urls = []
    if otherss: texts = message.caption
    else: texts = message.text

    if texts in [None,""]: return
    for ele in texts.split():
        if "http://" in ele or "https://" in ele:
            urls.append(ele)
    if len(urls) == 0: return

    if bypasser.ispresent(bypasser.ddl.ddllist,urls[0]):
        msg = app.send_message(message.chat.id, "⚡ __generating...__", reply_to_message_id=message.id)
    elif freewall.pass_paywall(urls[0], check=True):
        msg = app.send_message(message.chat.id, "🕴️ __jumping the wall...__", reply_to_message_id=message.id)
    else:
        if "https://olamovies" in urls[0] or "https://psa.wf/" in urls[0]:
            msg = app.send_message(message.chat.id, "⏳ __this might take some time...__", reply_to_message_id=message.id)
        else:
            msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)

    strt = time()
    links = ""
    temp = None
    for ele in urls:
        if search(r"https?:\/\/(?:[\w.-]+)?\.\w+\/\d+:", ele):
            handleIndex(ele,message,msg)
            return
        elif bypasser.ispresent(bypasser.ddl.ddllist,ele):
            try: temp = bypasser.ddl.direct_link_generator(ele)
            except Exception as e: temp = "**Error**: " + str(e)
        elif freewall.pass_paywall(ele, check=True):
            freefile = freewall.pass_paywall(ele)
            if freefile:
                try: 
                    app.send_document(message.chat.id, freefile, reply_to_message_id=message.id)
                    remove(freefile)
                    app.delete_messages(message.chat.id,[msg.id])
                    return
                except: pass
            else: app.send_message(message.chat.id, "__Failed to Jump", reply_to_message_id=message.id)
        else:    
            try: temp = bypasser.shortners(ele)
            except Exception as e: temp = "**Error**: " + str(e)
        print("bypassed:",temp)
        if temp != None: links = links + temp + "\n"
    end = time()
    print("Took " + "{:.2f}".format(end-strt) + "sec")

    if otherss:
        try:
            app.send_photo(message.chat.id, message.photo.file_id, f'__{links}__', reply_to_message_id=message.id)
            app.delete_messages(message.chat.id,[msg.id])
            return
        except: pass

    try: 
        final = []
        tmp = ""
        for ele in links.split("\n"):
            tmp += ele + "\n"
            if len(tmp) > 4000:
                final.append(tmp)
                tmp = ""
        final.append(tmp)
        app.delete_messages(message.chat.id, msg.id)
        tmsgid = message.id
        for ele in final:
            tmsg = app.send_message(message.chat.id, f'__{ele}__',reply_to_message_id=tmsgid, disable_web_page_preview=True)
            tmsgid = tmsg.id
    except Exception as e:
        app.send_message(message.chat.id, f"__Failed to Bypass : {e}__", reply_to_message_id=message.id)
        
def docthread(message):
    if message.document.file_name.endswith("dlc"):
        msg = app.send_message(message.chat.id, "🔎 __bypassing...__", reply_to_message_id=message.id)
        print("sent DLC file")
        sess = requests.session()
        file = app.download_media(message)
        dlccont = open(file,"r").read()
        link = bypasser.getlinks(dlccont,sess)
        app.edit_message_text(message.chat.id, msg.id, f'**__Ads Link - {urls}__**\n\n**__Original Link - {link}__**\n**__Generated By - [Link Bypasser](https://t.me/TellyLinkBypasser_bot)__**', disable_web_page_preview=True)
        os.remove(file)


print("Bot Starting")
app.run()
