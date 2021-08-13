import discord, os, os.path, json, asyncio, random, time
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *
from .functions import *

class Raids(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_button_click(self, res):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            if res.component.id == "gold_up":
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} Started the Gold Storage Upgrade")
                data[str(res.guild.id)]["up_timer"][0] = (time.time() + (21600 / int(Functions.builders(self, res.message.guild))))
                data[str(res.guild.id)]["up_timer"][1] = "Gold Storage"
                
                Functions.write(self, "data", data, f); await res.message.delete()
                await asyncio.sleep(21600 / int(Functions.builders(self, res.message.guild)))
                await res.channel.send(embed=Functions.upgradeSystem(self, "gold storage", res.message.guild))

            if res.component.id == "elixir_up":
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} Started the Elixir Storage Upgrade")
                data[str(res.guild.id)]["up_timer"][0] = (time.time() + (21600 / int(Functions.builders(self, res.message.guild))))
                data[str(res.guild.id)]["up_timer"][1] = "Elixir Storage"
                
                Functions.write(self, "data", data, f); await res.message.delete()
                await asyncio.sleep(21600 / int(Functions.builders(self, res.message.guild)))
                await res.channel.send(embed=Functions.upgradeSystem(self, "elixir storage", res.message.guild))
            

            if res.component.id == "def_up":
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} Started the Defense Upgrade")
                data[str(res.guild.id)]["up_timer"][0] = (time.time() + (21600 / int(Functions.builders(self, res.message.guild))))
                data[str(res.guild.id)]["up_timer"][1] = "Defense"
                
                Functions.write(self, "data", data, f); await res.message.delete()
                await asyncio.sleep(21600 / int(Functions.builders(self, res.message.guild)))
                await res.channel.send(embed=Functions.upgradeSystem(self, "defense", res.message.guild))


            if res.component.id == "army_up":
                await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} Started the Army Upgrade")
                data[str(res.guild.id)]["up_timer"][0] = (time.time() + (21600 / int(Functions.builders(self, res.message.guild))))
                data[str(res.guild.id)]["up_timer"][1] = "Army"
                
                Functions.write(self, "data", data, f); await res.message.delete()
                await asyncio.sleep(21600 / int(Functions.builders(self, res.message.guild)))
                await res.channel.send(embed=Functions.upgradeSystem(self, "army", res.message.guild))
            
            if res.component.id == "buy_builder":
                if data[str(res.guild.id)]["gold storage"][0] - (5000 * data[str(res.guild.id)]["builders"]) > 0:
                    data[str(res.guild.id)]["gold storage"][0] - (5000 * data[str(res.guild.id)]["builders"])
                    data[str(res.guild.id)]["builders"] += 1
                    await res.channel.send(embed=discord.Embed(description=f'{res.author.mention} Purchased **+1 Builder**', color=65535))
                    await res.respond(type=InteractionType.ChannelMessageWithSource, content=f"{res.author.mention} Bought a builder!")

            if res.component.id == 'start_raid':
                raid = Functions.raidSystem(self, res.guild)
                data[str(res.guild.id)]["raid_timer"] = (time.time() + 900)
                Functions.write(self, "data", data, f)

                channel = self.client.get_channel(int(data[str(raid[0])]["raid_channel_id"]))
                await channel.send(embed=discord.Embed(title=f'You Won a Raid!', description=f'**Results**\n+500 Gold\n+1000 Elixir\n+2 Defense/Army Level', color=65535))

                channel = self.client.get_channel(int(data[str(raid[1])]["raid_channel_id"]))
                await channel.send(embed=discord.Embed(title=f'You Lost a Raid!', description=f'**Results**\n-600 Gold\n-1200 Elixir', color=65535))

            if res.component.id == 'yes_speed_pot':
                upgrade = data[str(res.guild.id)]["up_timer"][1]
                await res.message.delete()
                await res.channel.send(embed=Functions.upgradeSystem(self, f"{upgrade.lower()}", res.message.guild))

            if res.component.id == 'no_speed_pot':
                await res.message.delete()

            if res.component.id == 'cancel_raid':
                await res.message.delete()





def setup(client):
    client.add_cog(Raids(client))