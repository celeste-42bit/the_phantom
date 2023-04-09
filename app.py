import discord

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True
intents.reactions = True
class MyClient(discord.Client):
    #login
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('----------------------------------------------')

    #on_message
    async def on_message(self, message):
        # don't react to yourself, bot!
        if message.author == client.user:
            return

        print(str(message.author) + ": " + str(message.content))

        if message.content.startswith("$hello"):
            await message.channel.send("Hello " + str(message.author)[:-5])
        if message.content.startswith("$test"):
            await message.channel.send("This is a test.")

    #on_typing
    async def on_typing(self, channel, user, when):
        return

    #on_message_deleted
    async def on_message_delete(self, message):
        return

    '''
    #on_message_edit
    #async def on_message_edit(self, before, after):
        #return

    #on_reaction_add
    #async def on_reaction_add(self, reaction, user):
        #await reaction.message.channel.send(str(user) + " reacted " + str(reaction.message.content) + " with " + reaction.emoji)
        #await reaction.message.channel.send("Count: " + str(reaction.count))
        #return
    '''

    async def on_reaction_remove(self, reaction, user):
        return

    async def on_raw_reaction_add(self, payload):
        channel = client.get_channel(payload.channel_id)
        user = client.get_user(payload.user_id)
        message = await channel.fetch_message(payload.message_id)
        emoji = str(payload.emoji)
        return

    async def on_raw_reaction_remove(self, payload):
        return

    async def on_member_join(self, member):
        pass
    async def on_member_remove(self, member):
        pass
    async def on_member_update(self, before, after):
        pass

with open("token", "r") as tkn:
    token = str(tkn.read())
    tkn.close()

client = MyClient(intents=intents)
client.run(token)