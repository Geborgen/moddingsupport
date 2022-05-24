
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


import discord
from discord.ext import commands
from datetime import datetime

class ErrorReporting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='error')
    async def error(self, ctx):
        user = self.bot.get_user(668828647653638174)
        if user is None:
            user = await self.bot.fetch_user(668828647653638174)
            sender_id = ctx.message.author.id
            sender_name = ctx.message.author.name
            channel = ctx.message.channel.name
            timestamp = datetime.now()
        embed = discord.Embed(title="Modlink Error Reported")
        embed.add_field(name="Reporter:", value=f"Name: {sender_name} \n ID: {sender_id}", inline=False)
        embed.add_field(name="Channel:", value=f"#{channel}", inline=False)
        embed.add_field(name="Date and Time:", value= str(timestamp))
        await user.send(embed=embed)
        await ctx.send("The error has been reported. Thank you!")


def setup(bot):
    bot.add_cog(ErrorReporting(bot))