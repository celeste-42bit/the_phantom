import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

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
        
        if message.content.startswith("Hello Phantom!"):
            await message.channel.send("Hello " + str(message.author)[:-5])


with open("token", "r") as tkn:
    token = str(tkn.read())
    tkn.close()

client = MyClient(intents=intents)
client.run(token)