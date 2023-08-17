import pyrogram
from pyrogram import Client
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
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

from database import db
from info import CHANNEL_TWO, CHANNEL_ONE, ADMINS,temp, is_requested_one, is_requested_two, broadcast_messages
from bypasser import *
from pyrogram.enums import MessageEntityType, ChatMemberStatus
from pyrogram.errors import RPCError, FloodWait, UserNotParticipant
# bot
bot_token = os.environ.get("TOKEN", "6603231946:AAFl2XnXTzUTj-HilY8Ws09YxDTFT33oc0k")
api_hash = os.environ.get("HASH", "4cebb9b44a78851588f0d48f2e68a386") 
api_id = os.environ.get("ID", "25271844")
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)  
log_channel = os.environ.get("LOG_CHANNEL", "-1001321271473")

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
    
def handleIndex(ele,message,msg):
    result = bypasser.scrapeIndex(ele)
    try: app.delete_messages(message.chat.id, msg.id)
    except: pass
    for page in result: app.send_message(message.chat.id, page, reply_to_message_id=message.id, disable_web_page_preview=True)


# loop thread
def loopthread(client, message):
 #   if not handle_force_sub(Client, message):
  #         return
    if CHANNEL_ONE and not is_requested_one(client, message):
        if temp.LINK_ONE is not None:
            ONE = temp.LINK_ONE
        else:
            temp.LINK_ONE = (app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
            ONE = temp.LINK_ONE
        btn = [[
            InlineKeyboardButton(
                "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🎗", url=ONE)
        ]]
        try:
            if CHANNEL_TWO  and not is_requested_two(client, message):
                if temp.LINK_TWO is not None:
                    TWO = temp.LINK_TWO
                else:
                    temp.LINK_ONE = (app.create_chat_invite_link(chat_id=CHANNEL_TWO, creates_join_request=True)).invite_link 
                    TWO = temp.LINK_TWO
                btn.append(
                      [
                    InlineKeyboardButton(
                        "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🎗", url=TWO)
                      ]
                )
        except Exception as e:
            print(e)
        app.send_message(
            chat_id=message.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return

    if CHANNEL_TWO and not is_requested_two(client, message):
        if temp.LINK_TWO is not None:
            TWO = temp.LINK_TWO
        else:
            temp.LINK_TWO = (app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
            ONE = temp.LINK_TWO
        btn = [[
            InlineKeyboardButton(
                "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🎗", url=TWO)
        ]]
        try:
            if CHANNEL_ONE  and not is_requested_one(client, message):
                if temp.LINK_ONE is not None:
                    ONE = temp.LINK_ONE
                else:
                    temp.LINK_ONE = (app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
                    ONE = temp.LINK_ONE
                btn.append(
                      [
                    InlineKeyboardButton(
                        "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🎗", url=ONE)
                      ]
                )
        except Exception as e:
            print(e)
        app.send_message(
            chat_id=message.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
    urls = []
    for ele in message.text.split():
        if "http://" in ele or "https://" in ele:
            urls.append(ele)
    if len(urls) == 0: return

    if bypasser.ispresent(ddllist,urls[0]):
        msg = app.send_message(message.chat.id, "⚡ __generating... Please Wait 8-10 Seconds__", reply_to_message_id=message.id)
    else:
        if urls[0] in "https://olamovies" or urls[0] in "https://psa.pm/":
            msg = app.send_message(message.chat.id, "🔎 __this might take some time...__", reply_to_message_id=message.id)
        else:
            msg = app.send_message(message.chat.id, "🔎 __bypassing... Please Wait 8-10 Seconds__", reply_to_message_id=message.id)
           
            
    link = ""
    for ele in urls:
        if ele.split("/")[3] == "0:":
            handleIndex(ele,message,msg)
            return
        elif bypasser.ispresent(ddllist,ele):
            try: temp = ddl.direct_link_generator(ele)
            except Exception as e: temp = "**Error**: " + str(e)
        else:    
            try: temp = bypasser.shortners(ele)
            except Exception as e: temp = "**Error**: " + str(e)
        print("bypassed:",temp)
        link = link + temp + "\n\n"
        
    try:
        app.edit_message_text(message.chat.id, msg.id, f'**__Ads Link - {urls}__**\n\n**__Original Link - {link}__**\n**__Generated By - [Link Bypasser](https://t.me/TellyLinkBypasser_bot)\n\n⚡Powered By - @TellyBotzz__**', disable_web_page_preview=True)#,
       # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡Request⚡", url='https://t.me/Legend_Shivam_7Bot')]]), reply_to_message_id=message.id)
        app.send_message(log_channel, text=f"**__Ads Link - {urls}__**\n\n**__Original Link - {link}__**\n**__Generated By - [Link Bypasser](https://t.me/TellyLinkBypasser_bot)__**\n\n**__Requested By: {message.from_user.mention}__**\n**__First Name: {message.from_user.first_name}__**\n**__Username: @{message.from_user.username}__**\n**__ID: {message.from_user.id}__**\n\n**__#BypassLinks__**") 
         
    except:
        try: 
            app.edit_message_text(message.chat.id, msg.id, "__Failed to Bypass__",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡Complaint⚡", url="https://t.me/Legend_Shivam_7Bot")]]), reply_to_message_id=message.id)
        except:
            try: app.delete_messages(message.chat.id, msg.id)
            except: pass
            app.send_message(message.chat.id, "__Failed to Bypass__",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡Complaint⚡", url="https://t.me/Legend_Shivam_7Bot")]]), reply_to_message_id=message.id)

# start command



# help command
@app.on_message(filters.command(["sites"]))
def send_sites(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, SITES_TEXT,
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡Request⚡", url='https://t.me/Legend_Shivam_7Bot')]]), reply_to_message_id=message.id)



        
        
# links
@app.on_message(filters.text)
def receive(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    if CHANNEL_ONE and not is_requested_one(client, message):
        if temp.LINK_ONE is not None:
            ONE = temp.LINK_ONE
        else:
            temp.LINK_ONE = (app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
            ONE = temp.LINK_ONE
        btn = [[
            InlineKeyboardButton(
                "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🎗", url=ONE)
        ]]
        try:
            if CHANNEL_TWO  and not is_requested_two(client, message):
                if temp.LINK_TWO is not None:
                    TWO = temp.LINK_TWO
                else:
                    temp.LINK_ONE = (app.create_chat_invite_link(chat_id=CHANNEL_TWO, creates_join_request=True)).invite_link 
                    TWO = temp.LINK_TWO
                btn.append(
                      [
                    InlineKeyboardButton(
                        "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🎗", url=TWO)
                      ]
                )
        except Exception as e:
            print(e)
        app.send_message(
            chat_id=message.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return

    if CHANNEL_TWO and not is_requested_two(client, message):
        if temp.LINK_TWO is not None:
            TWO = temp.LINK_TWO
        else:
            temp.LINK_TWO = (app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
            ONE = temp.LINK_TWO
        btn = [[
            InlineKeyboardButton(
                "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 1 🎗", url=TWO)
        ]]
        try:
            if CHANNEL_ONE  and not is_requested_one(client, message):
                if temp.LINK_ONE is not None:
                    ONE = temp.LINK_ONE
                else:
                    temp.LINK_ONE = (app.create_chat_invite_link(chat_id=CHANNEL_ONE, creates_join_request=True)).invite_link 
                    ONE = temp.LINK_ONE
                btn.append(
                      [
                    InlineKeyboardButton(
                        "🎗 Rᴇǫᴜᴇꜱᴛ Tᴏ Jᴏɪɴ Cʜᴀɴɴᴇʟ 2 🎗", url=ONE)
                      ]
                )
        except Exception as e:
            print(e)
        app.send_message(
            chat_id=message.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
    
    bypass = threading.Thread(target=lambda:loopthread(client, message),daemon=True)
    bypass.start()


# doc thread
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


# doc


def handle_force_sub(bot: pyrogram.client.Client, cmd: pyrogram.types.messages_and_media.message.Message):
    try:
        user = bot.get_chat_member(chat_id=-1001976892848,
                                         user_id=cmd.from_user.id)
        if user.status in (ChatMemberStatus.BANNED,
                           ChatMemberStatus.RESTRICTED):
            cmd.reply_text(
                text=
                "Sorry, You are Banned to use me. Contact my [Shivam](https://t.me/Legend_Shivam_7).",
                disable_web_page_preview=True,
            )
            return 0
    except UserNotParticipant:
        try:
            cmd.reply_text(
                text="Due to Overload Only Channel Members Can Use Me",
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            "Join Now",
                            url="https://t.me/Cyber_Robots",
                        )
                    ],
                ]),
            )
            return 0
        except RPCError as e:
            print(e.MESSAGE)
    except FloodWait as ee:
        sleep(ee.value + 3)
        cmd.reply_text("Try later flooded!")
        return 0
    except Exception:
        cmd.reply_text(
            text=
            "Something went Wrong! Contact [Shivam](https://t.me/Legend_Shivam_7)",
            disable_web_page_preview=True,
        )
        return 0
    return 1

@app.on_message(filters.document)
def docfile(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    bypass = threading.Thread(target=lambda:docthread(message),daemon=True)
    bypass.start()


# server loop
print("Bot Starting")
app.run()
