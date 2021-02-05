#This my bot, named JoshuaPBot

import discord  # connects to discord server
from discord.ext import commands
import requests # requests data from the API
import os # gets the discord key
import asyncio # figure out why this cannot be imported
import datetime
#import twelvedata
#from twelvedata import TDClient

'''
import datetime
import numpy
import twelvedata 
from twelvedata import TDClient
from time import time, sleep
import pandas as pd
'''
#import matplotlib.pyplot as plt
#from pandas_datareader import data as web

#https://twelvedata.com/docs#getting-started
#Xignite
#AlphaVantage
#IEXCloud

'''
The following row occurs at the end of every day
Row 1: (Date)   (Total Amount Made) (Total fees)    (Total Amount Made(with fees taken out))    (Percentage made(so total amount in the bank from today divided by the total amount in the bank from yesterday))
An example is if I made $1,000 today, and my total is now $11,000, I would make
The following 3 rows happen for each trade
Row 1: (time)   (Stock Name)  (Stock Amount)  (Buy Price (the ask amount)(put the actual price in brackets))
Row 2: (time)   (Stock Name)  (Stock Amount)  (Selling Price(the buy amount)(put the actual price in brackets))
Row 3: (Money Made) (Fees)  (Money Made minus fees)
Note: Fees are $9.99 for each buy and $9.99 for each sell. Also, $29.99 + GST (so $33.8887) after every month for TD Dashboard. If you get 30 or above trades in 1 quarter (a.k.a. 3 months), or if you have $500,000 or more with TD, then the fees are gone.
In a different file, there will be
Note: the day and all time ones occur every day while the week, month, and year occur on their respective times (e.g. the week one is shown at the end of the week)
After each day: (Date)   (Total Amount Made) (Total fees)    (Total Amount Made(with fees taken out))    (Percentage made(so total amount in the bank from today divided by the total amount in the bank from yesterday))
After all time: (Date)   (Total Amount Made) (Total fees)    (Total Amount Made(with fees taken out))    (Percentage made(so total amount in the bank from right now divided by the starting amount which is currently $10,000))
After each week: (Date)   (Total Amount Made) (Total fees)    (Total Amount Made(with fees taken out))    (Percentage made(so total amount in the bank from this week divided by the total amount in the bank from last week))
After each month: (Date)   (Total Amount Made) (Total fees)    (Total Amount Made(with fees taken out))    (Percentage made(so total amount in the bank from this month divided by the total amount in the bank from last month))
After each year: (Date)   (Total Amount Made) (Total fees)    (Total Amount Made(with fees taken out))    (Percentage made(so total amount in the bank from this year divided by the total amount in the bank from last year))
'''
'''
Things to do:
 *   Convert the APIs to something better, add an API for cryptocurrencies
 *   Figure out how to run the loop every minute
 *   Add a "stock" class
 *   Add a "shortSell" class
 *   Add a "trade" class
 *   Add diversification (allow the bot to have multiple positions, like multiple stocks)
 *   Use files, like have a file that reads and writes the balance, and have another file for all of the trades, so their dates, buy/sell or sell/buy prices, etc
 *   Maybe have a website or something other than Discord to access it
 *   Add better info on financial instruments
 *   Convert to a websocket for lower latency, or at least have a loop that gets data every minute
 *   Use machine learning for better algorithms (so have 2 programs, one that runs in the background and creates an algorithm for tomorrow and another one that does the actual trading using the algorithm from yesterday, and maybe connect them with a websocket
 *   Convert to a faster language (right now, I think C++)
 *   Make the program use something (like the Robot class in Java) to make actual buy and sells
 *   Try not to use the entire money on a stock (e.g. if you ahve $10k, spend 1/3 on MSFT)
 *   Convert to getting data every second or tick (so a wired connection would be needed)
'''
#https://tradingstrategyguides.com/best-combination-of-technical-indicators/
#https://realpython.com/async-io-python/
#https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
#https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client#:~:text=If%20you%20simply%20want%20your,means%2C%20use%20the%20base%20Client%20.
#https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
#https://discordpy.readthedocs.io/en/latest/
#https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/
#https://medium.com/python-in-plain-english/how-to-change-discord-bot-status-with-discord-py-39219c8fceea
#https://stackoverflow.com/questions/59126137/how-to-change-discord-py-bot-activity
#https://gist.github.com/4Kaylum/a1e9f31c31b17386c36f017d3c59cdcc
#https://stackoverflow.com/questions/46307035/latency-command-in-discord-py
#https://www.w3schools.com/python/python_try_except.asp             I mixed this up with the try catch from Java, so that's why I needed this
#https://realpython.com/how-to-make-a-discord-bot-python/#checking-command-predicates
#https://stackoverflow.com/questions/59255799/trying-to-send-a-message-to-a-specific-channel-using-discord-py-rewrite-and-it-i
#https://www.home-assistant.io/integrations/discord/#:~:text=In%20The%20Discord%20application%20go,channel%20ID%20(Copy%20ID).
#https://medium.com/better-programming/how-to-make-discord-bot-commands-in-python-2cae39cbfd55
#https://www.investopedia.com/terms/i/ichimoku-cloud.asp#:~:text=The%20Ichimoku%20Cloud%20is%20a,plotting%20them%20on%20the%20chart.
#https://school.stockcharts.com/doku.php?id=technical_indicators:ichimoku_cloud
#https://forextraininggroup.com/how-to-use-ichimoku-cloud-strategies-to-trade-forex/
#https://twelvedata.com/docs#getting-started
#https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository
#https://docs.github.com/en/github/using-git/adding-a-remote
#https://www.atlassian.com/git/tutorials/syncing/git-pull#:~:text=The%20git%20pull%20command%20is,Git%2Dbased%20collaboration%20work%20flows.
#https://docs.python.org/3/library/asyncio-task.html
#https://www.diffchecker.com/
#https://jsonformatter.org/
#Paul Lee

bot = commands.Bot(command_prefix = ";")
security = 'MSFT'
#td = TDClient(apikey=os.environ['TWELVE_DATA_TOKEN'])
choice = 0


@bot.event
async def on_ready():  # runs when bot connects to discord, says that it is logged in
    await bot.change_presence(activity=discord.Game(name="games with my life"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


"""
async def position(ctx):  # sees the message in the chat
    await bot.wait_until_ready()
    channel = bot.get_channel(785190821997576257) # replace with channel ID that you want to send to

    while True:
        if choice == -1:
            await channel.send('sell')
        elif choice == 1:
            await channel.send('buy')
        elif choice == 0:
            await channel.send('hodl')

    await asyncio.sleep(1)
"""

async def Ichimoku ():
    #await bot.wait_until_ready()

    channel = bot.get_channel(785190821997576257) # replace with channel ID that you want to send to

    data = requests.get('https://api.twelvedata.com/ichimoku?symbol=' + security + '&conversion_line_period=150&base_line_period=150&lagging_span_period=1&leading_span_b_period=60&interval=1min&outputsize=1&apikey=' + os.environ['TWELVE_DATA_TOKEN']).json()
    
    global SenkouA
    SenkouA = float(data['values'][0]['senkou_span_a'])

    global SenkouB
    SenkouB = float(data['values'][0]['senkou_span_b'])

    if SenkouA > SenkouB:
        await channel.send("sell")
    elif SenkouA < SenkouB:
        await channel.send("buy")

    await asyncio.sleep(60)

@bot.command(name = 'stock')
async def stock (ctx, arg1):

    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return

    global security
    security = arg1

@bot.command(name = 'decision')
async def decision (ctx, arg1):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return

    try:
        data = requests.get('https://api.twelvedata.com/ichimoku?symbol=' + arg1 + '&conversion_line_period=150&base_line_period=150&lagging_span_period=1&leading_span_b_period=60&interval=1min&outputsize=1&apikey=' + os.environ['TWELVE_DATA_TOKEN']).json()

        SenkouATemp = float(data['values'][0]['senkou_span_a'])

        SenkouBTemp = float(data['values'][0]['senkou_span_b'])

        if SenkouATemp > SenkouBTemp:
            await ctx.channel.send("sell")
        elif SenkouATemp < SenkouBTemp:
            await ctx.channel.send("buy")
        else:
            await ctx.channel.send("hold")
    except:
        await ctx.channel.send("Please enter the ticker name of the security, such as MSFT for Microsoft. Note: allowing other types such as cryptocurrencies, indexes, etc. will come soon)")
        await ctx.channel.send("An example would be: .decision MSFT")

@bot.command(name = 'hello')
async def hello (ctx, *args):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return

    await ctx.send(ctx.message.content)

@bot.command(name = 'ping')
async def ping(ctx):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return

    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@bot.command(name = 'comic')
async def comic (ctx):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return

    #--------------------sends a random comic----------------------------
    data = requests.get(
    'https://c.xkcd.com/random/comic/')  # fetches random comic
    data = requests.get(
    'https://xkcd.com/' + data.url[17:-1] +
    '/info.0.json').json()  # fetches the json data + the comic number
    await ctx.send(data["img"])  # sends the actual image

@bot.command(name = 'yesno')
async def yesno (ctx):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return
        
    #--------------------sends either yes or no-----------------------------
    data = requests.get(
        'https://yesno.wtf/api')  # fetches the yes/no json data
    await ctx.send(data.json()["image"])  # sends the image

@bot.command(name = 'anime')
async def anime (ctx):
    try:
        # we do not want the bot to reply to itself
        if ctx.author.id == bot.user.id:  # checks if the message is from itself
            return
            
        #--------------sends a random anime picture-----------------------------
        response = requests.get('https://kitsu.io/api/edge/anime'
                                )  # fetches the yes/no json data
        data = response.json()['data']
        anime = random.choice(data)
        await ctx.send(data.json()["image"])  # sends the image
    except:
        await ctx.send("Please try again alter because this part is in process. Sorry for the inconvenice.")

@bot.command(name = 'hatelaptops')
async def hatelaptops (ctx):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return
        
    #--------------sends a hate message towards gaming laptops-------------------
    await ctx.send(
        "Today when I walked into my economics class I saw    something I dread every time I close my eyes. Someone had brought their new gaming laptop to class. The Forklift he used to bring it was still running idle at the back. I started sweating as I sat down and gazed over at the 700lb beast that was his laptop. He had already reinforced his desk with steel support beams and was in the process of finding an outlet for a power cable thicker than Amy Schumer's thigh. I start shaking. I keep telling myself I'm going to be alright and that there's nothing to worry about. He somehow finds a fucking outlet. Tears are running down my cheeks as I send my last texts to my family saying I love them. The teacher starts the lecture, and the student turns his laptop on. The colored lights on his RGB Backlit keyboard flare to life like a nuclear flash, and a deep humming fills my ears and shakes my very soul. The entire city power grid goes dark. The classroom begins to shake as the massive fans begin to spin. In mere seconds my world has gone from vibrant life, to a dark, earth shattering void where my body is getting torn apart by the 150mph gale force winds and the 500 decibel groan of the cooling fans. As my body finally surrenders, I weep, as my school and my city go under. I fucking hate gaming laptops."
    )

@bot.command(name = 'ree')
async def ree (ctx):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return
        
    #------------------sends ree-------------------------------------------
    await ctx.send("ree")

@bot.command(name = 'add')
async def add (ctx):
    # we do not want the bot to reply to itself
    if ctx.author.id == bot.user.id:  # checks if the message is from itself
        return
        
    #---------------------sends the addition of two inputted numbers--------------
    #await message.channel.send('Die!')
    #print("hi")
    data = ctx.message.content[5:]  # gets the content from the message
    try:
        ans = int(data.split(" ")[0]) + int(data.split(" ")[1])
        await ctx.send(ans)
    except:
        await ctx.send("Please enter an integer")
        # await means that it waits for the async command to stop, allows multiple users to use the bot at once
        # if the bot is waiting for a response from the HTTP website, then async (a.k.a a coroutine) allows it to submit a request, like a request to the website, and then do other work in the queue, like reading the chat, while waiting for the HTTP website to respond
        # await tells the code that it is waiting for it to be run, which is useful in async - https://docs.python.org/3/library/asyncio-task.html, https://stackabuse.com/python-async-await-tutorial/
        # the main idea is if statement for commands in the chat, then fetch the data from the source, then send it to the chat

bot.loop.create_task(Ichimoku())
bot.run(os.environ['DISCORD_TOKEN'])
