
"""
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

import asyncio
import discord

ARBIGATE = 668828647653638174
GEBORGEN = 358998624295714816

elevated_users = {
    '668828647653638174': 'Arbigate',
    '259867648542638081': 'Griseo',
    '292387271049609226': 'Adroit',
    '837258758890586143': 'Monitor',
    '358998624295714816': 'Geborgen',
    '269261628099264523': 'Val',
    '861116755781877790': 'Olivinism',
    '397336803054714891': 'Fox',
    '882139549084557332': 'Shizar'
}


async def error_report(self, message, user, guild):
    dev = self.get_user(GEBORGEN)
    if dev is None:
        dev = await self.fetch_user(GEBORGEN)

    embeds = message.embeds
    for embed in embeds:
        incorrect_message = embed.to_dict()
        error_embed = discord.Embed(title="Error Report")
        error_embed.add_field(name='Reporter:', value=str(user), inline=False)
        error_embed.add_field(name='Guild:', value=str(user.guild), inline=False)
        error_embed.add_field(name='Query:', value=incorrect_message['title'], inline=False)
        if 'fields' in incorrect_message.keys():
            error_embed.add_field(name='Fields:', value=incorrect_message['fields'])
            await dev.send(embed=error_embed)
        else:
            await dev.send(embed=error_embed)


async def deletion_reaction(self, message):
    await message.add_reaction('\N{CROSS MARK}')

    def check(reaction, user):
        return str(user.id) in elevated_users.keys() and reaction.message == message and str(reaction.emoji) in ['\N{CROSS MARK}']

    try:
        reaction, user = await self.wait_for("reaction_add", timeout=20, check=check)
        if str(reaction.emoji) == '\N{CROSS MARK}':
            await message.delete()
    except asyncio.TimeoutError:
        await message.remove_reaction('\N{CROSS MARK}', self.user)


async def error_reaction(self, message):
    await message.add_reaction('\N{WHITE QUESTION MARK ORNAMENT}')

    def check(reaction, user):
        return user != self.user and reaction.message == message and str(reaction.emoji) in ['\N{WHITE QUESTION MARK ORNAMENT}']

    try:
        reaction, user = await self.wait_for("reaction_add", timeout=20, check=check)
        if str(reaction.emoji) == '\N{WHITE QUESTION MARK ORNAMENT}':
            await error_report(self, message, user, user.guild)
            await message.channel.send("The error was reported. Thank you!")
            await message.remove_reaction('\N{WHITE QUESTION MARK ORNAMENT}', self.user)
    except asyncio.TimeoutError:
        try:
            await message.remove_reaction('\N{WHITE QUESTION MARK ORNAMENT}', self.user)
        except discord.NotFound:
            return
