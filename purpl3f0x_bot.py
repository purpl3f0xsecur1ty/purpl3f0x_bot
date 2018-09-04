# Import the required libraries

import discord
import hashlib
import base64

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
        print(server.default_channel)

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
                    "`f.b64decode <b64 encoded text>` - Decode Base64"
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

# Just for fun:
# Checks for a string and reacts
@client.event
async def on_message(message):

    if "fox" in message.content.lower():
        await client.add_reaction(message, "🦊")
    await client.process_commands(message) # Without this command the bot will not carry out any commands!!

# Login token
# Note that this line must come LAST
client.run('YOUR TOKEN HERE')
