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



    def levelSystem(self):
        random_levels = [1, 1, 1, 3, 4, 2, 1, 1, 1, 2, 2, 1, 3, 1, 0]
        level_up = random.choice(random_levels)
        if level_up <= 0: return 0
        else: return level_up



    def upgradeSystem(self, upgrade, guild):
        amount = Functions.levelSystem(self)
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            data[str(guild.id)][upgrade][len(data[str(guild.id)][upgrade]) - 1] += amount
            data[str(guild.id)]['speed_potions'] -= 1
            data[str(guild.id)]['up_timer'][0] = 0
            data[str(guild.id)]['raid_timer'][0] = 0
            Functions.write(self, "data", data, f)

            return discord.Embed(title='Upgrade Success', description=f'Your Builders have upgraded your **{upgrade}** to level **{data[str(guild.id)][upgrade.lower()][len(data[str(guild.id)][upgrade.lower()]) - 1]}**', color=16777215)
            


    def raidSystem(self, guild):
        with open(os.path.dirname(__file__) + f'\\..\\json\\data.json', 'r+') as f:
            data=json.load(f)
            target=random.choice(list(data))
            if target == (guild.id):
                Functions.raidSystem(self, guild)
            else:
                arr = []
                for _ in range(round(12 * int(data[str(guild.id)]["army"][0]))):
                    arr.append(str(guild.id))

                for _ in range(round(10 * int(data[str(target)]["defense"][0]))):
                    arr.append(str(target))

                winner = random.choice(arr)

                if winner == str(guild.id):
                    data[str(guild.id)]["army"][0] += 2

                    if data[str(guild.id)]["gold storage"][0] + 500 > data[str(guild.id)]["gold storage"][1] * 10000:
                        data[str(guild.id)]["gold storage"][0] = data[str(guild.id)]["gold storage"][1] * 10000
                    else:
                        data[str(guild.id)]["gold storage"][0] += 500
                    
                    if data[str(guild.id)]["elixir storage"][0] + 1000 > data[str(guild.id)]["elixir storage"][1] * 10000:
                        data[str(guild.id)]["elixir storage"][0] = data[str(guild.id)]["elixir storage"][1] * 10000
                    else:
                        data[str(guild.id)]["elixir storage"][0] += 1000
                    

                    if data[str(target)]["elixir storage"][0] - 1200 <= 0:
                        data[str(target)]["elixir storage"][0] = 0
                    else:
                        data[str(target)]["elixir storage"][0] -= 1200

                    if data[str(target)]["gold storage"][0] - 600 <= 0:
                        data[str(target)]["gold storage"][0] = 0
                    else:
                        data[str(target)]["gold storage"][0] -= 600

                    Functions.write(self, "data", data, f)
                    return guild.id, target

                else:
                    data[str(target)]["defense"][0] += 2
            
                    if data[str(target)]["gold storage"][0] + 500 > data[str(target)]["gold storage"][1] * 10000:
                        data[str(target)]["gold storage"][0] = data[str(target)]["gold storage"][1] * 10000
                    else:
                        data[str(target)]["gold storage"][0] += 500

                    if data[str(target)]["elixir storage"][0] + 1000 > data[str(target)]["elixir storage"][1] * 10000:
                        data[str(target)]["elixir storage"][0] = data[str(target)]["elixir storage"][1] * 10000
                    else:
                        data[str(target)]["elixir storage"][0] += 1000
                    

                    if data[str(guild.id)]["elixir storage"][0] - 1200 <= 0:
                        data[str(guild.id)]["elixir storage"][0] = 0
                    else:
                        data[str(guild.id)]["elixir storage"][0] -= 1200

                    if data[str(guild.id)]["gold storage"][0] - 600 <= 0:
                        data[str(guild.id)]["gold storage"][0] = 0
                    else:
                        data[str(guild.id)]["gold storage"][0] -= 600

                    Functions.write(self, "data", data, f)
                    return target, guild.id



def setup(client):
    client.add_cog(Functions(client))