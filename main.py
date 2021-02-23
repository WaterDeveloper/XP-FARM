# CONFIG
token = "TOKEN" # Pesquise no google como achar isso.
prefix = "!"



import asyncio
from discord.ext import commands
import discord
import random
import re

print("Loading..")

words = ['esse jogo é legal', 'nice client', 'alguem quer duo plat', '.', 'alguem pode me ajuda?', 'como assim', 'entendi', 'oi', 'obrigado', 'desculpa', 'sério?', 'pq eu n consigo entrar no lol?', 'ele morreu e falou: Eh o grongos', 'alguem pode me doar rp?', 'n consigo falar no chat do lol', 'pq eu ganhei pouco pdl?', 'não entendi', 'saquei', 'kkkkkkkkk', 'boa man', 'diga não aos discord modificados', 'impossivel jogar lol vei', 'pq n respondem?', 'sou eu', 'oq é gankar?', 'dsclp sou novo', 'kkkkkk (rindo de nervoser)', 'escutem K/DA galera', 'sério cara?', 'pq isso man? calma drill!', 'Oieee', 'Oi, meu nome é pedro sou ferro e éh isso', 'impossivel vey', 'hj n', 'yone mt op lek', 'eh de f3d3er', 'queue de ferro = pouco pdl', 'tá f0d4', 'algm duo?', 'fleex agr go', '#GOpaiN', '#GOFLA', '#GOKabuM!', 'é o grongos', 'só a cabecinha', 'só darius abuser nisso, credo.', 'darius tá mt forte cara', 'tinowns pernas de camille', '4lan mão fofa', 'só o básico hehe', 'cheio de tóxico no lol credo', 'jogar lol é frustante lek', 'bruh ;-;', 'carroça', 'tá tendo uns drop insano ultimamente hein', 'muito massa o teemo', 'é dahora de jogar de irelia man', 'cabei de feedar de yasuo kkk', 'aphelios é legal?']

#   Count bot config
counting_channel = 718190688356794418 #	ID do canal
enabled = True
last_number = 0



bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot Loaded.")

@bot.command()
async def farm(ctx, amount=10):
    await ctx.message.delete()
    for r in range(amount):
        message = await ctx.send(random.choice(words))
        await asyncio.sleep(random.uniform(0,3))
        await message.delete()
        await asyncio.sleep(random.uniform(61,65))

@bot.command()
async def count(ctx, option='on'):
    global enabled
    if option.lower() == 'on':
        await ctx.send('Counting Enabled..')
        enabled = True
    elif option.lower() == 'off':
        await ctx.send('Counting Disabled..')
        enabled = False
    elif option.lower() == 'reset':
        global last_number
        last_number = 0
        await ctx.send('Count variable reset.')
    else:
        await ctx.send('Counting Disabled..')

@bot.event
async def on_message(message):
    global last_number
    global enabled
    if bot.user.id != message.author.id and message.channel.id == int(counting_channel) and enabled:
        channel = bot.get_channel(int(counting_channel))
        try:
            number = int(re.search(r"(\d*)", message.content).group(0))
        except:
            pass
        else:
            if number == last_number + 1 or last_number == 0:
                async with message.channel.typing():
                    last_number = number + 1
                    print(f"Sending -> {number+1}")
                    await asyncio.sleep(random.uniform(0, 2))
                    await channel.send(number+1)
    await bot.process_commands(message)





bot.run(token, bot=False)  
