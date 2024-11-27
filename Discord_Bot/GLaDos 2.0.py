import discord, requests,json
from time import sleep
from discord.ext import commands
from datetime import datetime

print('Initializing...') #making console look fancy
sleep(0.5)
print('\n.')
sleep(0.5)
print('\n..')
sleep(0.5)
print('\n...\n')
bot = commands.Bot(command_prefix='!') #setting up discord client

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=""))                  
  print('Initialization complete.\n\nThe bot the humans call GLaDoS is online!')

global data
crypto_URL = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'
bad_words = ['shit', 'fuck', 'bitch', 'Fuck', 'Shit', 'Bitch', 'Stfu', 'dick']
data = {
  'balance':0,
  'BTCnum':0,
  'ETHnum':0,
  'BTCbuyin':0,
  'ETHbuyin':0
}
def getPrice(coin, currency):
  try:
    response = requests.get(crypto_URL.format(coin, currency)).json()
    return response
  except:
    return False

def getData():
  with open('data.json', 'r') as file: #gets data from a JSON file.                                               
    data = json.load(file)
    data['balance'] = float(data['balance']) 
    data['BTCbuyin'] = float(data['BTCbuyin'])
    data['ETHbuyin'] = float(data['ETHbuyin'])
  return data

@bot.command(aliases = ['b'])
async def balance(ctx):
  data = getData() 
  em = discord.Embed(title="**__Total Balance:__**",color=ctx.author.color)
  em.add_field(name="**Bitcoin**", value=data['BTCnum'])
  em.add_field(name="**Etherium**", value=data['ETHnum'])
  em.add_field(name="**Balance**", value=data['balance'])
  em.set_thumbnail(url='https://th.bing.com/th/id/OIP.wivQXmKbDLwGLWXKFIXMIwHaD4?w=318&h=180&c=7&o=5&pid=1.7')
  em.set_footer(text="Developed by @hello_worlds")        
  await ctx.send(embed=em)

@bot.command(aliases = ['btc'])
async def BTC(ctx):
  date_time = datetime.now()
  date_time = date_time.strftime('%H:%M:%S')
  CurrentPrice = getPrice('BTC', 'GBP')['GBP']
  await ctx.send(f'The price of 1 Bitcoin is £{CurrentPrice} at {date_time}')

@bot.command(aliases = ['eth'])
async def ETH(ctx):
  date_time = datetime.now()
  date_time = date_time.strftime('%H:%M:%S')
  CurrentPrice = getPrice('ETH', 'GBP')['GBP']
  await ctx.send(f'The price of 1 Bitcoin is £{CurrentPrice} at {date_time}')

@bot.command(aliases = ['buy btc','b-btc'])
async def buy_BTC(ctx):
  data = getData()
  CurrentPrice = getPrice('BTC', 'GBP')['GBP']
  data['BTC_amount'] = CurrentPrice
  data['BTCnum'] += 1
  data['balance'] = data['balance'] - CurrentPrice
  with open('data.json', 'w') as file:
    file.seek(0)
    file.truncate()
    json.dump(data,file,indent = 2)
  print('\nBTC bought successfully')
  await ctx.send(f'You bought 1 fake bitcoin for £{CurrentPrice}.')

@bot.command(aliases = ['buy eth','b-eth'])
async def buy_ETH(ctx):
  data = getData()
  CurrentPrice = getPrice('BTC', 'GBP')['GBP']
  data['ETH_amount'] = CurrentPrice
  data['ETHnum'] += 1
  data['balance'] = data['balance'] - CurrentPrice
  with open('data.json', 'w') as file:
    file.seek(0)
    file.truncate()
    json.dump(data,file,indent = 2)
  print('\nETH bought successfully')
  await ctx.send(f'You bought 1 fake ether for £{CurrentPrice}.')

@bot.command()
async def sell_BTC(ctx):
  data = getData()
  if data['BTCnum'] != 0:
    CurrentPrice = getPrice('BTC', 'GBP')['GBP']
    ProfitLoss = CurrentPrice - data['BTCbuyin']
    ProfitLoss = round(ProfitLoss, 2)
    data['BTCnum'] = data['BTCnum'] - 1
    data['balance'] += CurrentPrice
    with open('data.json','w') as file:
      file.seek(0)
      file.truncate()
      json.dump(data,file,indent = 2)
    print('\nBTC sold successfully')
    await ctx.send(f'You sold 1 fake bitcoin for £{CurrentPrice} which made you {ProfitLoss}.')
  else:
    print('\nERROR: No Bitcoin in wallet')
    await ctx.send(f"You don't have any bitcoins to sell, sorry mate.\nyou can buy some bitcoin using !buy_BTC.")


@bot.command(aliases = ['hi GLaDoS','hi bot','hello bot'])
async def hi_there(ctx):
    if ctx.author.name == 'hello_worlds':
        await ctx.send(f'Greetings Master, thank you for returning to your beloved testing server!')
    else:
        await ctx.send(f'Hey there {ctx.author.name}, welcome to the testing server made by hello_worlds!\nHow are you doing?')

@bot.command(aliases = ['walter wednesday'])
async def wednesday(ctx):
    em = discord.Embed(title="It's that time of the week again!")
    em.set_image(url="https://media1.tenor.com/images/720ec30e99758f06a32e1905f2a9f810/tenor.gif?itemid=22250042")
    await ctx.send(embed=em)
    


bot.run('ODA5NDE5NDA3NTk5NTk5Njc3.YCU0kQ.RZnMIQz53e2WXje3U8PBCwti9xQ')

input()
