from io import open_code
import discord,json,random,time
from discord.ext import commands
client = discord.Client()
print('Connected Successfully: Maurice v2.0 is Online.\n\n------------Start of Conversation-------------')

with open('people.json','r') as file:
    names = json.load(file)
name = "alex"
bad_words = ['shit','fuck','fucking','bitch','cunt','fucker']
greetings = [['hello','hi'],['how are you','how are you doing']]
responses = ['Hi, how are you doing?','Hey there! How are things?',f'Hi there {name}!']
affirmative = ['yes','yeah','ok']
negatory = ['no','nah']

@client.event
async def on_message(message):
    if isinstance(message.channel,discord.channel.DMChannel):
        if message.author != client.user:
            channel = message.channel
            with open('people.json','r') as file:
                names = json.load(file)
                name = names[message.author.name]
            newMessage = message.content.lower()
            if newMessage.startswith('call me'):
                messageList = newMessage.split()
                call_position = messageList.index('call') + 1
                me_position = messageList.index('me') + 1
                if me_position - call_position == 1:
                    name = messageList[me_position]
                    response = f"Ok, I'll call you {name} from now on then."
                    names.update({message.author.name:name})
                    with open('people.json','w') as file:
                        file.seek(0)
                        file.truncate()
                        json.dump(names,file,indent = 2)
            if newMessage.startswith('ping'):
                response = 'pong'
            if any(words in newMessage for words in bad_words):
                response = "What's wrong?"
            if any(words in newMessage for words in greetings[0]):
                name = names[message.author.name]
                response = responses[random.randint(0,len(responses)-1)]
            if any(words in newMessage for words in greetings[1]):
                response = "I'm good, thanks!"
            if newMessage == "what's my name?":
                response = f"Your name is {name}"
            time.sleep(0.1)
            await channel.send(response)
            print(f'\n{message.author.display_name}> {message.content}\n\n{client.user.name}> {response}')

client.run('ODU4OTk2NDczMDgxMjMzNDI5.YNmQzg.ae7vb9vIi6VMwlSwNWqW4SvoEQI')