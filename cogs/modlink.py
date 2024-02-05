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

import discord
from discord.ext import commands
from nexus_search import parse_query
from common_exceptions import false_nsfw_flagged
from common_exceptions import common_acronyms
from common_exceptions import manual_exceptions
import re

SEARCH_QUERIES_RE = re.compile(r"{([^\";:=\*%\$&_<>\?`\[\]{]*?)}")  # Searches for text within curly brackets and removes some unwanted characters.
trusted_users = [668828647653638174, 358998624295714816]


def format_error_reports(error_content, guild, user, date, title="Modlink Error Reported"):

    if len(error_content['fields']) > 2:  # Single query embeds are formatted differently, so this checks if it is single or multiple queries.
        error_report_embed = discord.Embed(title=title, color=0x197482)
        error_report_embed.add_field(name="Guild:", value=guild)
        error_report_embed.add_field(name="User:", value=f"{user.name}#{user.discriminator}")
        error_report_embed.add_field(name="Date:", value=date)
        for field in error_content['fields']:
            error_report_embed.add_field(name=field['name'], value=field['value'], inline=field['inline'])
    else:
        error_report_embed = discord.Embed(title=title, description=f"{error_content['title']}", color=0x197482)
        error_report_embed.add_field(name="Guild:", value=guild)
        error_report_embed.add_field(name="User:", value=f"{user.name}#{user.discriminator}")
        error_report_embed.add_field(name="Date:", value=date)
        for field in error_content['fields']:
            error_report_embed.add_field(name=field['name'], value=field['value'])
    return error_report_embed


def find_queries(msg):
    queries = []
    for query in SEARCH_QUERIES_RE.findall(msg.content):
        if len(queries) > 5:
            return queries
        else:
            if 2 < len(parse_query(query)) < 100:
                queries.append(query.strip())
    return queries


class ModLinkSearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author.bot or not (queries := find_queries(msg)):
            return
        if (ctx := await self.bot.get_context(msg)).valid:
            return
        if len(queries) > 5:
            embed = discord.Embed(description="You cannot link more than 5 mods in a message.", color=0x197482)
            await ctx.send(embed=embed)
        else:
            await self.search_nexus_for_query(ctx, queries)

    async def search_nexus_for_query(self, ctx, queries, acronym=None):
        embed = discord.Embed(title="Modlink Results:", color=0x197482)
        games = {1704: "Special Edition", 110: "Legendary Edition"}
        search_results = []
        for query in queries:  # This is where the nexus endpoint is utilized, and result data is obtained.
            for game_id in games.keys():
                if query.lower() in manual_exceptions.keys():
                    search_results.append(manual_exceptions[query.lower()][0])
                    search_results.append(manual_exceptions[query.lower()][1])
                    break
                resp = await self.bot.request_handler.search_mods(query=query, game_id=game_id, include_adult=False)
                if query.lower() in false_nsfw_flagged.keys():
                    resp = await self.bot.request_handler.search_mods(query=query, game_id=game_id, include_adult=True)
                if query.lower() in common_acronyms.keys():
                    resp = await self.bot.request_handler.search_mods(query=common_acronyms[query.lower()], game_id=game_id, include_adult=False)
                if resp['total'] >= 1:  # "Total" is the number of results nexus recognized.
                    search_results.append(resp['results'][0])
                else:  # If no results are found the game_id is saved and a string attached for easy recognition.
                    no_result_info = {"No results": game_id}
                    search_results.append(no_result_info)
        if len(search_results) <= 2:  # Uses a more efficient embed layout for single-query searches.
            embed = discord.Embed(title=f"Search results for: '{queries[0]}'", color=0x197482)
            for results in search_results:
                if "No results" in results.keys():  # Executes if either SE or LE search result is blank
                    if results['No results'] == 1704:
                        embed.add_field(name="Special Edition", value="No results", inline=True)
                    else:
                        embed.add_field(name="Legendary Edition", value="No results", inline=True)
                else:  # Splits the search results into LE and SE inline fields.
                    if results['game_id'] == 1704:
                        embed.add_field(name='Special Edition', value=f"[{results['name']}](https://www.nexusmods.com{results['url']})", inline=True)
                    else:
                        embed.add_field(name='Legendary Edition', value=f"[{results['name']}](https://www.nexusmods.com{results['url']})", inline=True)
        else:
            iterations_counter = 0  # Counter used to position embed fields and used instead of passing 'query'.
            for results in search_results:
                if (iterations_counter % 2 == 0) and iterations_counter == 0:  # Adds initial embed break.
                    embed.add_field(name=f"Search results for:", value=f"**'{queries[iterations_counter]}'**", inline=False)
                if (iterations_counter % 2 == 0) and iterations_counter > 0:  # Adds new embed break every two results.
                    embed.add_field(name=f"Search results for:", value=f"**'{queries[int(iterations_counter/2)]}'**", inline=False)
                if "No results" in results.keys():  # Executes if either SE or LE search result is blank
                    if results['No results'] == 1704:
                        embed.add_field(name="Special Edition", value="No results", inline=True)
                        iterations_counter += 1
                    else:
                        embed.add_field(name="Legendary Edition", value="No results", inline=True)
                        iterations_counter += 1
                else:  # Splits the search results into LE and SE inline fields.
                    if results['game_id'] == 1704:
                        embed.add_field(name='Special Edition', value=f"[{results['name']}](https://www.nexusmods.com{results['url']})", inline=True)
                        iterations_counter += 1
                    else:
                        embed.add_field(name='Legendary Edition', value=f"[{results['name']}](https://www.nexusmods.com{results['url']})", inline=True)
                        iterations_counter += 1
        if acronym:
            embed.add_field(name="Acronym Used:", value=f"'{acronym}'", inline=False)
            view = AcronymSuggestionButtons(self.bot.architect_channel)
            view.message = await ctx.send(content=f'Is this the mod you wanted to link?', embed=embed, view=view, ephemeral=True)
        else:
            view = ModLinkButtons(self.bot.error_channel)
            view.message = await ctx.send(embed=embed, view=view, ephemeral=False)

    @commands.hybrid_command(name='link', description='Searches Nexus for input and provides mod link.')
    async def link(self, ctx, *, query):
        queries = []
        raw_queries = query.split(',')
        for query in raw_queries:
            if 2 < len(parse_query(query)) < 100:
                queries.append(query.strip())
        if len(queries) > 5:
            embed = discord.Embed(description="You cannot link more than 5 mods in a message.", color=0x197482)
            await ctx.send(embed=embed)
        else:
            await self.search_nexus_for_query(ctx, queries)

    @link.error
    async def link_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(content="Please provide a mod name when using the link command.")


    @commands.hybrid_command(name='suggest-acronym', description='Suggest an acronym for the mod linking function to recognize')
    async def suggest_acronym(self, ctx, acronym, *, mod_name):
        queries = []

        if acronym in common_acronyms:
            return await ctx.send(content="That acronym already exists.", ephemeral=True)
        if 2 < len(acronym) < 15:
            if 2 < len(parse_query(mod_name)) < 100:
                queries.append(mod_name.strip())
                await self.search_nexus_for_query(ctx, queries, acronym=acronym)
            else:
                await ctx.send(content="The mod name you have entered is too long.", ephemeral=True)
        else:
            await ctx.send(content="Acronyms need to be between 3 and 10 characters long. If you feel this is an exception, contact an Architect and let them know.", ephemeral=True)

    @suggest_acronym.error
    async def suggest_acronym_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(content="This command requires two arguments: an acronym, and the mod name.")

class ModLinkButtons(discord.ui.View):
    def __init__(self, error_channel):
        super().__init__()
        self.timeout = 15
        self.error_channel = error_channel


    async def on_timeout(self):
        for item in self.children:
            self.remove_item(item)
        await self.message.edit(view=self)

    @discord.ui.button(label="❌", style=discord.ButtonStyle.gray)
    async def deletion_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        role_check = interaction.user.get_role(805197610046324756)
        if interaction.user.id in trusted_users or role_check:
            await interaction.message.delete()
            self.stop()
        else:
            await interaction.response.send_message(content="You don't have permission to do that.", ephemeral=True, delete_after=5)

    @discord.ui.button(label="❔", style=discord.ButtonStyle.gray)
    async def error_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        message_embeds = interaction.message.embeds
        error_content = message_embeds[0].to_dict()
        guild = interaction.guild
        user = interaction.user
        date = interaction.created_at

        error_report_embed = format_error_reports(error_content, guild, user, date)
        await self.error_channel.send(embed=error_report_embed)
        await interaction.response.send_message(content="The error has been reported. Thank you!", ephemeral=True, delete_after=5)

class AcronymSuggestionButtons(discord.ui.View):
    def __init__(self, architect_channel):
        super().__init__()
        self.timeout = 60
        self.architect_channel = architect_channel

    async def on_timeout(self):
        for item in self.children:
            self.remove_item(item)
        await self.message.edit(view=self)

    @discord.ui.button(label="Yes", style=discord.ButtonStyle.gray)
    async def suggestion_button_yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        message_embeds = interaction.message.embeds
        embed_content = message_embeds[0].to_dict()
        acronym_request_embed = format_error_reports(embed_content, guild=interaction.guild, user=interaction.user, date=interaction.created_at, title="Acronym Request Submitted:")

        view = AcronymApprovalButtons(embed_content)
        view.message = await self.architect_channel.send(embed=acronym_request_embed, view=view)
        self.clear_items()
        await self.message.edit(view=self)
        await interaction.response.send_message(content="Your request has be submitted for approval. Thank you!", ephemeral=True)



    @discord.ui.button(label="No", style=discord.ButtonStyle.gray)
    async def suggestion_button_no(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.clear_items()
        await self.message.edit(view=self)
        await interaction.response.send_message(content="Your request has been canceled.", ephemeral=True)


class AcronymApprovalButtons(discord.ui.View):
    def __init__(self, acronym_fields_list):
        super().__init__()
        self.timeout = None
        self.acronym_fields_list = acronym_fields_list

    @discord.ui.button(label="Approve", style=discord.ButtonStyle.gray)
    async def approval_button_yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        acronym_field = self.acronym_fields_list['fields'][2]
        query_text = self.acronym_fields_list['title']
        common_acronyms[acronym_field['value'].strip("'")] = query_text.strip('Search results for: ').strip("'")
        self.clear_items()
        await self.message.edit(view=self)
        await interaction.response.send_message(content=f"This acronym has been approved by {interaction.user.name}#{interaction.user.discriminator}.")

    @discord.ui.button(label="Reject", style=discord.ButtonStyle.gray)
    async def approval_button_no(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.clear_items()
        await self.message.edit(view=self)
        await interaction.response.send_message(content=f"This acronym has been declined by {interaction.user.name}#{interaction.user.discriminator}.")

async def setup(bot):
    await bot.add_cog(ModLinkSearch(bot))
