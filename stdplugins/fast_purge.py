from telethon import events

@borg.on(events.NewMessage(outgoing=True, pattern='.fastpurge'))  
async def fastpurge(event):
   chat = await event.get_input_chat()
   msgs = []
   count =0
   async with aclosing(client.iter_messages(chat, min_id=event.reply_to_msg_id)) as h:
    async for m in h:
        msgs.append(m)
        count=count+1
        if len(msgs) == 100:
            await client.delete_messages(chat, msgs)
            msgs = []
   if msgs:
    await client.delete_messages(chat, msgs)
   await client.send_message(event.chat_id,"```Fast Purge Complete!\n```Purged "+str(count)+" messages. **This auto-generated message shall be self destructed in 2 seconds.**")
   await client.send_message(-1001200493978,"Purge of "+str(count)+" messages done successfully.")
   time.sleep(2)
   i=1
   async for message in client.iter_messages(event.chat_id,from_user='me'):
        if i>1:
            break
        i=i+1
        await message.delete()
