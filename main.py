print("File main.py found")

# Update testing
from time import sleep
import re
import random
import io
import json
import sys
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import imageio
from better_profanity import profanity
import colorama
from colorama import Fore
import discord
from requests import get
from discord.ext import commands
from PyDictionary import PyDictionary as PD
from os.path import join as path
from os.path import expanduser
import os
import subprocess
import sys
from pprint import pprint
sys.path.insert(1, expanduser("~"))
from config import *

colorama.init(autoreset=True)
rofl = "🤣"
neutral = "😐"
among_us = r"‼️‼️HOLY FUCKING SHIT‼️‼️‼️‼️ IS THAT A MOTHERFUCKING AMONG US REFERENCE??????!!!!!!!!!!11!1!1!1!1!1!1! 😱😱😱😱😱😱😱 AMONG US IS THE BEST FUCKING GAME 🔥🔥🔥🔥💯💯💯💯 RED IS SO SUSSSSS 🕵️🕵️🕵️🕵️🕵️🕵️🕵️🟥🟥🟥🟥🟥 COME TO MEDBAY AND WATCH ME SCAN 🏥🏥🏥🏥🏥🏥🏥🏥 🏥🏥🏥🏥 WHY IS NO ONE FIXING O2 🤬😡🤬😡🤬😡🤬🤬😡🤬🤬😡 OH YOUR CREWMATE? NAME EVERY TASK 🔫😠🔫😠🔫😠🔫😠🔫😠 Where Any sus!❓ ❓ Where!❓ ❓ Where! Any sus!❓ Where! ❓ Any sus!❓ ❓ Any sus! ❓ ❓ ❓ ❓ Where!Where!Where! Any sus!Where!Any sus Where!❓ Where! ❓ Where!Any sus❓ ❓ Any sus! ❓ ❓ ❓ ❓ ❓ ❓ Where! ❓ Where! ❓ Any sus!❓ ❓ ❓ ❓ Any sus! ❓ ❓ Where!❓ Any sus! ❓ ❓ Where!❓ ❓ Where! ❓ Where!Where! ❓ ❓ ❓ ❓ ❓ ❓ ❓ Any sus!❓ ❓ ❓ Any sus!❓ ❓ ❓ ❓ Where! ❓ Where! Where!Any sus!Where! Where! ❓ ❓ ❓ ❓ ❓ ❓ I think it was purple!👀👀👀👀👀👀👀👀👀👀It wasnt me I was in vents!!!!!!!!!!!!!!😂🤣😂🤣😂🤣😂😂😂🤣🤣🤣😂😂😂 r/amongusmemes r/unexpectedamongus r/expectedamongus perfectly balanced as all things should be r/unexpectedthanos r/expectedthanos for balance HOLY SHIT DID YOU JUST SAY THE WORD SUS???😳1?/1😱//1😳/1111!!!! Wait, you don't know what it is from?😳😳😳Let 👆give you a brief r/history. 📚📚📚👨‍🚀If you didn't r/knowyourshit, the r/term sus(suspicious) is a saying from the r/popular r/game r/AmongUs. Among us is so fun😔 👉👈, don't insult it, every youtuber and streamer says so!!!!!!!11 Corpses voice is so deep am i right or am i right😳😳????? I mean Mr beast and Dream play and pull big 🧠 1000000000000 iq moves in their videos..... YOU WERE THE IMPOSTER.... ඞ ඞ ඞ Get it because you don't know what sus means? r/stupidquestions r/youranidot r/stupidcuck. I CAnT BELEeVE YOUU dont KNoW WHT SUS MeaNS?/??!??!?!!🖕🖕🖕🖕🖕 Man why do i have to r/explain this to a r/idiot🤪🤪🤪📚📚📚... Sus is a GREAT WORD from a GREAT VIDEO GAME. in class, YOU CAN PLAY IT ON YOUR PHONE😜😜😜😜😜😜**??!?!?** such a masterpiece... FOR THE GREAT PRICE OF FREE!!!11!💰💰🤑🤑🤑🤑😜😜😜💰💰 It can also mean gay 😳😳😳😳"


# I N I T I A L I Z A T I O N
# text files
with open(path(root, "settings", "blacklist.txt"), "r") as f:
    blacklist = f.read().splitlines()
with open(path(root, "settings", "whitelist.txt"), "r") as f:
    whitelist = f.read().splitlines()

print("Text files loaded")

# constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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

debugstate = False # Not a CONSTANT

# start
bot = commands.Bot(command_prefix="!",
                   owner_id=owner_id,
                   help_command=None,
                   activity=discord.Game(name="with your mom"),
                   intents=discord.Intents.all())
print("Client set up")


# C U S T O M
def getcontent(url):
    return get(url).content


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
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount + 1)


@bot.command(brief="Kicks a user")
@commands.is_owner()
async def kick(ctx, user: discord.Member, reason):
    await user.kick(reason=reason)


# commands available to everyone
@bot.command(brief="Shh...")
async def rickroll(ctx):
    await ctx.send(file=discord.File(path(f"{root}/assets", "rickroll.gif")))

@bot.command(brief="Shh...")
async def ohno(ctx):
    await ctx.send(file=discord.File(path(f"{root}/assets", "walter-white-falling.gif")))

@bot.command(brief="Shh...")
async def whoasked(ctx):
    await ctx.send(file=discord.File(path("root", "assets", "skeletons.gif")))

@bot.command(brief="Shh...")
async def pog(ctx):
    await ctx.send(file=discord.File(path("root", "assets", "pog.png")))

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


@bot.command(brief="Writes text to a meme")
async def meme(ctx, text, color=None):
    try:
        img_url = img_url = ctx.message.attachments[0].url
    except IndexError:
        await ctx.send("Please input an image")
    else:
        if color is None:
            color = "black"
        await ctx.channel.purge(limit=1)
        # load the passed image
        img = PIL.Image.open(io.BytesIO(getcontent(img_url)))
        # get image size
        img_width, img_height = img.size
        # init font
        font = PIL.ImageFont.truetype(path(root, "assets", "Roboto", "Roboto-Medium.ttf"), 60)
        # create empty text image and render onto it
        _, _, fw, fh = font.getbbox(text)
        fw = int(fw * 0.75)
        fh = int(fh * 0.75)
        text_img = PIL.Image.new("RGBA", (fw, fh))
        draw = PIL.ImageDraw.Draw(text_img)
        draw.text((img.width / 2 - fw / 2, 10), text, color, font=font)
        # save and message the image
        img_path = f"{root}{text}.png"
        text_img.save(img_path)
        message = await ctx.send(file=discord.File(img_path, "meme.png"))
        os.remove(img_path)


# E V E N T S
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pattern = 'Command "(.*?)" is not found'
        await ctx.send(f"Unknown command _{re.search(pattern, str(error)).group(1)}_")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("You have no permission to invoke this command.")
    else:
        await ctx.send(repr(error))
        print(repr(error))


@bot.event
async def on_ready():
    text = f"{bot.user} is online!"
    print(Fore.GREEN + text)


# profanity check
@bot.event
async def on_message(msg):
    if msg.author.id == bot.user.id:
        return
    c = msg.content
    if profanity.contains_profanity(c):
        await msg.channel.send("Language")
    if c.lower() == "sus":
        await msg.channel.send(among_us)
    await bot.process_commands(msg)

# D O N ' T  C H A N G E
@bot.command(brief="Updates the bot")
async def update(ctx):
    await ctx.send("Restarting services...")
    subprocess.run(["rm", "-rf", root])
    subprocess.run(["git", "clone", "https://github.com/LMCuber/CaeborgDiscordBot", root])
    await ctx.send("Regenerated code base...")
    subprocess.run(["sudo", "-n", "systemctl", "restart", "caeborg"])
    await ctx.send("Update complete.")


@bot.command(aliases=["poweroff"], brief="Shuts down the server")
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    subprocess.run(["sudo", "-n", "systemctl", "poweroff"])
    await ctx.send("Shutting down complete")

@bot.command(alias=["debug"], brief="Enters debug mode and enables journal printing")
async def debug(ctx):
    global debugstate
    if debugstate:
        debugstate = False
        await ctx.send("Disabled debug mode.")
    else:
        debugstate = True
        await ctx.send("Enabled debug mode.")
        while debugstate:
            # await ctx.send(subprocess.run(["journalctl", "--no-pager", "-n", "1", "|", "grep", "-Ev", "'(GMT|BST)'"], capture_output=True))
            # sleep(0.5)
            await ctx.send(subprocess.check_output(["journalctl", "--no-pager", "-n", "1", "|", "grep", "-Ev", "'(GMT|BST)'"]))
        

bot.run(token)
