# A Python 3 bot created by Joric using the tutorial found here: https://www.devdungeon.com/content/make-discord-bot-python
# Some features are original, some are from the guide
# Last Updated: 10-20-18

# TODO:
# make users with certain role be able to poll only
# more math functions
# image functions
# oof functions

# imports
import random
import requests
import config
import asyncio
import discord
from discord import Game
from discord.ext.commands import Bot

# sets the bot's command prefixes
BOT_PREFIX = ("?", "!")

# creates a reaction list for polls
POLL_LIST = ['\U0001F44D', '\U0001F44E', '\U0001F937']
ROLE_LIST = ['smash', 'siege', 'rocketleague', 'overwatch', 'league', 'hearthstone', 'fortnite', 'dota', 'dbfz', 'csgo']
FLAIR_LIST = [':smash:497210123400249344', ':siege:497210123102715904', ':rocketleague:497210119646478336', ':overwatch:497210119499808770', ':league:497210123039670295', ':hearthstone:497210119772438529', ':fortnite:497210119243956236', ':dota2:497210119625637888', ':dbfz:497210124109086720', ':csgo:497210119193362433']
ROLE_ID = [497210123400249344]

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
				value="{:,}".format(len(client.guilds)))
	embed.add_field(name="Invite",
				value="[Invite](https://discordapp.com/api/oauth2/authorize?client_id=446055335342505994&permissions=0&scope=bot)")
	embed.set_image(url="https://cdn.discordapp.com/attachments/446058435646324736/446483912005255179/monkaGIGA.png")
	embed.set_footer(text="") 
	await context.send(embed=embed)

	
# test steam
@client.command(name='steam',
				pass_context=True)
async def steam(context):
	r = requests.get('https://steamgaug.es/api/v2')
	json = r.json()
	embed = discord.Embed(color=0x505050)
	embed.set_author(name="Steam Status", icon_url="https://images-ext-2.discordapp.net/external/yLGqhhaaGzCx2L2nDNOa0SU47p0jo3y97CsGuPNtSI8/https/upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/2000px-Steam_icon_logo.svg.png")
	embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/yLGqhhaaGzCx2L2nDNOa0SU47p0jo3y97CsGuPNtSI8/https/upload.wikimedia.org/wikipedia/commons/thumb/8/83/Steam_icon_logo.svg/2000px-Steam_icon_logo.svg.png")
	embed.set_footer(text="via steamgaug.es")
	
	if json["SteamCommunity"]["online"] == 1:
		embed.add_field(name="Steam Community",
				value = "Online <:yes:503287380719960074>",
				inline = True)
	else:
		embed.add_field(name="Steam Community",
				value = "Offline <:no:503287380883537947>",
				inline = True)
	if json["SteamStore"]["online"] == 1:
		embed.add_field(name="Steam Store",
				value = "Online <:yes:503287380719960074>",
				inline = True)
	else:
		embed.add_field(name="Steam Store",
				value = "Offline <:no:503287380883537947>",
				inline = True)

# # # # # # # STEAM API IS CURRENTLY DOWN FOR GAMES # # # # # # # 
#	if json["ISteamGameCoordinator"]["570"]["online"] == 1:
#		embed.add_field(name="Dota 2 <:dota2:497210119625637888>",
#					value = "Online with {} players".format(json["ISteamGameCoordinator"]["570"]["stats"]["players_searching"]),
#					inline = True)
#	else:
#		embed.add_field(name="Dota 2 <:dota2:497210119625637888>",
#					value = "Offline",
#					inline = True)
#	if json["ISteamGameCoordinator"]["730"]["online"] == 1:
#		embed.add_field(name="CS:GO <:csgo:497210119193362433>",
#					value = "Online with {} players".format(json["ISteamGameCoordinator"]["730"]["stats"]["players_searching"]),
#					inline = True)
#	else:
#		embed.add_field(name="CS:GO <:csgo:497210119193362433>",
#					value = "Offline",
#					inline = True)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #	
	
	await context.send(embed=embed)
	
	
	
#flairing
@client.command(name="flair",
				description="Allows users to flair themselves using various reactions",
				brief="flair")
async def flair(context):
	embed = discord.Embed(title="Roles",
					description="React to this message using the respective logo to get your game's role! You can then access a channel dedicated to that game. To remove the role, remove your react!",
					color=0x003087)
	await context.send(embed=embed)
	async for message in context.channel.history(limit=2):
			if message.author == client.user:
				for i in FLAIR_LIST:
					await message.add_reaction(i)
					
# add flair to when a user reacts
@client.event
async def on_raw_reaction_add(payload):
	guild = discord.utils.get(client.guilds, name = "Test")
	channelID = 446058435646324736
	member = guild.get_member(payload.user_id)
	print(member)
	if payload.user_id != client.user.id:
		if payload.channel_id != channelID:
			return
		if payload.emoji.name in ROLE_LIST:
			if payload.emoji.name == ROLE_LIST[0]:
				role = guild.get_role(ROLE_ID[0])
		#	if payload.emoji.name == "siege":
		#		role = discord.utils.get(user.server.roles, name='siege')
		#	if payload.emoji.name == "rocketleague":
		#		role = discord.utils.get(user.server.roles, name='rocketleague')
		#	if payload.emoji.name == "overwatch":
		#		role = discord.utils.get(user.server.roles, name='overwatch')
		#	if payload.emoji.name == "league":
		#		role = discord.utils.get(user.server.roles, name='league')
		#	if payload.emoji.name == "hearthstone":
		#		role = discord.utils.get(user.server.roles, name='hearthstone')
		#	if payload.emoji.name == "fortnite":
		#		role = discord.utils.get(user.server.roles, name='fortnite')
		#	if payload.emoji.name == "dota2":
		#		role = discord.utils.get(user.server.roles, name='dota')
		#	if payload.emoji.name == "dbfz":
		#		role = discord.utils.get(user.server.roles, name='dbfz')
		#	if payload.emoji.name == "csgo":
		#		role = discord.utils.get(user.server.roles, name='csgo')
				
			await member.add_roles(role)
			print("Role {} added to {}".format(role, member))
	

# remove flair when a user removes their reaction
@client.event
async def on_reaction_remove(reaction, user):
	channelID = '446058435646324736'
	if reaction.message.author != user:
		if reaction.message.channel.id != channelID:
			return
		if payload.emoji.name in ROLE_LIST:
			if payload.emoji.name == "smash":
				role = discord.utils.get(user.server.roles, name='smash')
			if payload.emoji.name == "siege":
				role = discord.utils.get(user.server.roles, name='siege')
			if payload.emoji.name == "rocketleague":
				role = discord.utils.get(user.server.roles, name='rocketleague')
			if payload.emoji.name == "overwatch":
				role = discord.utils.get(user.server.roles, name='overwatch')
			if payload.emoji.name == "league":
				role = discord.utils.get(user.server.roles, name='league')
			if payload.emoji.name == "hearthstone":
				role = discord.utils.get(user.server.roles, name='hearthstone')
			if payload.emoji.name == "fortnite":
				role = discord.utils.get(user.server.roles, name='fortnite')
			if payload.emoji.name == "dota2":
				role = discord.utils.get(user.server.roles, name='dota')
			if payload.emoji.name == "dbfz":
				role = discord.utils.get(user.server.roles, name='dbfz')
			if payload.emoji.name == "csgo":
				role = discord.utils.get(user.server.roles, name='csgo')

			await client.remove_roles(user, role)
			print("Role {} removed from {}".format(role, user.name))
	
	
	
	
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
			
# math commands	
# square
@client.command(name='square',
				description="Squares a number.",
				brief="Squares a number.",
				aliases=['sqr'])
async def square(context, number):
	squared_value = int(number) * int(number)
	await context.send(str(number) + " squared is " + str(squared_value))
	
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
	await client.change_presence(activity=discord.Game(name="Testing Roles"))
	print("Logged in as " + client.user.name)
	print("discord.py version " + discord.__version__)

				
	

async def list_servers():
	await client.wait_until_ready()
	while not client.is_closed():
		print("------")
		print("Current servers:")
		for guild in client.guilds:
			print(guild.name)
		print("------")
		await asyncio.sleep(600)

# runs the bot
client.loop.create_task(list_servers())
client.run(config.token)