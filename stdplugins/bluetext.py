# First plugin by Abin Paul Zackariah Hope this one will work

from telethon import events

@borg.on(events.NewMessage(pattern=r".bluetext", outgoing=True))
async def _(event):
   if event.fwd_from
        return
   await.event.edit("BLUE TEXT\n MUST CLICK\n I AM A STUPID ANIMAL THAT IS ATTRACTED TO COLORS")
