"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Currently Alive, my peru master!` **ψ(｀∇´)ψ**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "`Bot created by:` [SnapDragon](tg://user?id=719877937), @gujjuopgohil\n"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "https://www.youtube.com/c/opgohil")
import asyncio
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, hellversion
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/mp4-11-24"
pm_caption = "__**🔥🔥ÒP ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈Òpẞø†😈       : `{hellversion}`\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"
pm_caption += "Currently Alive, my peru master! ψ(｀∇´)ψ"
pm_caption += "MY Details iz" 
pm_caption += "I aM A Ro BOT OP"
pm_caption += "Telethon version: 6.9.0"
pm_caption += "MY GoD iZ @Gujjuopgohil"
pm_caption += "Python: 3.7.3"

pm_caption += "Bot created by: SnapDragon, @opgohil"

pm_caption += "My peru owner: @GUJJUOPGOHIL"
pm_caption += f"I Talk To YöU 😠"
pm_caption += "Bol kya kam he Bhadve (‘_’)"


#@command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
