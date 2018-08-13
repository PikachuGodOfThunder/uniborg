from telethon import events
import gsearch
import subprocess

@borg.on(events.NewMessage(outgoing=True,pattern=r'.google (.*)'))
async def gsearch(event):
        match = event.pattern_match.group(1)
        result_=subprocess.run(['gsearch', match], stdout=subprocess.PIPE)
        result=str(result_.stdout.decode())
        await client.send_message(await client.get_input_entity(event.chat_id), message='**Search:**\n`' + match + '`\n\n**Result:**\n' + result, reply_to=event.id, link_preview=False)
        await client.send_message(-1001200493978,"Google Search query "+match+" was executed successfully")
