
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

valid_id = [668828647653638174]

class ErrorReporting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def check_author(ctx):
        if ctx.author.id in valid_id:
            return ctx.author.id in valid_id

    @commands.command(name='error')
    async def error(self, ctx):
        user = self.bot.get_user(668828647653638174)
        if user is None:
            user = await self.bot.fetch_user(668828647653638174)
            channel = ctx.message.channel.name
            timestamp = datetime.now()
        embed = discord.Embed(title="Modlink Error Reported")
        embed.add_field(name="Reporter:", value=f"Name: {ctx.message.author.name}#{ctx.message.author.discriminator} \n ID: {ctx.message.author.id}", inline=False)
        embed.add_field(name="Channel:", value=f"#{channel}", inline=False)
        embed.add_field(name="Date and Time:", value= str(timestamp))
        await user.send(embed=embed)
        await ctx.send("The error has been reported. Thank you!")

    @commands.command(name='respond')
    @commands.check(check_author)
    async def respond(self, ctx, user: discord.User, error_image, *, response):
        embed = discord.Embed(title="Error Response", description=f"**Responder:** {ctx.message.author.name}#{ctx.message.author.discriminator} \n \n **Response:**\n {response}")
        embed.set_image(url=f"{error_image}")
        await user.send(embed=embed)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ErrorReporting(bot))
