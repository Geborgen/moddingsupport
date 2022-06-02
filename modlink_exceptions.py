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

exceptions = {
    'skse': 'https://skse.silverlock.org/',
    'enbseries': 'http://enbdev.com/download_mod_tesskyrimse.htm',
    'lux': 'https://www.nexusmods.com/skyrimspecialedition/mods/43158',
    'enb light': 'https://www.nexusmods.com/skyrimspecialedition/mods/22574',
    'sky idles': 'https://www.nexusmods.com/skyrimspecialedition/mods/45794',
    'wabbajack': 'https://www.wabbajack.org',
    'open cities': 'https://www.afkmods.com/index.php?/files/file/1905-open-cities-skyrim/',
    'nordic ui': 'https://www.nexusmods.com/skyrimspecialedition/mods/49881'
}

false_adult = [
    'maximum carnage',
    'vigilant',
    'glenmoril',
    'wico',
    'enhanced blood textures'
]

le_modlink_exceptions = [
    'skyrim 2020',
    'skyrim 2020 parallax',
    'pi-cho',
    'wico'
]

se_modlink_exceptions = [

]

common_acronyms = {
    'elfx': 'Enhanced Lights and FX',
    'nff': 'Nether Follower Framework',
    'ussep': 'Unofficial Skyrim Special Edition Patch',
    'mo2': 'Mod Organizer 2',
    'lotd': 'Legacy of the Dragonborn',
    'icow': 'Immersive College of Winterhold',
    'nemesis': 'Nemesis Unlimited Behavior Engine',
    'cgo': 'Combat Gameplay Overhaul',
    'mbo': 'Movement Behavior Overhaul',
    'jbo': 'Jump Behavior Overhaul',
    'tdm': 'True Directional Movement',
    'dar': 'Dynamic Animation Replacer'
}

sos_acronym = {
    'Sabrecats of Skyrim': 'https://www.nexusmods.com/skyrim/mods/37719',
    'Sales Overflow Solved': 'https://www.nexusmods.com/skyrimspecialedition/mods/41625',
    'Scallions of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/53205',
    'Scarecrows of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/39575',
    'Scarves of Skyrim': 'https://www.nexusmods.com/skyrim/mods/16660/',
    'Scribes of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/50008',
    'Sea of Spirits': 'https://www.nexusmods.com/skyrimspecialedition/mods/4781',
    'Seagulls of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/52153',
    'Seasons of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/62861',
    'Shadows of Sunlight': 'https://www.nexusmods.com/skyrimspecialedition/mods/41368',
    'Sharpen Other Swords': 'https://www.nexusmods.com/skyrimspecialedition/mods/52723',
    'Sharpening Oversampling Shader': 'https://www.nexusmods.com/skyrimspecialedition/mods/45295',
    'Shields of Skyrim': 'https://www.nexusmods.com/skyrim/mods/21988',
    'Sigils of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/54108',
    'Signs of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/22292',
    'Simple Obvious Spell-crafting': 'https://www.nexusmods.com/skyrimspecialedition/mods/48621',
    'Simple Offence Suppression': 'https://www.nexusmods.com/skyrimspecialedition/mods/41764',
    'Simple Overwhelming Slaying': 'https://www.nexusmods.com/skyrimspecialedition/mods/46324',
    'Simply Overflowing Salt': 'https://www.nexusmods.com/skyrimspecialedition/mods/48819/',
    'Sink or Swim': 'https://www.nexusmods.com/skyrimspecialedition/mods/42962',
    'Skaven of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/46519',
    'Skyrim Outfit System': 'https://www.nexusmods.com/skyrimspecialedition/mods/42162',
    'Sleeping on Solstheim': 'https://www.nexusmods.com/skyrimspecialedition/mods/46236',
    'Slip off Slopes': 'https://www.nexusmods.com/skyrimspecialedition/mods/45886',
    'Sloads of Skyrim': 'https://www.nexusmods.com/skyrim/mods/21771',
    'Smart Optimal Salves': 'https://www.nexusmods.com/skyrimspecialedition/mods/48479',
    'Sojourn over Signs': 'https://www.nexusmods.com/skyrimspecialedition/mods/51567',
    'Solstheim Objects SMIMed': 'https://www.nexusmods.com/skyrimspecialedition/mods/53779',
    'Sounds of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/8286?',
    'Sprawling Open Solitude': 'https://www.nexusmods.com/skyrimspecialedition/mods/46432',
    'Spread Our Spells': 'https://www.nexusmods.com/skyrimspecialedition/mods/46010',
    'Staff of Shalidor': 'https://www.nexusmods.com/skyrimspecialedition/mods/13764',
    'Staff of Sheogorath': 'https://www.nexusmods.com/skyrimspecialedition/mods/16873',
    'Stances of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/21617',
    'Starting Outfit Suppressed': 'https://www.nexusmods.com/skyrimspecialedition/mods/43967',
    'Staves of Skyrim': 'https://www.nexusmods.com/skyrim/mods/22691',
    'Stockades of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/43227',
    'Storm of Steel': 'https://www.nexusmods.com/skyrimspecialedition/mods/33697',
    'Supplies of Skyrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/45377',
    'Sweeping Organizes Stuff': 'https://www.nexusmods.com/skyrimspecialedition/mods/51645',
    'Sword of Shadow': 'https://www.nexusmods.com/skyrimspecialedition/mods/60766'
}
