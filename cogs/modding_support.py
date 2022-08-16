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
import random
from discord.ext import commands
from modlink_exceptions import sos_acronym


class ModdingSupport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='source')
    async def source(self, ctx):
        embed = discord.Embed(description='[Source Code](https://github.com/Geborgen/moddingsupport)')
        await ctx.send(embed=embed)

    @commands.command(name='guide')
    async def guide(self, ctx):
        embed = discord.Embed(description='[Modding Guide](https://docs.google.com/document/d/1jTXnuuLZQ201rLRFw0TbxDnBDO9DqZDcCqFIJJSXCDU/edit?usp=sharing)')
        await ctx.send(embed=embed)

    @commands.command(name='skse')
    async def skse(self, ctx):
        embed = discord.Embed(title='SKSE Tutorial', description= 'Launch your game at least once. Go [here](http://skse.silverlock.org/) and download; **__MAKE SURE YOU GET THE RIGHT VERSION FOR YOUR GAME.__** \nDrag the files from the image below into your game folder, located at \n Steam/steamapps/common/Skyrim Special Edition. \n\nKeep in mind, from now on you will have to launch your game from skse_loader.exe (do not launch through Steam). If you use MO2, it will add an executable there automatically. \n\n[Video Tutorial](https://www.youtube.com/watch?v=tdiFIL_02dI)')
        embed.set_image(url='https://i.imgur.com/E2HoLOc.png')
        await ctx.send(embed=embed)

    @commands.command(name='ae')
    async def ae(self, ctx):
        embed = discord.Embed(title='AE Info Board', description="The Anniversary Edition *update* was forced for ALL users, while the *upgrade* is a new DLC that includes CC content. Everyone has the AE update, which brings your game version from **1.5.97** to **1.6.353**. \n\nAny mod that uses an SKSE DLL will not work on AE 1.6.353 unless it has been updated by the author. At this point, most mods are updated. \n\nMake sure your SKSE mods match your game version. You can check by seeing what file you downloaded, usually they will indicate AE compatibility. \n\nIt is possible to downgrade your game (not recommended for average users). See -downgrade for more info.")
        await ctx.send(embed=embed)

    @commands.command(name='downgrade')
    async def downgrade(self, ctx):
        embed = discord.Embed(title='How to Downgrade', description='It is possible to downgrade your game from 1.6.353 to 1.5.97 for mod compatibility. This is becoming more and more obsolete as more mods get updated, but the option is still avaiable. \n\n[Downgrade Patcher](https://www.nexusmods.com/skyrimspecialedition/mods/57618) \n[Instructions](https://www.youtube.com/watch?v=r2XSWUkOKz0)')
        await ctx.send(embed=embed)

    @commands.command(name='version')
    async def version(self, ctx):
        embed = discord.Embed(title='What version of Skyrim should I get?', description='Legendary Edition (LE): The original version of Skyrim released in 2011, with all DLC. Oldrim refers to the base game without DLC. This version is mostly unsupported. \n\nSpecial Edition (SE): Updated version of the game, released in 2016. Includes all DLC and major graphical/engine updates. Most mods are released here, and you will get the most support for SE.')
        await ctx.send(embed=embed)

    @commands.command(name='porting', aliases=['converting', 'port', 'convert'])
    async def porting(self, ctx):
        embed = discord.Embed(description ="[TLO's Converting Mods Tutorial](https://pastebin.com/xXixFzib)")
        await ctx.send(embed=embed)

    @commands.command(name='crash')
    async def crash(self, ctx):
        embed = discord.Embed(title='Crash Resources', description="Use [this](https://www.nexusmods.com/skyrimspecialedition/mods/21294) mod to generate crash logs. \nUse [this](https://www.nexusmods.com/skyrimspecialedition/mods/59596) instead if you're on AE. \nUse [this](https://www.nexusmods.com/skyrimspecialedition/mods/59818) if you're on VR. \n\n[Reading Crash Logs Tutorial](https://pastebin.com/q7fc8FvF) \n[Troubleshooting Checklist](https://pastebin.com/fLuwitW3) \n[Stability Guide](https://www.youtube.com/watch?v=ucJkYLyRMso)")
        await ctx.send(embed=embed)

    @commands.command(name='modmanager')
    async def modmanager(self, ctx):
        embed = discord.Embed(title='What mod manager should I use?', description='[Differences Breakdown](https://pastebin.com/5gKqk5LN) \n[MO2 Download](https://www.nexusmods.com/skyrimspecialedition/mods/6194) \n[Vortex Download](https://www.nexusmods.com/about/vortex/) \n\nYou may see a lot of references to “Nexus Mod Manager” or NMM. DO NOT USE NMM. Not only is it no longer officially maintained or even supported by modern tools, it is known to directly modify game files and lacks essential features.')
        await ctx.send(embed=embed)

    @commands.command(name='reinstall')
    async def reinstall(self, ctx):
        embed = discord.Embed(description='[Clean Reinstall Tutorial](https://www.youtube.com/watch?v=zQ5uNCKOKmI)')
        await ctx.send(embed=embed)

    @commands.command(name='laws')
    async def laws(self, ctx):
        embed = discord.Embed(description="[Arbi's 10 Commandments of Modding](https://pastebin.com/YpJ6nSJ8)")
        await ctx.send(embed=embed)

    @commands.command(name='nemesis')
    async def nemesis(self, ctx):
        embed = discord.Embed(title='Nemesis Unlimited Behavior Engine', description="Nemesis is the modern replacement for FNIS. It is essentially the same thing, you don't need FNIS at all if you use Nemesis. It will even generate an empty FNIS.esp for compatibility. The only thing it doesn't support are creature animations. \n\n[Download](https://www.nexusmods.com/skyrimspecialedition/mods/60033) \n[Instructions](https://www.youtube.com/watch?v=ki2bghy2Mvo) \n[Instructions for Vortex](https://www.youtube.com/watch?v=W9hrvc8ync4) \n*Please keep in mind that these tutorials use Nemesis from GitHub; you can now just download from Nexus and install through your mod manager normally, then pick up from there.* \n\nWhitelist Nemesis in your antivirus/turn off real time protection if you have issues. Also make sure you are installing mods for the correct version of your game.")
        await ctx.send(embed=embed)

    @commands.command(name='dyndolod')
    async def dyndolod(self, ctx):
        embed = discord.Embed(title='DynDOLOD Guide', description='[Guide by Kiloee & Geborgen](https://docs.google.com/document/d/1n1Bqh1a2kD_Kgg8Hfxc3GZtpYMORP6lYg76kWwP4rOo/edit?usp=sharing) \n[Video Tutorial](https://www.youtube.com/watch?v=encZYHEeQrQ)')
        await ctx.send(embed=embed)

    @commands.command(name='cleaning')
    async def cleaning(self, ctx):
        embed = discord.Embed(description='[Cleaning Master Files Tutorial by Arbigate](https://docs.google.com/document/d/1ro3PiBbWimZSwYz1h4DaG_DnpiIFVwNmyqnV_SKdC8Q/edit?usp=sharing)')
        await ctx.send(embed=embed)

    @commands.command(name='navmesh')
    async def navmesh(self, ctx):
        embed = discord.Embed(description='[Fixing Deleted Navmesh Tutorial by Arbigate](https://docs.google.com/document/d/1tTu3N4l5FTs8zb5sNrTvkHFXgrXvQC7WVdT_XJnaXe4/edit?usp=sharing)')
        await ctx.send(embed=embed)

    @commands.command(name='eslify')
    async def eslify(self, ctx):
        embed = discord.Embed(description='[ESL Flagging Plugins Tutorial](https://www.nexusmods.com/skyrimspecialedition/mods/21618)')
        await ctx.send(embed=embed)

    @commands.command(name='vanillastart')
    async def vanillastart(self, ctx):
        embed = discord.Embed(title='Broken Vanilla Intro Fix', description='Use [this](https://www.nexusmods.com/skyrimspecialedition/mods/272) mod to make your character, then wait a few minutes and let your scripts load. Then select vanilla start. \n\nAdditionally, try [this](https://www.nexusmods.com/skyrimspecialedition/mods/8004) fix.')
        await ctx.send(embed=embed)

    @commands.command(name='darkface')
    async def name(self, ctx):
        embed = discord.Embed(title="Dark Face Bug Fix", description="[Info Board](https://www.reddit.com/r/skyrimmods/comments/n6gio6/guide_the_dark_face_bug_and_what_causes_it_and/) \n\n[Face Discoloration Fix Download](https://www.nexusmods.com/skyrimspecialedition/mods/42441) \n*Please note that this only fixes the dark tint, and doesn't fix the actual facegen issue.* \n\n[EasyNPC Download](https://www.nexusmods.com/skyrimspecialedition/mods/52313) \n*This tool will merge all of your face data into one plugin.*")
        await ctx.send(embed=embed)

    @commands.command(name='loadorder', aliases=['loot'])
    async def loadorder(self, ctx):
        embed = discord.Embed(title='Load Order Resources', description='[LOOT Download](https://loot.github.io/) \n[LOOT Basic Tutorial](https://www.youtube.com/watch?v=fyvwslyKiog) \n\n[Load Order Basics](https://www.youtube.com/watch?v=Ncv_FWQUw0k)\n[Load Order Structure Info](https://skyrimseblog.wordpress.com/load-order-structure/)')
        await ctx.send(embed=embed)

    @commands.command(name='corrupt', aliases=['fallrim'])
    async def corrupt(self, ctx):
        embed = discord.Embed(title='Save Corruption Resources', description='When playing a modded game, **always** make frequent saves that **are not** quick or autosaves. **Do not** save during heavy script load areas e.g. combat. **Do not** delete old saves. \n\n[FallrimTools](https://www.nexusmods.com/skyrimspecialedition/mods/5031) \nREAD THE MOD PAGE')
        await ctx.send(embed=embed)

    @commands.command(name='essentials')
    async def essentials(self, ctx):
        embed = discord.Embed(description='[Essential Bugfixes & Tools List](https://github.com/Geborgen/usefulmods)')
        await ctx.send(embed=embed)

    @commands.command(name='script')
    async def script(self, ctx):
        embed = discord.Embed(description="[Monitor's Script Info Board](https://pastebin.com/s3aUUhv2)")
        await ctx.send(embed=embed)

    @commands.command(name='modlimit')
    async def modlimit(self, ctx):
        embed = discord.Embed(description='[255 Mod Limit for SE/AE Info by Monitor](https://pastebin.com/Hu8vnpQ3)')
        await ctx.send(embed=embed)

    @commands.command(name='enb')
    async def enb(self, ctx):
        embed = discord.Embed(title="ENB Info Board", description="An ENB is, essentially, a complete replacement of the game's lighting and shaders, *in addition* to any weather or lighting mods you might have installed. Two different presets can change the aesthetic of a game drastically; you should choose wisely and find one suited to your weather mod and/or game aesthetic. Do you want fairytale fantasy? Real life? Dark Souls? There’s a preset for every visual persuasion. \n\nEvery ENB has installation instructions on the mod page. You should know the basic steps however; download the most recent ENB binaries [here](http://enbdev.com/download_mod_tesskyrimse.htm) and extract ONLY the two .DLL files in the WrapperVersion folder to your game directory. Then download the preset of your choice and extract to your game directory. \n\n[ENB Settings Breakdown](https://stepmodifications.org/wiki/Guide:ENBSeries_INI)")
        await ctx.send(embed=embed)

    @commands.command(name='ini')
    async def ini(self, ctx):
        embed = discord.Embed(title='INI Resources', description='[INI Settings Breakdown](https://stepmodifications.org/wiki/Guide:Skyrim_Configuration_Settings#SkyrimPrefs.ini) \n[BethINI Download](https://www.nexusmods.com/skyrimspecialedition/mods/4875) \n*Instructions for BethINI are on the mod page.*')
        await ctx.send(embed=embed)

    @commands.command(name='modlist')
    async def modlist(self, ctx):
        embed = discord.Embed(title='Tools for Sharing Modlists', description='[Modwat.ch Download](https://modwat.ch/) \n[Modwat.ch for Vortex](https://www.nexusmods.com/site/mods/152) \n[Load Order Library](https://loadorderlibrary.com/)')
        await ctx.send(embed=embed)

    @commands.command(name='ussep')
    async def ussep(self, ctx):
        embed = discord.Embed(title='Unofficial Skyrim Special Edition Patch', description='[USSEP Download](https://www.nexusmods.com/skyrimspecialedition/mods/266) \n[Old Version (pre-AE)](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=209150&game_id=1704) \n[Non-Arthmoor Alternatives](https://www.reddit.com/r/skyrimmods/comments/usamua/unarthmoored_ussep_compendium/)')
        await ctx.send(embed=embed)

    @commands.command(name='tudm')
    async def tudm(self, ctx):
        embed = discord.Embed(title="The Ultimate Dodge Mod", description="[TUDM Reborn Download](https://www.nexusmods.com/skyrimspecialedition/mods/63000) \n\nCompatible with AE. Please note that your vanilla sneak key will become your dodge key. You can configure the key you use for sneaking in TUDM's MCM.")
        await ctx.send(embed=embed)

    @commands.command(name='synthesis')
    async def synthesis(self, ctx):
        embed = discord.Embed(title='Synthesis Patcher', description='[Download](https://github.com/Mutagen-Modding/Synthesis/wiki/Installation) \n[Guide](https://www.youtube.com/watch?v=s7luh0hMMAU)')
        await ctx.send(embed=embed)

    @commands.command(name='xbox')
    async def xbox(self, ctx):
        embed = discord.Embed(description="[Sovereign's Noteworthy Xbox Mods](https://pastebin.com/J8i5g18L)")
        await ctx.send(embed=embed)

    @commands.command(name='ps4')
    async def ps4(self, ctx):
        embed = discord.Embed(description="[Nick's Noteworthy PlayStation Mods](https://pastebin.com/pTk9E2w7)")
        await ctx.send(embed=embed)

    @commands.command(name='sinitar')
    async def sinitar(self, ctx):
        embed = discord.Embed(description='[He had a 29 page essay written about him, should say something.](https://docs.google.com/document/d/1F1-6lF8dI4i2Zz8iT-bv_Ci1VO9MSU4MiSUrT5JqgHA/edit?usp=sharing)')
        await ctx.send(embed=embed)

    @commands.command(name='sos')
    async def sos(self, ctx):
        random_sos = random.choice(list(sos_acronym))
        await ctx.send(random_sos)

    @commands.command(name='rtfm')
    async def rtfm(self, ctx):
        await ctx.send('https://i.imgur.com/k3qSKbl.png')

    @commands.command(name='tryitandsee')
    async def tryitandsee(self, ctx):
        await ctx.send('https://tryitands.ee/')

    @commands.command(name='dontasktoask')
    async def dontasktoask(self, ctx):
        await ctx.send('https://dontasktoask.com/')

    @commands.command(name='stefan')
    async def stefan(self, ctx):
        await ctx.send('ignore him')

    @commands.command(name='help')
    async def help(self, ctx, pages = None):
        help_body = ["-guide (beginner's modding guide) \n-skse (SKSE tutorial) \n-ae (information about AE) \n-downgrade (downgrading game tutorial) \n-version (breaks down the versions of the game) \n-porting / -converting (tutorial for porting mods) \n-crash (what to do in the event of a crash) \n-modmanager (mod manager comparison) \n-reinstall (how to correctly reinstall the game) \n-laws (10 Commandments of Modding™️)", "-nemesis (tutorial for Nemesis engine) \n-dyndolod (tutorial for DynDOLOD) \n-cleaning (xEdit plugin cleaning) \n-navmesh (fixing deleted navmesh) \n-eslify (ESL flagging plugins) \n-vanillastart (broken vanilla intro fix) \n-darkface (dark face bug fix) \n-loadorder / -loot (load order resources) \n-corrupt / -fallrim (corrupted save game resources)", "-essentials (list of essential mods) \n-script (script info board) \n-modlimit (mod limit info board) \n-enb (ENB info board) \n-ini (ini resources) \n-modlist (modlist sharing resources) \n-ussep (link to USSEP) \n-tudm (link to TUDM) \n-synthesis (link to Synthesis patcher) \n-xbox (Xbox mod recommendations) \n-ps4 (PlayStation mod recommendations)", "-sinitar (essay on Sinitar) \n-sos (returns a random 'SOS' mod) \n-rtfm (read the [redacted] manual) \n-tryitandsee (please do this) \n-dontasktoask (seriously, just ask your question) \n-stefan (ignore him)"]
        try:
            if pages is None:
                embed = discord.Embed(title='Modding Support Help', description=help_body[0])
                embed.set_footer(text=f"\n \nPage 1/4 | Type -ping to return latency")
                await ctx.send(embed=embed)
            elif int(pages) > 4 or int(pages) < 1:
                await ctx.send("Valid page numbers range from 1 to 4.")
            else:
                embed = discord.Embed(title='Modding Support Help', description=help_body[int(pages)-1])
                embed.set_footer(text=f"\n \nPage {pages}/4 | Type -ping to return latency")
                await ctx.send(embed=embed)
        except ValueError:
            await ctx.send("Valid page numbers range from 1 to 4; words are not accepted.")

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! Bot latency is ``{round(self.bot.latency*1000)} ms``')

#NOTE: USE THIS FORMAT WHEN ADDING NEW COMMANDS:

#    @commands.command(name='name', aliases=['alias1', 'alias2'])
#    async def name(self, ctx):
#        embed = discord.Embed(title='title', description='description')
#        await ctx.send(embed=embed)

#Do not put a space after \n
#Hyperlink format is [text](link)

def setup(bot):
    bot.add_cog(ModdingSupport(bot))

