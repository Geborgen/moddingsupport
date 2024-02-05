"""
Copyright notice:

Parts of this code are based on https://github.com/JonathanFeenstra/discord-modlinkbot:

Copyright (C) 2019-2023 Jonathan Feenstra
Copyright (C) 2022-2023 Arbigate

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import os
import discord
import aiohttp
from discord.ext import commands
from dotenv import load_dotenv
from nexus_search import RequestHandler
from cogs.modding_support import HelpCommand

load_dotenv()
extensions = ['cogs.modlink', 'cogs.modding_support', 'cogs.bot_battle_commands']
ERROR_CHANNEL_ID = 1056028135377874954
ARCHITECT_CHANNEL = 806307229182984202


class ModLink(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='-',
            help_command=HelpCommand(),
            intents=discord.Intents(
                guilds=True, members=True, message_content=True, guild_messages=True
            ),
            )

    async def setup_hook(self):
        self.loop.create_task(self.startup())

        for extension in extensions:
            await bot.load_extension(extension)

    async def startup(self):
        self.session = aiohttp.ClientSession()
        self.error_channel = self.get_channel(ERROR_CHANNEL_ID) or await self.fetch_channel(ERROR_CHANNEL_ID)
        self.architect_channel = self.get_channel(ARCHITECT_CHANNEL) or await self.fetch_channel(ARCHITECT_CHANNEL)
        await self.initialize_request_handler()

    async def close(self):
        await self.session.close()
        await super().close()

    async def initialize_request_handler(self):
        self.request_handler = RequestHandler(self.session)


bot = ModLink()


def check_if_verified(ctx):
    return ctx.message.author.id == 668828647653638174


@bot.command(name="sync")
@commands.check(check_if_verified)
async def sync(ctx):
    x = await bot.tree.sync()
    print(x)
    await ctx.send("Bot synced!")

bot.run(os.getenv("DISCORD_TOKEN"))
