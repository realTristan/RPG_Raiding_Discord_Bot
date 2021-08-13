import discord, os, os.path, json, asyncio, random, time
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *
from .functions import *


class Core(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def raid(self, ctx):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f); await ctx.message.delete()
            timeLeft = data[str(ctx.message.guild.id)]["raid_timer"] - time.time()
            if timeLeft > 0:
                await ctx.send(embed=discord.Embed(title=f'Raid Blocked ┃ {str(datetime.timedelta(seconds=int(timeLeft)))}', description=f"{ctx.author.mention} would you like to use a **Speed Potion? [1/{data[str(ctx.message.guild.id)]['speed_potions']}]**", color=65535),
                    components=[
                    [Button(style=ButtonStyle.green, label="Yes", custom_id="raid_speed_pot"),
                    Button(style=ButtonStyle.red, label="No", custom_id="cancel")]])
            else:
                await ctx.send(
                embed=discord.Embed(title="Are you sure?", description=f'**Lord {ctx.author.mention}**, are you sure you want to start a raid?', color=16777215),
                components=[
                [Button(style=ButtonStyle.green, label="Start", custom_id="start_raid"),
                Button(style=ButtonStyle.red, label="Cancel", custom_id="cancel")]])



    @commands.command()
    @has_permissions(administrator=True)
    async def shop(self, ctx):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f); await ctx.message.delete()
            embed=discord.Embed(title='Select an item to purchase', color=65535)
            embed.add_field(name=f'Buy a Builder [{5000 * data[str(ctx.message.guild.id)]["builders"]}$]', value='Amount: **+1**')
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='Buy Speed Potion [2200$]', value='Amount: **+1**')
            embed.add_field(name=' ‎\nBuy Gold Storage [1700$]', value='Amount: **+1 lvl**')
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name=' ‎\nBuy Elixir Storage [1700$]', value='Amount: **+1 lvl**')
            embed.add_field(name=' ‎\nBuy Defenses [1300$]', value='Amount: **+1 lvl**')
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name=' ‎\nBuy Army Troops [1300$]', value='Amount: **+1 lvl**')
            await ctx.send(
            embed=embed,
            components=[
            [Button(style=ButtonStyle.blue, label="Builder", custom_id="buy_builder"),
            Button(style=ButtonStyle.blue, label="Speed Potion", custom_id="buy_speed_pot"),
            Button(style=ButtonStyle.blue, label="Gold Storage", custom_id="buy_gold_up")],
            [Button(style=ButtonStyle.blue, label="Elixir Storage", custom_id="buy_elixir_up"),
            Button(style=ButtonStyle.blue, label="Defense", custom_id="buy_def_up"),
            Button(style=ButtonStyle.blue, label="Army", custom_id="buy_army_up")]])



    @commands.command()
    @has_permissions(manage_messages=True)
    async def upgrade(self, ctx):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f); await ctx.message.delete()
            timeLeft = int(data[str(ctx.message.guild.id)]["up_timer"]) - time.time()
            upgrade = data[str(ctx.message.guild.id)]["up_name"]

            if timeLeft > 0:
                if data[str(ctx.message.guild.id)]["speed_potions"] > 0:
                    await ctx.send(embed=discord.Embed(title=f'{upgrade} Upgrade in Progress ┃ {str(datetime.timedelta(seconds=int(timeLeft)))}', description=f"{ctx.author.mention} would you like to use a **Speed Potion? [1/{data[str(ctx.message.guild.id)]['speed_potions']}]**", color=65535),
                    components=[
                    [Button(style=ButtonStyle.green, label="Yes", custom_id="up_speed_pot"),
                    Button(style=ButtonStyle.red, label="No", custom_id="cancel")]])
                    
                else:
                    await ctx.send(embed=discord.Embed(title=f'{upgrade} Upgrade in Progress ┃ {str(datetime.timedelta(seconds=int(timeLeft)))}', color=65535))
            else:
                await ctx.send(
                embed=discord.Embed(title='Select an upgrade', color=65535),
                components=[
                [Button(style=ButtonStyle.blue, label="Gold Storage", custom_id="gold_up"),
                Button(style=ButtonStyle.blue, label="Elixir Storage", custom_id="elixir_up"),
                Button(style=ButtonStyle.red, label="Defense", custom_id="def_up"),
                Button(style=ButtonStyle.red, label="Army", custom_id="army_up")]])



    @commands.command()
    async def bank(self, ctx):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f); await ctx.message.delete()
            embed=discord.Embed(title=f"{ctx.message.guild.name}'s Bank", color=16776992)
            embed.add_field(name='Gold', value=f'Amount: **{data[str(ctx.message.guild.id)]["gold storage"]}**\nLevel: **{data[str(ctx.message.guild.id)]["gold lvl"]}**')
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='Elixir', value=f'Amount: **{data[str(ctx.message.guild.id)]["elixir storage"]}**\nLevel: **{data[str(ctx.message.guild.id)]["elixir lvl"]}**')
            embed.add_field(name='‏‏‎ ‎\nArmy', value=f'Level: **{data[str(ctx.message.guild.id)]["army"]}**')
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='‏‏‎ ‎\nDefenses', value=f'Level: **{data[str(ctx.message.guild.id)]["defense"]}**')
            embed.add_field(name='‏‏‎ ‎\nBuilders', value=f'Amount: **{data[str(ctx.message.guild.id)]["builders"]}**')
            await ctx.send(embed=embed)







def setup(client):
    client.add_cog(Core(client))