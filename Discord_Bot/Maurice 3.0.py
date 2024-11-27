from io import open_code
import discord,json,random,time
from discord.ext import commands
client = discord.Client()
print('Connected Successfully: Maurice v3.0 is Online.\n\n------------Start of Conversation-------------')

@client.event
async def on_message(message):
    if isinstance(message.channel,discord.channel.DMChannel):
        if message.author != client.user:
            channel = message.channel
            #868242847579643905
            newMessage = message.content.lower()
            if newMessage.startswith('maria'):
                for i in range(0,5):
                    em = discord.Embed(title="Hi!")
                    em.set_image(url="https://c.tenor.com/5HIKskKbeZkAAAAd/tp-mar%C3%ADa.gif")
                    await channel.send(embed=em)
                    print(channel.id)
            time.sleep(0.1)
            #await channel.send(response)
            #print(f'\n{message.author.display_name}> {message.content}\n\n{client.user.name}> {response}')

client.run('ODU4OTk2NDczMDgxMjMzNDI5.YNmQzg.ae7vb9vIi6VMwlSwNWqW4SvoEQI')