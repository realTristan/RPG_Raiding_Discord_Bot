import discord, os, os.path, json, asyncio, random, time
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Settings(commands.Cog):
    def __init__(self, client):
        self.client = client


    def write(self, file, data, f):
        with open(os.path.dirname(__file__) + f'\\..\\json\\{file}.json', 'w') as x:
            json.dump(data, x, indent=4)
            x.close()




    @commands.command()
    @has_permissions(administrator=True)
    async def setup(self, ctx):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            if not str(ctx.message.guild.id) in data:
                data.update({
                    str(ctx.message.guild.id): {
                        "builders": 2,
                        "speed_potions": 0,
                        "up_timer": [0, "none"],
                        "raid_timer": 0,
                        "raid_channel_id": int(ctx.message.channel.id),
                        "elixir storage": [0, 1], # elixir_storage[1] * 1000 is the max amount of storage
                        "gold storage": [0, 1],
                        "army": [0],
                        "defense": [0]
                    }
                })
                self.write("data", data, f)
                await ctx.send(embed=discord.Embed(description=f'{ctx.author.mention} successfully setup the raid bot', color=65535))







def setup(client):
    client.add_cog(Settings(client))