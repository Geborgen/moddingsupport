"""
Copyright notice:

Parts of this code are based on https://github.com/JonathanFeenstra/discord-modlinkbot:

Copyright (C) 2019-2021 Jonathan Feenstra

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
import discord
import aiohttp
import re
import random
from discord.ext import commands
from dotenv import load_dotenv
from modlink import parse_query
from modlink_exceptions import exceptions
from modlink_exceptions import common_acronyms
from modlink_exceptions import sos_acronym
from modlink_exceptions import le_modlink_exceptions
from modlink_exceptions import se_modlink_exceptions

SEARCH_REGEX = re.compile(r'{(.*?)}')
intents = discord.Intents.default()
extensions = ['cogs.modding_support', 'cogs.error_reporting']
load_dotenv()

class ModlinkBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='-', intents=intents, help_command=None)
        self.loop.create_task(self.startup())

    async def startup(self):
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()
        await super().close()
    
    async def get_modlink(self, query):
        if query.lower() not in se_modlink_exceptions:
            async with self.session.get("https://search.nexusmods.com/mods", params={"terms": parse_query(query), "game_id": 1704}) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    results = data["results"]
                    if results:
                        return results[0]
        else:
            return

    async def get_le_modlink(self, query):
        if query.lower() not in le_modlink_exceptions:
            async with self.session.get("https://search.nexusmods.com/mods", params={"terms": parse_query(query), "game_id": 110}) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    results = data["results"]
                    if results:
                        return results[0]
        else:
            return

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return

        queries = SEARCH_REGEX.findall(message.content)
        if len(queries) > 5:
            return await message.channel.send('You cannot link more than 5 mods in a message.')
        for query in queries:
            if query.lower() == "sos":
                random_sos = random.choice(list(sos_acronym))
                exceptions_embed = discord.Embed(title= str(random_sos))
                exceptions_embed.add_field(name= "-", value = sos_acronym[random_sos])
                exceptions_embed.set_footer(text="If the bot makes any mistake, use -error please; it helps improve the bot. For the source code, use \n-source")
                await message.channel.send(embed=exceptions_embed)
                continue
            if query.lower() in exceptions.keys():
                exceptions_embed = discord.Embed(title= str(query.title()))
                exceptions_embed.add_field(name="Special Edition", value=f"[{query.title()}]({exceptions[query.lower()]})")
                exceptions_embed.set_footer(text="If the bot makes any mistake, use -error please; it helps improve the bot. For the source code, use \n-source")
                await message.channel.send(embed=exceptions_embed)
                continue
            if query.lower() in common_acronyms.keys():
                modlink = await self.get_modlink(common_acronyms[query.lower()])
                le_modlink = await self.get_le_modlink(common_acronyms[query.lower()])
            else:
                modlink = await self.get_modlink(query)
                le_modlink = await self.get_le_modlink(query)
            if modlink is not None and le_modlink is not None:
                embed = discord.Embed(title= f'Search results for: "{query}"')
                embed.add_field(name="Special Edition", value= f"[{modlink['name']}](https://www.nexusmods.com{modlink['url']})")
                embed.add_field(name="Legendary Edition", value=f"[{le_modlink['name']}](https://www.nexusmods.com{le_modlink['url']})")
                embed.set_footer(text="If the bot makes any mistake, use -error please; it helps improve the bot. For the source code, use \n-source")
                await message.channel.send(embed=embed)
            elif le_modlink is not None:
                embed = discord.Embed(title= f'Search results for: "{query}"')
                embed.add_field(name="Legendary Edition", value =f"[{le_modlink['name']}](https://www.nexusmods.com{le_modlink['url']})")
                embed.set_footer(text="If the bot makes any mistake, use -error please; it helps improve the bot. For the source code, use \n-source")
                await message.channel.send(embed=embed)
            elif modlink is not None:
                embed = discord.Embed(title= f'Search results for: "{query}"')
                embed.add_field(name="Special Edition", value =f"[{modlink['name']}](https://www.nexusmods.com{modlink['url']})")
                embed.set_footer(text="If the bot makes any mistake, use -error please; it helps improve the bot. For the source code, use \n-source")
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(f'There were no results for: "{query}"')

        await bot.process_commands (message)

bot = ModlinkBot()


if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)


bot.run(os.getenv("DISCORD_TOKEN"))





