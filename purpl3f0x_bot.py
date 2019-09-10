# Import the required libraries

import discord
import hashlib
import base64
import random
import time


from discord.ext import commands

description = 'Bot made by purpl3f0x'
bot_prefix = 'f.'

client = commands.Bot(description=description, command_prefix=bot_prefix)


# Prints info to the command line
# Verifies successful connection to Discord
@client.event
async def on_ready():
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)
    for server in client.servers:  # List connected servers
        print('Joined: {}'.format(server.name))

choices = [
        "💜**Definitely!**💜",
        "🦊**Maybe**🦊",
        "🚫**No**🚫",
        "❔**I don't know**🦊",
        "⛔**Never**⛔",
        "🔥**Hell no**🛑",
        "🦊**Fuck yea!**🦊",
        "🕳*Fox stuck in hole, try again later*🦊",
        "👍**Very likely~**🦊",
        "🛑**I don't think so**🛑"
]

# Array for fact command
facts = [
        "Foxes are without a doubt the sneakiest little fuckers in the entire animal kingdom.",
        "Foxes skulk around doing all kinds of dodgy shit far more than any other species.",
        "Foxes are quick to recognize lewdness.",
        "A female fox is called a vixen, and a male fox is called a dog fox or a tod.",
        "Foxes are loners except during mating season.",
        "Like cats, foxes are most active at night, and their eyes narrow into vertical slits.",
        "Foxes harness the earth's magnetic field to hunt.",
        "Foxes are good parents, caring for their pups for 7 months and going to great lengths to protect them.",
        "Having pet foxes is legal in certain states, some of which require permits.",
        "Arctic foxes don't feel cold until -94F/-70C.",
        "Foxes make 40 different sounds, the most startling of which is its scream.",
        "Foxes have understood the universe for many years.",
        "Foxes eat nothing but grapes.🍇",
        "Foxes will inherit the earth after puny fur-less humans die off in the next ice age.",
        "Foxes are not amused by 'What Does The Fox Say' so don't make that joke around them.",
        "Foxes are prone to pinching the booty.",
        "Foxes will drink your pepsi and call you a bitch.",
        "Foxes fancy the color purple the most."
]


# Commands start here
# Basic info command

@client.command(pass_context=True)
async def info(ctx):
    await client.say("purpl3f0x's bot\n"
                    "Author: **Grey Peterson aka purpl3f0x**, with contributions from **Rorroh**\n"
                    "Written in **Python 3.6**\n"
                    "Github: https://github.com/purpl3-f0x\n"
                    "For a list of current commands type `f.commands`\n"
                    "Note: This bot is experimental and is often offline.")

# Help command

@client.command(pass_context=True)
async def commands(ctx):
    await client.say("***List of commands:***\n"
                    "`f.md5 <text>` - Calculate an MD5 hash\n"
                    "`f.sha1 <text>` - Calculate a SHA1 hash\n"
                    "`f.sha256 <text>` - Calculate a SHA256 hash\n"
                    "`f.b64encode <text>` - Encode text with Base64\n"
                    "`f.b64decode <b64 encoded text>` - Decode Base64\n"
                    "**Fun:**\n"
                    "`f.fact` - Random fox facts!\n"
                    "`f.magicball` - Ask the fox a question!"
                    )

# Begin cryptography commands
# Hashing commands

@client.command(pass_context=True)
async def md5(ctx):
    params = ctx.message.content.split()[1:]
    message = ' '.join(params)

    await client.say(hashlib.md5(message.encode('utf-8')).hexdigest())

@client.command(pass_context=True)
async def sha1(ctx):
    params = ctx.message.content.split()[1:]
    message = ' '.join(params)

    await client.say(hashlib.sha1(message.encode('utf-8')).hexdigest())

@client.command(pass_context=True)
async def sha256(ctx):
    params = ctx.message.content.split()[1:]
    message = ' '.join(params)

    await client.say(hashlib.sha256(message.encode('utf-8')).hexdigest())

# Base64 commands

@client.command(pass_context=True)
async def b64encode(ctx):
    params = ctx.message.content.split()[1:]
    message = ' '.join(params)

    await client.say(base64.b64encode(message.encode('ascii')).decode('utf-8'))

@client.command(pass_context=True)
async def b64decode(ctx):
    params = ctx.message.content.split()[1:]
    message = ' '.join(params)

    await client.say(base64.b64decode(message).decode('utf-8'))

# Fun commands

@client.command(pass_context=True)
async def fact(ctx):
    await client.say(random.choice(facts))

@client.command(pass_context=True)
async def magicball(ctx):
    await client.say("✨*Shaking magic tail...*✨")
    time.sleep(1)
    await client.say("🦊*Wiggling nose...*🦊")
    time.sleep(1)
    await client.say("🖥*Decrypting answer...*🖥")
    time.sleep(2)
    await client.say(random.choice(choices))

# Just for fun:
# Checks for a string and reacts
@client.event
async def on_message(message):

    if "fox" in message.content.lower():
        await client.add_reaction(message, "🦊")
    await client.process_commands(message) # Without this command, no other commands will be processed!


# Login token
# Note that this line must come LAST
client.run('')
