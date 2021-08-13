import discord, os, os.path, json, asyncio, random, time
from discord.ext import commands
from discord.utils import get, find
from discord.ext.commands import has_permissions
import datetime as datetime
from discord_components import *


class Functions(commands.Cog):
    def __init__(self, client):
        self.client = client

    def write(self, file, data, f):
        with open(os.path.dirname(__file__) + f'\\..\\json\\{file}.json', 'w') as x:
            json.dump(data, x, indent=4)
            x.close()


    def builders(self, guild):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            return data[str(guild.id)]["builders"]


    def numCheck(self, guild):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            for v in data[str(guild.id)]:
                try:
                    if int(data[str(guild.id)][v]) < 0:
                        data[str(guild.id)][v] = 0
                except Exception as e:
                    print(e)
                    pass
            
            if data[str(guild.id)]["elixir storage"] > (data[str(guild.id)]["elixir lvl"]) * Functions.builders(self, guild):
                data[str(guild.id)]["elixir storage"] = (data[str(guild.id)]["elixir lvl"]) * Functions.builders(self, guild)

            if data[str(guild.id)]["gold storage"] > (data[str(guild.id)]["gold lvl"]) * Functions.builders(self, guild):
                data[str(guild.id)]["gold storage"] = (data[str(guild.id)]["gold lvl"]) * Functions.builders(self, guild)

            Functions.write(self, "data", data, f)



    def levelSystem(self):
        random_levels = [1, 1, 1, 3, 4, 2, 1, 1, 1, 2, 2, 1, 3, 1, 0]
        level_up = random.choice(random_levels)
        if level_up <= 0: return 0
        else: return level_up



    def upgradeSystem(self, upgrade, guild):
        amount = Functions.levelSystem(self)
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            data[str(guild.id)][upgrade] += amount
            data[str(guild.id)]['speed_potions'] -= 1
            data[str(guild.id)]['up_timer'] = 0
            Functions.write(self, "data", data, f)
            return discord.Embed(title='Upgrade Success', description=f'Your Builders have upgraded your **{upgrade.replace("lvl", "storage")}** to level **{data[str(guild.id)][upgrade]}**', color=16777215)
            


    def raidSystem(self, guild):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            target=random.choice(list(data))
            if target == (guild.id):
                Functions.raidSystem(self, guild)
            else:
                arr = []
                for _ in range(round(12 * int(data[str(guild.id)]["army"]))):
                    arr.append(str(guild.id))

                for _ in range(round(10 * int(data[str(target)]["defense"]))):
                    arr.append(str(target))

                winner = random.choice(arr)

                if winner == str(guild.id):
                    data[str(guild.id)]["army"] += 2
                    data[str(guild.id)]["gold storage"] += 500
                    data[str(guild.id)]["elixir storage"] += 1000
                    
                    data[str(target)]["elixir storage"] -= 1200
                    data[str(target)]["gold storage"] -= 600

                    Functions.numCheck(self, guild)
                    return guild.id, target

                else:
                    data[str(target)]["defense"] += 2
                    data[str(target)]["gold storage"] += 500
                    data[str(target)]["elixir storage"] += 1000

                    data[str(guild.id)]["elixir storage"] -= 1200
                    data[str(guild.id)]["gold storage"] -= 600

                    Functions.write(self, "data", data, f)
                    return target, guild.id



def setup(client):
    client.add_cog(Functions(client))