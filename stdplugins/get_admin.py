# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins


@borg.on(events.NewMessage(pattern=".get_admin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    mentions = "**Admins in this Chat**: \n"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"\n[{x.first_name}](tg://user?id={x.id})"
    await borg.send_message(
        chat, mentions, reply_to=event.message.reply_to_msg_id)
