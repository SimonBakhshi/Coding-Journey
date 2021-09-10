import discord
import random 

token = "xxxxxxxx"

client = discord.Client()

@client.event # event decorator/wrapper
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return
    
    if message.channel.name == "dobberman":
        if user_message.lower() == "hey":
            await message.channel.send(f"Yo whats up ;) {username}")
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f"see you later alig8tor {username} !")
        elif user_message.lower() == "!random":
            response = f"This is your random number: {random.randrange(1000000)}"
            await message.channel.send(response)
            return
    
    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return 


client.run(token)
