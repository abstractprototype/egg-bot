import discord

TOKEN = 'OTk3NzYwOTMyMDczNzA5NjQ5.GiHRx0.3BDkdCTdTeJ8zS4f3q9WNdOuTA1j6XHCUAZpwE'

client = discord.Client()


@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.display_name}!')
        return

    if message.content.lower() == 'bye':
        await message.channel.send(f'See you later, {message.author.display_name}!')
        return

    if message.content.lower() == 'egg':
        await message.channel.send('Egg!')
        return

client.run(TOKEN)
