"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio

from telethon import events

from userbot.utils import admin_cmd, sudo_cmd

from userbot import ALIVE_NAME, opversion

from telethon.tl.types import ChannelParticipantsAdmins

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "OP User"

ludosudo = Config.SUDO_USERS

if ludosudo:

    sudou = "True"

else:

    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/Op-11-24-2"

pm_caption = "__**🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={gujjuopgohil})』**\n\n"

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈ÓP-ẞø†😈       : `{hellversion}`\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/GUJJUOPGOHIL)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/GUJJUOPGOHIL)\n\n"

pm_caption += "      [✨REPO✨](https://github.com/hellboy-op/hellbot) 🔹 [📜License📜](https://github.com/HellBoy-OP/HellBot/blob/master/LICENSE)"

#@command(outgoing=True, pattern="^.alive$")

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))

@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))

async def amireallyalive(alive):

    chat = await alive.get_chat()

    await alive.delete()

    """ For .alive command, check if the bot is running.  """

    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    await alive.delete() 
