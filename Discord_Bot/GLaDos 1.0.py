
import discord, requests
from time import sleep
from discord.ext import commands
from datetime import datetime

global ETH_num
global BTC_num
global my_btc
global my_eth

print('Initializing...') #making console look fancy
sleep(0.5)
print()
print('.')
sleep(0.5)
print()
print('..')
sleep(0.5)
print()
print('...')
print()
client = discord.Client() #setting up discord connection

crypto_URL = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'
bad_words = ['shit', 'fuck', 'bitch', 'Fuck', 'Shit', 'Bitch', 'Stfu', 'dick'] #don't worry, this is to stop naughty people
y = 0

def get_price(coin, currency):
  try:
    response = requests.get(crypto_URL.format(coin, currency)).json()
    return response
  except:
    return False

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="yo mamma's ass"))
  print('''Initialization complete.

The bot the humans call {0.user} is online.'''.format(client))


@client.event
async def on_message(message):
    msg = message.content
    bot_say = message.channel.send
    if message.author == client.user:
        return

    if any(words in msg for words in bad_words) and message.author != 'hello_worlds':
      await bot_say('Mind your language - you have been timed out for 10 seconds.')
      await message.delete()
      await message.channel.set_permissions(message.author, send_messages = False)
      sleep(10)
      await message.channel.set_permissions(message.author, send_messages = True)

    if msg.startswith('!hello'):
      sleep(1)
      await bot_say('Hello!')

    if msg.startswith('Say my name, GLaDos!'):
      sleep(1)
      await bot_say('While I appreciate the Breaking Bad reference, I\'m not gonna say your name because that would break privacy laws.')

    if msg.startswith('!BTC'):
      date_time = datetime.now()
      date_time = date_time.strftime('%H:%M:%S')
      currentPrice = get_price('BTC', 'GBP')
      print(currentPrice)
      await bot_say(f'The price of 1 Bitcoin is £{currentPrice} at {date_time}')
    
    if msg.startswith('!ETH'):
      date_time = datetime.now()
      date_time = date_time.strftime('%H:%M:%S')
      currentPrice = get_price('ETH', 'GBP')
      await bot_say('The price of 1 Ether is £' + str(currentPrice['GBP']) + ' at ' + str(date_time))

    if msg.startswith('!buy ETH'):
        with open('data.txt', 'r+') as test:
          for count in range(0, 5):
            a = test.readline()
            if count == 0:
              balance = a
              balance = float(balance)
            if count == 1:
              BTC_num = a
              BTC_num = int(BTC_num)
            if count == 2:
              ETH_num = a
              ETH_num = int(ETH_num)
            if count == 3:
              BTC_amount = a
              BTC_amount = float(BTC_amount)
            if count == 4:
              ETH_amount = a
              ETH_amount = float(ETH_amount)
          currentPrice = get_price('ETH', 'GBP')
          ETH_amount = currentPrice['GBP']
          balance = float(balance)
          ETH_num = int(ETH_num)
          ETH_num += 1
          balance = balance - currentPrice['GBP']
          test.seek(0)
          test.truncate()
          test.write(str(balance) + '\n' + str(BTC_num) + str(ETH_num))
          print()
          print('ETH bought successfully')
          await bot_say('You bought 1 fake ether for £' + str(currentPrice['GBP']) + '.')

    if msg.startswith('!buy BTC'):
      with open('data.txt', 'r+') as test:
        for count in range(0, 5):
          a = test.readline()
          if count == 0:
            balance = a
            balance = float(balance)
          if count == 1:
            BTC_num = a
            BTC_num = int(BTC_num)
          if count == 2:
            ETH_num = a
            ETH_num = int(ETH_num)
          if count == 3:
            BTC_amount = a
            BTC_amount = float(BTC_amount)
          if count == 4:
            ETH_amount = a
            ETH_amount = float(ETH_amount)
        currentPrice = get_price('BTC', 'GBP')
        BTC_amount = currentPrice['GBP']
        balance = float(balance)
        BTC_num = int(BTC_num)
        BTC_num += 1
        balance = balance - currentPrice['GBP']
        test.seek(0)
        test.truncate()
        test.write(str(balance) + '\n' + str(BTC_num) + '\n' + str(ETH_num) + '\n' + str(BTC_amount) + '\n' + str(ETH_amount))
        print()
        print('BTC bought successfully')
        await bot_say('You bought 1 fake bitcoin for £' + str(currentPrice['GBP']) + '.')

    if msg.startswith('!sell BTC'):
      with open('data.txt', 'r+') as test:
        for count in range(0, 5):
          a = test.readline()
          if count == 0:
            balance = a
            balance = float(balance)
          if count == 1:
            BTC_num = a
            BTC_num = int(BTC_num)
          if count == 2:
            ETH_num = a
            ETH_num = int(ETH_num)
          if count == 3:
            BTC_amount = a
            BTC_amount = float(BTC_amount)
          if count == 4:
            ETH_amount = a
            ETH_amount = float(ETH_amount)
        if BTC_num != 0:
          currentPrice = get_price('BTC', 'GBP')
          ProfitLoss = currentPrice['GBP'] - BTC_amount
          ProfitLoss = round(ProfitLoss, 2)
          BTC_num = BTC_num - 1
          balance += currentPrice['GBP']
          test.seek(0)
          test.truncate()
          test.write(str(balance) + '\n' + str(BTC_num) + '\n' + str(ETH_num) + '\n' + str(BTC_amount) + '\n' + str(ETH_amount))
          print()
          print('BTC sold successfully')
          await bot_say('You sold 1 fake bitcoin for £' + str(currentPrice['GBP']) + ' which made you £' + str(ProfitLoss) + ' of profit/loss. You\'re balance is £' + str(round(balance, 2)))
        else:
          print()
          print('ERROR: No Bitcoin available')
          await bot_say('Sorry buddy, you don\'t have any bitcoin to sell.\n If you want to get some fake bitcoin, type in !buy BTC.')

    if msg.startswith('!sell ETH'):
      with open('data.txt', 'r+') as test:
        for count in range(0, 5):
          a = test.readline()
          if count == 0:
            balance = a
            balance = float(balance)
          if count == 1:
            BTC_num = a
            BTC_num = int(BTC_num)
          if count == 2:
            ETH_num = a
            ETH_num = int(ETH_num)
          if count == 3:
            BTC_amount = a
            BTC_amount = float(BTC_amount)
          if count == 4:
            ETH_amount = a
            ETH_amount = float(ETH_amount)
        if ETH_num != 0:
          currentPrice = get_price('ETH', 'GBP')
          ProfitLoss = currentPrice['GBP'] - ETH_amount
          ProfitLoss = round(ProfitLoss, 2)
          ETH_num = ETH_num - 1
          balance += currentPrice['GBP']
          test.seek(0)
          test.truncate()
          test.write(str(balance) + '\n' + str(BTC_num) + '\n' + str(ETH_num) + '\n' + str(BTC_amount) + '\n' + str(ETH_amount))
          print()
          print('ETH sold successfully')
          await bot_say('You sold 1 fake ether for £' + str(currentPrice['GBP']), 'which made you £' + str(ProfitLoss), ' of profit/loss. You\'re balance is £' + str(balance))
        else:
          await bot_say('Sorry buddy, you don\'t have any etherium to sell.\n If you want to get some fake etherium, type in !buy ETH.')

    if msg.startswith('!balance'):
      with open('data.txt', 'r+') as test:
        balance_list = test.read()
        balance_list[0] = round(balance_list[0], 2)
      await bot_say('You have ' + str(balance_list[1]) +' bitcoins and ' + str(balance_list[2]) + ' ethers.')
      if balance_list[0] <= 0:
        await bot_say('You\'re balance is currently £' + str(balance_list[0]))
      if balance_list[0] > 0:
        await bot_say('You\'re balance is currently £' + str(balance_list[0]) + ', keep the cash money flowing, big man!')
      
    if msg.startswith('!reset'):
      await bot_say('\nDo you wish to reset your balance? \nThis cannot be reversed, be careful!')
      print()
      reset = str(input('A balance reset request has been placed! Reset balance?\n'))
      if reset == 'yes':
        with open('data.txt', 'r+') as test:
          balance_list = test.read()
          test.seek(0)
          test.truncate()
          balance_list[0] = 0
          test.write(str(balance_list))
          print()
          print('Balance Reset')
          await bot_say('OK, I have reset your balance back to 0.') 
      else:
        await bot_say('OK, your balance hasn\'t been reset.')

client.run('ODA5NDE5NDA3NTk5NTk5Njc3.YCU0kQ.RZnMIQz53e2WXje3U8PBCwti9xQ')

input()
