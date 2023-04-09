import discord

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True
intents.reactions = True

client = discord.Client(intents = intents)

print(str(discord.version_info) + " PEP440 compliant: " + str(discord.__version__))

#login
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('----------------------------------------------')

    # ---- this is just for the fancies, ignore this... mumble, mumble... ----

    with open('intro', 'r', encoding='utf-8') as i:
        print(i.read())
        i.close()

    # ---- this is just for the fancies, ignore this... mumble, mumble... ----

    #bot_channel = client.get_channel(1091021500259241984)

#on_message
@client.event
async def on_message(message):
    # don't react to your bot!
    if message.author == client.user:
        return
    '''
    This is how you select a specific channel:

    welcome_channel = client.get_channel(welcome_channel_id)
    await welcome_channel.send("Woo!")
    '''
    print(str(message.channel.id))
    #print(str(message.author) + ": " + str(message.content))  # <----
    '''
    This throws an error, because Win console can't display unicode characters. StackOverflow suggests to fix this by installing the package win-unicode-console,
    although this didn't fix the issue.
    '''

    if message.content.startswith('$hello'):
        await message.channel.send('Hello ' + str(message.author)[:-5])  # [:-5] cut last 5 symbols (#0000)


#on_typing
@client.event
async def on_typing(channel, user, when):
    return


#on_message_deleted
@client.event
async def on_message_delete(message):
    return


'''
#on_message_edit
#@client.event
#async def on_message_edit(before, after):
    #return

#on_reaction_add
#@client.event
#async def on_reaction_add(reaction, user):
    #await reaction.message.channel.send(str(user) + " reacted " + str(reaction.message.content) + " with " + reaction.emoji)
    #await reaction.message.channel.send("Count: " + str(reaction.count))
    #return
'''

@client.event
async def on_reaction_remove(reaction, user):
    return

@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    user = client.get_user(payload.user_id)
    message = await channel.fetch_message(payload.message_id)
    emoji = str(payload.emoji)

@client.event
async def on_raw_reaction_remove(payload):
    return

@client.event
async def on_member_join(member):
    pass

@client.event
async def on_member_remove(member):
    pass

@client.event
async def on_member_update(before, after):
    pass


with open("token", "r") as tkn:
    token = str(tkn.read())
    tkn.close()

client.run(token)