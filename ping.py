from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
from time import sleep


@borg.on(admin_cmd("ping"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("`Пагодь....`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    sleep(0.5)
    await event.edit("`Да жив я, че пристал`\n`{}ms`".format(ms))