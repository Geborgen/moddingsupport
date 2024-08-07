"""
Copyright notice:

Information for commands partially created and primarily gathered by Geborgen

Copyright (C) 2022-2023 Geborgen
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
import random
from discord.ext import commands
from common_exceptions import sos_acronym
from common_exceptions import gamepass_gif
from typing import Mapping, List, Optional


class ModdingSupport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='source', description='Bot source code')
    async def source(self, ctx):
        embed = discord.Embed(description='[Source Code](https://github.com/Arbigate/moddingsupport)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='guide', description="Beginner's modding guide")
    async def guide(self, ctx):
        embed = discord.Embed(description="[Our Modding Guide](https://sites.google.com/view/skyrimsemoddingguide) \n[Phoenix's Beginner's Guide](https://thephoenixflavour.com/bg/)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='skse', description='SKSE tutorial')
    async def skse(self, ctx):
        embed = discord.Embed(title='SKSE Tutorial', description="The [Skyrim Script Extender](http://skse.silverlock.org/) is a tool that, well, extends Skyrim’s scripting functionality. It is absolutely essential and needed for many mods. \n\nInstallation is as simple as downloading the correct version and extracting to your game directory. The video outlines the process. \n\nFrom now on, you will launch Skyrim by launching SKSE through your mod manager. \n\n[Video Tutorial](https://youtu.be/ZuqfOw89vm0)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ae', description='Information about AE')
    async def ae(self, ctx):
        embed = discord.Embed(title='AE Info Board', description="November 11th, 2021, was Skyrim’s 10th anniversary. On that day, Bethesda released the **Anniversary Edition (AE)** update, which acts as an update to the base SSE game. Before the update, the version of the game was **1.5.97**, which we now refer to as the SE version. The current AE version is **1.6.1170**, but AE versions refer to any game version starting with **1.6**. The only mods that might not work across versions are most SKSE plugins. Make sure you are getting the correct version of those mods for the version of the game you have installed. Unless you have manually downgraded your game, you will be on the latest version of 1.6. \n\nThe AE update included four free Creation Club (CC) items: [Saints & Seducers](https://en.uesp.net/wiki/Skyrim:Saints_%26_Seducers), [Rare Curios](https://en.uesp.net/wiki/Skyrim:Rare_Curios), [Survival Mode](https://en.uesp.net/wiki/Skyrim:Survival_Mode), and [Fishing](https://en.uesp.net/wiki/Skyrim:Fishing). (The Creation Club mods are mods that are officially endorsed and published by Bethesda.) \n\nIn conclusion, there are two main versions of the game: **1.5** (SE)**, and **1.6** (AE). Make sure you're reading everything so you select the correct version of the SKSE mod you want. \n\nThis is not to be confused with the Anniversary Edition *upgrade* which is an entirely separate thing. This AE upgrade is a new DLC released by Bethesda, which includes all of the CC content (not including the four free items included with the *update*) which previously had to be purchased individually. \n\nThere is a very important distinction between the AE *update* and the *upgrade*. Many users will get confused by this, so make sure you understand it. \n\nIt is possible to downgrade your game, see -downgrade for more information.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='downgrade', description='Downgrading game tutorial')
    async def downgrade(self, ctx):
        embed = discord.Embed(title='How to Downgrade', description='If you want to use a version of Skyrim that is *not* 1.6.1170, you will need to downgrade your game using the [downgrade patcher](https://www.nexusmods.com/skyrimspecialedition/mods/57618). If you must downgrade, we recommend the "best of both worlds" file, which lets you keep your Creation Club content intact; but most mods are updated, and downgrading is not really necessary anymore. Remember to pay attention to the version for SKSE-based mods. \n\n[Full Tutorial](https://www.reddit.com/r/skyrimmods/comments/19esxy9/a_comprehensive_guide_to_downgrading_skyrim/)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='version', description='Breaks down versions of the game')
    async def version(self, ctx):
        embed = discord.Embed(title='What version of Skyrim should I get?', description="The first is **Skyrim Legendary Edition (LE)**. This refers to the original game released in 2011. It is also called Oldrim, but there is a difference between LE and Oldrim usually; LE refers to the base game with all DLCs, while Oldrim refers to just the base 2011 version of the game. This version of the game is outdated and we do not recommend it. \n\nThe second version is **Skyrim Special Edition (SSE)** which was released in 2016. It’s a full upgrade to Legendary Edition and was released separately on Steam. SSE includes every DLC. It also includes many engine fixes and graphical upgrades. No LE mod is compatible with SE by default (save most texture mods), however, the majority can easily be ported (more on that later). This guide will be focused on SSE because it’s the most supported.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='porting', description='Tutorial for porting mods', aliases=['converting', 'port', 'convert'])
    async def porting(self, ctx):
        embed = discord.Embed(description="[TLO's Converting Mods Tutorial](https://sites.google.com/view/skyrimsemoddingguide/the-guide/porting-mods)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='crash', description='What to do in the event of a crash')
    async def crash(self, ctx):
        embed = discord.Embed(title='Crash Resources', description="Use [this](https://www.nexusmods.com/skyrimspecialedition/mods/59818) mod to generate crash logs. \n\n[Reading SE Crash Logs Tutorial](https://docs.google.com/document/d/1Gw63VpT_PiiOXaHUeJvrjr3j9H-j-3N17ivxGA-CiTM/edit?usp=sharing) \n[Reading AE Crash Logs Tutorial](https://www.nexusmods.com/skyrimspecialedition/mods/75430) \n[Troubleshooting Guide](https://sites.google.com/view/skyrimsemoddingguide/the-guide/troubleshooting) \n[Stability Guide](https://www.youtube.com/watch?v=ucJkYLyRMso)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='modmanager', description='Mod manager comparison')
    async def modmanager(self, ctx):
        embed = discord.Embed(title='What mod manager should I use?', description='[Differences Breakdown](https://sites.google.com/view/skyrimsemoddingguide/the-guide/setup-workspace#h.cx65j1g77zn) \n[MO2 Download](https://www.nexusmods.com/skyrimspecialedition/mods/6194) \n[Vortex Download](https://www.nexusmods.com/about/vortex/) \n\nYou may see a lot of references to “Nexus Mod Manager”, or NMM. **DO NOT USE NMM.** Not only is it no longer officially maintained or even supported by modern tools, but it lacks many essential features and is known to directly modify game files.', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='reinstall', description='How to correctly reinstall the game')
    async def reinstall(self, ctx):
        embed = discord.Embed(description='[Clean Reinstall Tutorial](https://youtu.be/zQ5uNCKOKmI)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='laws', description='10 commandments of modding')
    async def laws(self, ctx):
        embed = discord.Embed(description="[Arbi's 10 Commandments of Modding](https://docs.google.com/document/d/1MTYjs5ofT0ISXFVfAZWssbWZ8KDcPeOoJ3FBpscTxyY/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='nemesis', description='Tutorial for Nemesis engine')
    async def nemesis(self, ctx):
        embed = discord.Embed(title='Nemesis Unlimited Behavior Engine', description="[Nemesis](https://www.nexusmods.com/skyrimspecialedition/mods/60033) is a modern replacement for Fore’s New Idles in Skyrim, or FNIS, a tool that allows for custom animation and behavior generation. You may see some mods requiring FNIS: FNIS is no longer needed. __All FNIS mods work with Nemesis__ and it will even generate an empty FNIS.esp for compatibility. The only thing Nemesis currently doesn’t support is creature animations. If you look for support with FNIS, you will most likely be redirected to Nemesis. [Here is a more in-depth comparison between the two.](https://www.youtube.com/watch?v=99OvhVogJ7c) \n\nNemesis is fairly simple to use and takes just a few clicks. Launch the program through your mod manager, check ONLY the mods you have installed, click 'update', and then 'launch'. Please refer to the video. \n\n[Video Tutorial](https://youtu.be/nB1-Z6RboxQ)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='dyndolod', description='Tutorial for DynDOLOD')
    async def dyndolod(self, ctx):
        embed = discord.Embed(title='DynDOLOD Guide', description='[Basic Guide](https://sites.google.com/view/skyrimsemoddingguide/the-guide/all-about-lod) \n[Advanced Guide](https://sites.google.com/view/skyrimsemoddingguide/advanced-topics/advanced-lod-guide) \n\n[Advanced Video Guide Part 1](https://www.youtube.com/watch?v=Xjzef1TT4Gk&list=PLQVRNa_qhFsrNmcAn80ImEh0HXiTsNUyY) \n-[Part 2](https://www.youtube.com/watch?v=jH7co25_JIo&list=PLQVRNa_qhFsrNmcAn80ImEh0HXiTsNUyY) \n-[Part 3](https://www.youtube.com/watch?v=nLVNXkxhJxI&list=PLQVRNa_qhFsrNmcAn80ImEh0HXiTsNUyY)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='cleaning', description='Tutorial for xEdit plugin cleaning')
    async def cleaning(self, ctx):
        embed = discord.Embed(description='[Cleaning Master Files Tutorial by Arbigate](https://docs.google.com/document/d/1ro3PiBbWimZSwYz1h4DaG_DnpiIFVwNmyqnV_SKdC8Q/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='navmesh', description='Tutorial for fixing deleted navmesh')
    async def navmesh(self, ctx):
        embed = discord.Embed(description='[Fixing Deleted Navmesh Tutorial by Arbigate](https://docs.google.com/document/d/1tTu3N4l5FTs8zb5sNrTvkHFXgrXvQC7WVdT_XJnaXe4/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='eslify', description='Tutorial for ESL flagging plugins')
    async def eslify(self, ctx):
        embed = discord.Embed(description='[ESL Flagging Plugins Tutorial](https://www.nexusmods.com/skyrimspecialedition/mods/21618)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='vanillastart', description='How to fix broken vanilla intro')
    async def vanillastart(self, ctx):
        embed = discord.Embed(title='Broken Vanilla Intro Fix', description='Use [Alternate Start - Live Another Life](https://www.nexusmods.com/skyrimspecialedition/mods/272) to make your character, then wait a minute or so and let your scripts load. Then select vanilla start. \n\nAdditionally, try [this](https://www.nexusmods.com/skyrimspecialedition/mods/8004) fix. \n\nSome other alternate start mods are [Skyrim Unbound Reborn](https://www.nexusmods.com/skyrimspecialedition/mods/27962), [Realm of Lorkhan](https://www.nexusmods.com/skyrimspecialedition/mods/18223), and [Optional Quick Start](https://www.nexusmods.com/skyrimspecialedition/mods/63953).', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='darkface', description='Dark face bug fix')
    async def name(self, ctx):
        embed = discord.Embed(title="Dark Face Bug Fix", description="[Info Board](https://sites.google.com/view/skyrimsemoddingguide/advanced-topics/facegen-the-dark-face-bug) \n\n[Face Discoloration Fix Download](https://www.nexusmods.com/skyrimspecialedition/mods/42441) \n*Please note that this only fixes the dark tint, and doesn't fix the actual facegen issue.* \n\n[EasyNPC Download](https://www.nexusmods.com/skyrimspecialedition/mods/52313) \n*This tool will merge all of your face data into one plugin.*", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='loadorder', description='Load order resources', aliases=['loot'])
    async def loadorder(self, ctx):
        embed = discord.Embed(title='Load Order Resources', description="[LOOT Download](https://loot.github.io/) \n[LOOT Basic Tutorial](https://www.youtube.com/watch?v=fyvwslyKiog) \n\n[Load Order Basics](https://www.youtube.com/watch?v=Ncv_FWQUw0k)\n[Load Order Structure Info](https://sites.google.com/view/skyrimsemoddingguide/the-guide/load-order?authuser=0) \n\nPlease note that manually sorting your load order is proper modding practice, as LOOT is often incorrect. If you are using LOOT, make sure to manually verify that it is correct. Always read mod pages, and if you're comfortable in xEdit, use xEdit to verify correct load order. For new modders, LOOT can provide a good baseline, but should not be completely relied upon.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='cycle', description='Cyclic interaction information', aliases=['cycles'])
    async def cycle(self, ctx):
        embed = discord.Embed(title='Vortex Cyclic Interactions', description='When encountering a cyclical load order in vortex, open the panel showing the graphical view of the cycle by clicking on the text in the pop-up. Once in this panel you pick the mod whose files you want to load in over the other mods. (for example, you would want a rug texture overhaul to load over the general texture overhaul) Right click it, and choose load last among connected. Repeat until the cycle goes away.', color=0x197482)
        embed.set_image(url="https://media.discordapp.net/attachments/849891362685976587/862435864093392916/caption-8.gif")
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='performance', description='Guide to increase performance')
    async def performance(self, ctx):
        embed = discord.Embed(description='[Performance Guide](https://sites.google.com/view/skyrimsemoddingguide/the-guide/performance)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='patching', description='Guide for patching mods')
    async def patching(self, ctx):
        embed = discord.Embed(description='[Patching Guide](https://sites.google.com/view/skyrimsemoddingguide/the-guide/patching)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='corrupt', description='Corrupted game save resources', aliases=['fallrim'])
    async def corrupt(self, ctx):
        embed = discord.Embed(title='Save Corruption Resources', description='When playing a modded game, **always** make frequent saves that **are not** quick or autosaves. **Do not** save during heavy script load areas e.g. combat. **Do not** delete old saves. \n\n[FallrimTools](https://www.nexusmods.com/skyrimspecialedition/mods/5031) \n*READ THE MOD PAGE*', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='essentials', description='List of essential mods')
    async def essentials(self, ctx):
        embed = discord.Embed(description='[Essential Bugfixes & Tools List](https://github.com/Geborgen/usefulmods)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='script', description='Script info board')
    async def script(self, ctx):
        embed = discord.Embed(description="[Monitor's Script Info Board](https://sites.google.com/view/skyrimsemoddingguide/advanced-topics/script-heavy-mods)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='modlimit', description='Mod limit info board')
    async def modlimit(self, ctx):
        embed = discord.Embed(description='[255 Mod Limit for SE/AE Info by Monitor](https://sites.google.com/view/skyrimsemoddingguide/advanced-topics/255-plugin-limit)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='enb', description='ENB info board')
    async def enb(self, ctx):
        embed = discord.Embed(title="ENB Info Board", description="An ENB is, essentially, a complete replacement of the game's lighting and shaders, in addition to any weather or lighting mods you might have installed. Two different presets can change the aesthetic of a game drastically; you should choose wisely and find one suited to your weather mod and/or game aesthetic. Do you want fairytale fantasy? Real life? Dark Souls? There’s a preset for every visual persuasion. \n\n[ENB Guide](https://sites.google.com/view/skyrimsemoddingguide/the-guide/enb-reshade) \n[ENB Settings Breakdown](https://stepmodifications.org/wiki/Guide:ENBSeries_INI)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ini', description='Ini resources')
    async def ini(self, ctx):
        embed = discord.Embed(title='INI Resources', description="[INI Settings Breakdown](https://stepmodifications.org/wiki/Guide:Skyrim_Configuration_Settings#SkyrimPrefs.ini) \n[BethINI Download](https://www.nexusmods.com/skyrimspecialedition/mods/4875) \n[BethINI Video Tutorial](https://www.youtube.com/watch?v=NI8ezwpZQFw) \nMake sure you set your .INI path correctly in the setup tab, pointing toward your MO2 profile, or else your changes won’t take effect. This is due to MO2’s Virtual File System (VFS) which uses its own version of Skyrim’s .INIs, instead of the default ones in documents.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='modlist', description='Modlist sharing resources')
    async def modlist(self, ctx):
        embed = discord.Embed(title='Tools for Sharing Modlists', description='[Modwat.ch Download](https://modwat.ch/) \n[Modwat.ch for Vortex](https://www.nexusmods.com/site/mods/152) \n[Load Order Library](https://loadorderlibrary.com/)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='wabbajack', description="Information about Wabbajack modlists")
    async def wabbajack(self, ctx):
        embed = discord.Embed(title='Wabbajack Modlists', description='[Wabbajack](https://www.wabbajack.org/) is a tool that allows users to automatically install complete modlists for Skyrim and other games. These lists are fully patched and complete experiences. During installation, the list will download mods from Nexus; it does not come packaged with mods, so it is not piracy. Nexus premium is recommended, or else you will find yourself manually clicking through each mod; most lists come with hundreds, often over a thousand mods. \n\nYou can use the [skychart][https://skychart.wabbajack.org/] or [wizard](https://wizard.wabbajack.org/) to find the list for you. Make sure you full read all instructions, as each list might be slightly different.', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ussep', description='Link to USSEP')
    async def ussep(self, ctx):
        embed = discord.Embed(title='Unofficial Skyrim Special Edition Patch', description='[USSEP Download](https://www.nexusmods.com/skyrimspecialedition/mods/266) \n[Old Version (1.5.97)](https://www.nexusmods.com/Core/Libs/Common/Widgets/DownloadPopUp?id=209150&game_id=1704) \n[Non-Arthmoor Alternatives](https://www.reddit.com/r/skyrimmods/comments/usamua/unarthmoored_ussep_compendium/)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='tudm', description='Link to TUDM')
    async def tudm(self, ctx):
        embed = discord.Embed(title="The Ultimate Dodge Mod", description="[TUDM Reborn Download](https://www.nexusmods.com/skyrimspecialedition/mods/63000) \n\nCompatible with AE. Please note that your vanilla sneak key will become your dodge key. You can configure the key you use for sneaking in TUDM's MCM.", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='synthesis', description='Link to Synthesis patcher')
    async def synthesis(self, ctx):
        embed = discord.Embed(title='Synthesis Patcher', description='[Download](https://github.com/Mutagen-Modding/Synthesis/wiki/Installation) \n[Guide](https://www.youtube.com/watch?v=s7luh0hMMAU)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='xbox', description='Xbox mod recommendations')
    async def xbox(self, ctx):
        embed = discord.Embed(description="[Sovereign's Noteworthy Xbox Mods](https://docs.google.com/document/d/1_wwawgIc2NFe-BYZptcJN9kli92zDkKT4Prg5dVqgpI/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='ps4', description='PlayStation mod recommendations')
    async def ps4(self, ctx):
        embed = discord.Embed(description="[Nick's Noteworthy PlayStation Mods](https://docs.google.com/document/d/1NueH5pWdWjgBaH5AVyiJGfy8jaDyNYuhiXgRNfDZsIc/edit?usp=sharing)", color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='sinitar', description='Essay on Sinitar')
    async def sinitar(self, ctx):
        embed = discord.Embed(description='[He had a 29 page essay written about him, should say something.](https://docs.google.com/document/d/1F1-6lF8dI4i2Zz8iT-bv_Ci1VO9MSU4MiSUrT5JqgHA/edit?usp=sharing)', color=0x197482)
        await ctx.send(embed=embed)

    @commands.hybrid_command(name='sos', description='Links a random SOS mod')
    async def sos(self, ctx):
        random_sos = random.choice(list(sos_acronym))
        await ctx.send(random_sos)

    @commands.hybrid_command(name='gamepass', description='Sends a random "skse does not work with gamepass" gif')
    async def gamepass(self, ctx):
        gamepass_meme = random.choice(list(gamepass_gif))
        await ctx.send(gamepass_meme)

    @commands.hybrid_command(name='rtfm', description='Sends a "read the manual" image')
    async def rtfm(self, ctx):
        await ctx.send('https://i.imgur.com/k3qSKbl.png')

    @commands.hybrid_command(name='tryitandsee', description='Try it and see')
    async def tryitandsee(self, ctx):
        await ctx.send('https://tryitands.ee/')

    @commands.hybrid_command(name='dontasktoask', description='Sends a message about not asking to ask a question')
    async def dontasktoask(self, ctx):
        await ctx.send('https://dontasktoask.com/')

    @commands.hybrid_command(name='stefan', description="Don't listen to him...")
    async def stefan(self, ctx):
        await ctx.send('ignore him')

    @commands.hybrid_command(name='ping', description='Checks the ping of bot')
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! Bot latency is ``{round(self.bot.latency*1000)} ms``')


class HelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.page_number = 0
        self.help_body = ["-guide (beginner's modding guide) \n-skse (SKSE tutorial) \n-ae (information about AE) \n-downgrade (downgrading game tutorial) \n-version (breaks down the versions of the game) \n-porting / -converting (tutorial for porting mods) \n-crash (what to do in the event of a crash) \n-modmanager (mod manager comparison) \n-reinstall (how to correctly reinstall the game) \n-laws (10 Commandments of Modding™️)", "-nemesis (tutorial for Nemesis engine) \n-dyndolod (tutorial for DynDOLOD) \n-cleaning (xEdit plugin cleaning) \n-navmesh (fixing deleted navmesh) \n-eslify (ESL flagging plugins) \n-vanillastart (broken vanilla intro fix) \n-darkface (dark face bug fix) \n-loadorder / -loot (load order resources \n-cycle (cyclic interaction information) \n-performance (performance guide) \n-patching (patching guide) \n-corrupt / -fallrim (corrupted save game resources)", "-essentials (list of essential mods) \n-script (script info board) \n-modlimit (mod limit info board) \n-enb (ENB info board) \n-ini (ini resources) \n-modlist (modlist sharing resources) \n-wabbajack (Wabbajack modlist information) \n-ussep (link to USSEP) \n-tudm (link to TUDM) \n-synthesis (link to Synthesis patcher) \n-xbox (Xbox mod recommendations) \n-ps4 (PlayStation mod recommendations)", "-sinitar (essay on Sinitar) \n-sos (returns a random 'SOS' mod) \n-gamepass (SKSE does not work with it) \n-rtfm (read the [redacted] manual) \n-tryitandsee (please do this) \n-dontasktoask (seriously, just ask your question) \n-stefan (ignore him) \n-source (links bot source code) \n/link (links mods, separate multiple with commas) \n/suggest-acronym (requests acronym to be added to mod linking", "/attack (attacks the Augur of Dunlain bot) \n/damage-leaderboard (shows top 10 attackers against Augur of Dunlain) \n/check-damage (checks how much damage has been done to Augur of Dunlain)"]

    async def send_bot_help(self, mapping: Mapping[Optional[commands.Cog], List[commands.Command]]):
        view = HelpButtons(HelpCommand())
        ctx = self.context
        embed = discord.Embed(title="Modding Support Help", description=self.help_body[0], color=0x197482)
        embed.set_footer(text="Page 1/5 | Use /ping to return latency")
        view.message = await ctx.send(embed=embed, view=view)


class HelpButtons(discord.ui.View):
    def __init__(self, help_command):
        super().__init__()
        self.help_command = help_command
        self.timeout = 120

    async def on_timeout(self):
        for item in self.children:
            self.remove_item(item)
        await self.message.edit(view=self)

    @discord.ui.button(label="◀ Previous Page", style=discord.ButtonStyle.gray)
    async def help_button_left(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.help_command.page_number > 0:
            self.help_command.page_number -= 1
            embed = discord.Embed(title="Modding Support Help", description=self.help_command.help_body[self.help_command.page_number], color=0x197482)
            embed.set_footer(text=f"Page {self.help_command.page_number + 1}/5 | Use /ping to return latency")
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.defer()

    @discord.ui.button(label="Next Page ▶", style=discord.ButtonStyle.gray)
    async def help_button_right(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.help_command.page_number < 4:
            self.help_command.page_number += 1
            embed = discord.Embed(title="Modding Support Help", description=self.help_command.help_body[self.help_command.page_number], color=0x197482)
            embed.set_footer(text=f"Page {self.help_command.page_number + 1}/5 | Use /ping to return latency")
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.defer()


async def setup(bot):
    await bot.add_cog(ModdingSupport(bot))
