import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://clicksfly.com/ref/111301026318453615482')
    START_TXT = environ.get("START_TXT", '''𝐇𝐄𝐘 {},
𝐌𝐲𝐬𝐞𝐥𝐟 <a href=https://t.me/{}>{}</a>,\n\n𝙏𝙧𝙪𝙨𝙩 𝙢𝙚 ! 𝙔𝙤𝙪 𝙘𝙖𝙣'𝙩 𝙚𝙫𝙚𝙣 𝙞𝙢𝙖𝙜𝙞𝙣𝙚 𝙝𝙤𝙬 𝙨𝙪𝙥𝙚𝙧-𝙛𝙖𝙨𝙩 𝙞 𝙘𝙖𝙣 𝙙𝙧𝙞𝙫𝙚 𝙮𝙤𝙪𝙧 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 \n\nAʀᴇ ʏᴏᴜ ʀᴇᴀᴅʏ ғᴏʀ ᴀ Lᴏɴɢ Dʀɪᴠᴇ 😎''')
    HELP_TXT = """𝙃𝙚𝙮 {}
𝙃𝙀𝙍𝙀 𝙄𝙎 𝙈𝙔 𝙃𝙀𝙇𝙋 𝘾𝙊𝙈𝙈𝘼𝙉𝘿."""
    ABOUT_TXT = """✯ 𝐌𝐘 𝐍𝐀𝐌𝐄 : {}
✯ 𝐂𝐑𝐄𝐀𝐓𝐎𝐑: <a href=https://t.me/pArAd0X6>pArAd0X6</a>
✯ 𝐋𝐈𝐁𝐑𝐀𝐑𝐘: 𝐏𝐘𝐏𝐑𝐎𝐆𝐑𝐀𝐌
✯ 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄: 𝐏𝐘𝐓𝐇𝐎𝐍 3
✯ 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄: 𝐌𝐎𝐍𝐆𝐎 𝐃𝐁
✯ 𝐁𝐎𝐓 𝐒𝐄𝐑𝐕𝐄𝐑: 𝐊𝐎𝐘𝐄𝐁
✯ 𝐁𝐔𝐈𝐋𝐃 𝐒𝐓𝐀𝐓𝐔𝐒: 𝐯-69 [ ミ *༄ᶦᶰᵈ᭄࿐𝘗𝘢𝘳𝘢𝘥𝟎𝘹 么 彡 ]"""
    SOURCE_TXT = """<b>ミ *༄ᶦᶰᵈ᭄࿐𝘗𝘢𝘳𝘢𝘥𝟎𝘹 么 彡 is an open source project</b>

You can easily get its source code from github - <a href='https://github.com/LazyDeveloperr/LazyPrincessV2'>LazyDeveloperr</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/pArAd0X6)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code> Mɪʙ
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code> Mɪʙ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
