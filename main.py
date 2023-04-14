print("File main.py found")


import re
import random
import io
import json
import sys
import PIL.Image
from better_profanity import profanity
import colorama
from colorama import Fore
import discord
from requests import get
from discord.ext import commands
from PyDictionary import PyDictionary as PD
from os.path import join as path
import os


colorama.init(autoreset=True)
rofl = "🤣"
neutral = "😐"
root = "/home/dt/git/CaeborgDiscordBot"


# I N I T I A L I Z A T I O N
# text files
with open(f"{root}specs.json", "r") as f:
    j = json.loads(f.read())
    token = j["token"]
    owner_id = j["owner id"]
with open(f"{root}blacklist.txt", "r") as f:
    blacklist = f.read().splitlines()
with open(f"{root}whitelist.txt", "r") as f:
    whitelist = f.read().splitlines()

print("Text files loaded")

# constants
profanity.load_censor_words(whitelist_words=whitelist)
profanity.add_censor_words(blacklist)
inspq_url = r"https://zenquotes.io/api/random"
quote_url = r"https://inspirobot.me/api?generate=true"
dict_url = r"https://api.urbandictionary.com/v0/define?term="
eq_url = r"https://mathsolver.microsoft.com/en/solve-problem/"
weather_url = r"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=46d89a681ca693f0ad27e2059dca0c6a"
lidwoord_url = r"https://welklidwoord.nl/"
wiki_url = r"https://en.wikipedia.org/wiki/Special:Random"
spanish_url = r"https://www.spanishdict.com/conjugate/{verb}"
chem_url = r"https://opsin.ch.cam.ac.uk/opsin/"

conn_error = "Sorry, cannot send a request. Your server admin has probably blocked it or you're not connected to the internet."

# start
bot = commands.Bot(command_prefix="!",
                   owner_id=owner_id,
                   help_command=None,
                   activity=discord.Game(name="with your mom"))
print("Client set up")


# C U S T O M
def gettext(url):
    return get(url).text


def str_user(user):
    return str(user).split("#")[0]


def get_ascii(pil_img, chars=('.', ',', ':', ';', '+', '*', '?', '%', '&', 'S', '@')):
    hl = 30
    vl = hl
    img = pil_img.resize((vl, hl))
    d = list(img.getdata())
    ascii = [chars[int(sum(data[:3]) / 3 / 25)] + ("\n" if index % hl == 0 else "") for index, data in enumerate(d, 1)]
    return "".join(ascii)


def no_link(str_):
    return str_.replace("[", "").replace("]", "")


def command_data(command):
    return ([str(command)] if not str(command).startswith("_") else []) + [alias for alias in command.aliases]


# C O M M A N D S
# my commands
@bot.command(brief=("Deletes the [:-n]th messages"))
@commands.is_owner()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)


@bot.command(brief="Kicks a user")
@commands.is_owner()
async def kick(ctx, user: discord.Member, reason):
    await user.kick(reason=reason)


# commands available to everyone
@bot.command(brief="Shh...")
async def rickroll(ctx):
    await ctx.send(file=discord.File(path("assets", "rickroll.gif")))

@bot.command(brief="Calls this command")
async def help(ctx, strcommand=None):
    await ctx.send("```" + "\n".join(sorted([", ".join(command_data(command)) + " | " + (command.brief if command.brief is not None else "") for command in bot.commands if (str(command).lstrip("_") if strcommand is not None else strcommand) == strcommand])) + "```")


@bot.command(aliases=["lidwoord"], brief="Gets whether noun is 'de' or 'het'")
async def deofhet(ctx, noun):
    content = gettext(lidwoord_url + noun)
    await ctx.send(f'_{re.search(f"In de Nederlandse taal gebruiken wij (.*?) {noun}", content).group(1)}_ {noun}')


@bot.command(brief="Gets the latency of the bot (ping) in milliseconds")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.command(brief="Gets the 4-hourly weather forecast of the given city")
async def weather(ctx, city):
    j = json.loads(gettext(weather_url.replace("{city}", city)))
    try:
        wtype = j["weather"][0]["description"]
    except KeyError:
        await ctx.send(f"Unkown city or place _{city}_")
    else:
        temp = j["main"]["temp"]
        fltemp = j["main"]["feels_like"]
        hum = j["main"]["humidity"]
        await ctx.send(f"Weather: {wtype}")
        await ctx.send(f"Temperature: {int(temp - 272.15)}°C (Feels like {int(fltemp - 272.15)}°C)")
        await ctx.send(f"Humidity: {hum}%")


@bot.command(aliases=["ascii"], brief="Converts image to ascii text")
async def _ascii(ctx):
    try:
        img_url = ctx.message.attachments[0].url
    except IndexError:
        await ctx.send("Please send an attachment with the command.")
    else:
        await ctx.channel.purge(limit=1)
        b = gettext(img_url).content
        await ctx.send(f"`{get_ascii(PIL.Image.open(io.BytesIO(b)))}`")


@bot.command(brief="Defines the given word ;)")
async def define(ctx, word):
    try:
        r = gettext(dict_url + word)
    except ConnectionError:
        await ctx.send(conn_error)
    else:
        c = r
        j = json.loads(c)
        _d = random.choice(j["list"])
        d = no_link(_d["definition"])
        e = no_link(_d["example"])
        await ctx.send(d + "\n")
        await ctx.send(f"_{e}_")


@bot.command(aliases=["inspirational-quote"], brief="Generates an inspirational quote")
async def quote(ctx, *args):
    """
    response = gettext(inspq_url)
    json_data = json.loads(response)
    quote = json_data[0]["q"]
    await ctx.send(quote)
    """
    img_url = gettext(quote_url)
    img_content = get(img_url).content
    img_bytes = io.BytesIO(img_content)
    message = await ctx.send(file=discord.File(img_bytes, "quote.png"))
    await message.add_reaction(rofl)
    await message.add_reaction(neutral)


@bot.command(brief="Spanish conjugation of verb in present form")
async def spanish(ctx, verb):
    text = gettext(spanish_url.replace("{verb}", verb))
    pattern = '"word":(.*?)",'
    conjgs = [c[1:] for c in re.findall(pattern, text)[3:9]]
    prons = ("Yo", "Tú", "Él/Ella/Usted", "Nosotros", "Vosotros", "Ellos/Ellas/Ustedes")
    max_chars = 0
    for p, c in zip(prons, conjgs):
        l = len(f"{p} {c}")
        if l > max_chars:
            max_chars = l
    for p, c in zip(prons, conjgs):
        l = len(f"{p} {c}")
        await ctx.send(f"`{p}{' ' * (max_chars - l + 1)}{c}`")


@bot.command(brief="Returns the image of an organic compound, derived from the IUPAC name")
async def chem(ctx, *names):
    name = " ".join(names)
    response = get(f"{chem_url}{name}.png")
    img_content = response.content
    img_text = response.text
    if "OPSIN" in img_text:
        await ctx.send(img_text.replace(name, f"_{name}_"))
    else:
        img_bytes = io.BytesIO(img_content)
        message = await ctx.send(file=discord.File(img_bytes, "chem.png"))


# E V E N T S
@bot.event
async def on_command_error(ctx, error):
    print(type(error))
    if isinstance(error, commands.CommandNotFound):
        pattern = 'Command "(.*?)" is not found'
        await ctx.send(f"Unknown command _{re.search(pattern, str(error)).group(1)}_")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("You have no permission to invoke this command.")
    else:
        print(error)


@bot.event
async def on_ready():
    print(Fore.GREEN + f"{bot.user} is online!")


# profanity check
@bot.event
async def on_message(msg):
    if msg.author.id == bot.user.id:
        return
    c = msg.content
    if profanity.contains_profanity(c):
        await msg.channel.send("Language")
    await bot.process_commands(msg)


bot.run(token)
