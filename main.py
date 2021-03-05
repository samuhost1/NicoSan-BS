import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="n!", inline=True, intents=discord.Intents.all())
icon = 'https://media.discordapp.net/attachments/816561013133672448/816561048357961738/NicoSan.png'
normcol = 0xff0000
gays = ['not gay', 'maybe a bit gay','a bit gay', 'very gay', 'the gaylord', 'lesbian']

client.remove_command('help')

@client.event
async def on_ready():
     await client.change_presence(activity=discord.Game(f'n!help | Made by Samu', status=discord.Status.online))

@client.command()
async def help(ctx):
    embed = discord.Embed(description='Here´s a list of all my commands. My prefix is `n!`', colour=normcol)
    embed.set_author(name='NicoSan Bot - help', icon_url=icon)
    embed.add_field(name='<:button_info:816559744973537281> Commands', value='`nicosan`, `howgay`')
    await ctx.send(embed=embed)

@client.command()
async def nicosan(ctx):
    embed=discord.Embed(colour=normcol)
    embed.set_author(name='NicoSan Bot - NicoSan', icon_url=icon)
    embed.add_field(name='<:button_info:816559744973537281> Who is NicoSan',
                    value='NicoSan is an insane Trickshotter.'
                          ' He has his own YT - Channel called "NicoSan BS". Make sure to subscribe to his channel!')
    await ctx.send('https://www.youtube.com/channel/UCBSLxhPZPNR2f1N-JRo53YQ', embed=embed)

@client.command()
async def howgay(ctx, user: discord.Member = None):
    if user is None:
        embed=discord.Embed(description='You have to mention a user.\r\n'
                                        '`F.e.:` n!howgay <@!816943898680360971>',
                            colour=normcol)
        embed.set_author(name='NicoSan Bot - Howgay error', icon_url=icon)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description=f'{user.mention} is {random.choice(gays)}'
                              , colour=normcol)
        embed.set_author(name='NicoSan Bot - Howgay', icon_url=icon)
        await ctx.send(embed=embed)
          
client.run(os.environ['token'])
