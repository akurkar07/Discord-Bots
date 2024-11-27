import discord, requests,json
from discord import user
from time import sleep
from discord.ext import commands

print('Initializing...')
bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
  print('\nHi, my name is Maurice Moss! I just woke up!')

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.dm_only()
    async def on_message(self,message):
        print('x')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

    @commands.command()
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            channel = member.dm_channel
            if channel is None:
                channel = await member.create_dm()
            em = discord.Embed(title="It's that time of the week again!")
            em.set_image(url="https://media1.tenor.com/images/720ec30e99758f06a32e1905f2a9f810/tenor.gif?itemid=22250042")
            await channel.send(embed=em)
            print(f'\n{member.name} has been poked!')
    
    @commands.command()
    async def oc(self, ctx,member: discord.Member = None):
        if member is not None:
            name = member.name
            id = member.id
            with open('people.json','r+') as file:
                fileContents = json.load(file)
            channel = member.dm_channel
            if channel is None:
                channel = await member.create_dm()
            await channel.send(f'Hi there!{name}')
        print(f'\n{name},{id}')
        
bot.add_cog(Test(bot))

bot.run('ODU4OTk2NDczMDgxMjMzNDI5.YNmQzg.ae7vb9vIi6VMwlSwNWqW4SvoEQI')

