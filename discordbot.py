import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
#Not yet used, this block can be deleted

	@client.event
	async def on_message(message):
	    if message.author == client.user:
	        return

@client.command()
async def ping():
    await client.say('Pong!')

@client.event
async def on_ready():
	activity = discord.Game(name="Python")
	await client.change_presence(status=discord.Status.online, activity=activity)
	print ("Logged in as", client.user.name)
	



client.run('YOUR TOKEN HERE')
