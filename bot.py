# A Python 3 bot created by Joric using the tutorial found here: https://www.devdungeon.com/content/make-discord-bot-python
# Some features are original, some are from the guide
# Last Updated: 5-18-18

# TODO:
# make users with certain role be able to poll only
# more math functions
# image functions
# oof functions

# imports
import random
import re
import asyncio
import discord
from discord import Game
from discord.ext.commands import Bot

# sets the bot's command prefixes
BOT_PREFIX = ("?", "!")
TOKEN = "NDk3MTk0NjE1NjI0MTcxNTMx.DpbovA.vq4vn-gkO8t5SnLWBGx2wGjzdY0"

# creates a reaction list for polls
POLL_LIST = ['\U0001F44D', '\U0001F44E', '\U0001F937']
REACT_LIST = [':smash:', ':siege:', ':rocketleague:', ':overwatch:', ':league:', ':hearthstone:', ':fortnite:', ':dota2:', ':dbfz:', ':csgo:']
FLAIR_LIST = [':smash:497210123400249344', ':siege:497210123102715904', ':rocketleague:497210119646478336', ':overwatch:497210119499808770', ':league:497210123039670295', ':hearthstone:497210119772438529', ':fortnite:497210119243956236', ':dota2:497210119625637888', ':dbfz:497210124109086720', ':csgo:497210119193362433']


client = Bot(command_prefix=BOT_PREFIX)

# current commands
# general commands
# info
@client.command(name="info",
				description="Tells you all you need to know about Champ",
				category="Test",
				brief="Bork!",
				aliases=['information', 'about'],
				pass_context=True)
async def info(context):
	embed = discord.Embed(title="Champ",
					description="Champ is here to help you in discord!.",
					color=0xd4af37)
	embed.set_author(name="Champ", icon_url=client.user.avatar_url)
	embed.add_field(name="Creator",
				value="Joric")
	embed.add_field(name="Server Count",
				value="{:,}".format(len(client.servers)))
	embed.add_field(name="Invite",
				value="[Invite](https://discordapp.com/api/oauth2/authorize?client_id=446055335342505994&permissions=0&scope=bot)")
	embed.set_image(url="https://cdn.discordapp.com/attachments/446058435646324736/446483912005255179/monkaGIGA.png")
	embed.set_footer(text="") 
	await client.say(embed=embed)

#flairing
@client.command(name="flair",
				description="Allows users to flair themselves using various reactions",
				brief="flair",
				pass_context=True)
async def flair(context):
	embed = discord.Embed(title="Roles",
					description="React to this message using the respective logo to get your game's role! You can then access a channel dedicated to that game. To remove the role, remove your react!",
					color=0x003087)
	await client.say(embed=embed)
	async for message in client.logs_from(context.message.channel, limit=2):
			if message.author == client.user:
				for i in FLAIR_LIST:
					await client.add_reaction(message, i)
					
# add flair to when a user reacts
@client.event
async def on_reaction_add(reaction, user):
	if reaction.emoji in REACT_LIST:
		channel = reaction.message.channel
		await client.send_message(channel, '{} has added {} to the the message {}'.format(user.name, reaction.emoji, reaction.message))

# remove flair when a user removes their reaction
@client.event
async def on_reaction_remove(reaction, user):
	channel = reaction.message.channel
	await client.send_message(channel, '{} has removed {} to the message {}'.format(user.name, reaction.emoji, reaction.message))
	
# hello
@client.command(name='hello',
				description="Say hello to Champ!",
				brief="Greet Champ!",
				aliases=['hi', 'hiya'],
				pass_context=True)
async def greet(context):
	response_list = [
		"Hi there, " + context.message.author.mention + "!",
		"How's it going, " + context.message.author.mention + "?",
		"Hello, " + context.message.author.mention + "!",
	]
	await client.say(random.choice(response_list))

# 8 ball
@client.command(name='8ball',
				description="Answers a yes/no question.",
				brief="Answers from the beyond.",
				aliases=['eight_ball', 'eightball', '8-ball'],
				pass_context=True)
async def eight_ball(context):
	possible_responses = [
		'That is a resounding no',
		'It is not looking likely',
		'Too hard to tell',
		'Ask again later',
		'It is quite possible',
		'Definitely',
	]
	await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
	
# choose
@client.command(name='choose',
				description="Chooses from the desired choices listed.",
				brief="Let me choose!")
async def choose(*choices: str):
	await client.say(random.choice(choices))

# ping
@client.command(name='ping',
				description="Pong?",
				brief="Pong?")
async def ping():
	await client.say("🏓 Pong!")
	
# kiss
@client.command(name='kiss',
				description="Give your friend a nice smooch!",
				brief="Smoochy smoochy!",
				pass_context=True)
async def kiss(context):
	try:
		await client.say(f"{context.message.author.mention} (*^3^) mwahh!!~ {context.message.mentions[0].mention}")
	except IndexError:
		await client.say(f"{context.message.author.mention} (*^3^) " + client.user.mention)

# avatar
@client.command(name='avatar',
				description="Enhance a user's avatar image.",
				brief="What's your Avatar?",
				pass_context=True)
async def avatar(context):
	try:
		await client.say(context.message.mentions[0].avatar_url)
	except IndexError:
		await client.say(context.message.author.avatar_url)
		
# poll
# requires "Poll Creator" role
@client.command(name='poll',
				description="Creates a poll of a question automatically.",
				brief="Polling your question.",
				pass_context=True)
async def poll(context, *question: str):
	roleList = []
	for role in context.message.author.roles:
		roleList.append(role.name)
	if "Poll Creator" in roleList:
		embed = discord.Embed()
		embed.set_author(name=context.message.author, icon_url=context.message.author.avatar_url)
		embed.add_field(name="Poll:", value=responsify(question))
		await client.say(embed=embed)
		async for message in client.logs_from(context.message.channel, limit=2):
			if message.author == client.user:
				for i in POLL_LIST:
					await client.add_reaction(message, i)
	if "Poll Creator" not in roleList:
		await client.say("You do not have permission to create a poll.")

'''		
#peepo? (broked)
@client.listen()
async def on_message(message):
	if message.author == client.user:
		pass
	else:
		m = re.search("peppo", message.content, re.IGNORECASE)
		if m != None:
			await client.send_message(message.channel, "MEEEE!!!!!!")
'''
			
# math commands	
# square
@client.command(name='square',
				description="Squares a number.",
				brief="Squares a number.",
				aliases=['sqr'])
async def square(number):
	squared_value = int(number) * int(number)
	await client.say(str(number) + " squared is " + str(squared_value))
	
# image commands
# risa (laugh)
@client.command(name='risa',
				pass_context=True)
async def risa(context):
	client.send_file(context.message.channel, 'images\spanish-laugh.jpg') 
	
# functions
def responsify(raw_response):
	temp = list(raw_response)
	clean_response = ' '.join(temp)
	return clean_response

# when the bot is launched, the following will be printed in the console:
# A list of the current servers
# The bot's name
# It will also set the current game being played
@client.event
async def on_ready():
	await client.change_presence(game=Game(name="with humans"))
	print("Logged in as " + client.user.name)
	print("discord.py version " + discord.__version__)

async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed:
		print("Current servers:")
		for server in client.servers:
			print(server.name)
		print("------")
		await asyncio.sleep(600)

# runs the bot
client.loop.create_task(list_servers())
client.run(TOKEN)