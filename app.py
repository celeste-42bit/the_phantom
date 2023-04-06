import discord

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True
intents.reactions = True

class MyClient(discord.Client):
    #login
    async def on_ready(self):
        print("Login complete!")
    
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
    
    #on_message_edit
    async def on_message_edit(self, before, after):
        return


with open("token", "r") as tkn:
    token = str(tkn.read())
    tkn.close()

client = MyClient(intents=intents)
client.run(token)