"""
Copyright notice:
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

manual_exceptions = {
    'lux': [{'game_id': 1704, 'name': 'Lux', 'url': '/skyrimspecialedition/mods/43158'}, {'No results': 110}],
    'qui': [{'game_id': 1704, 'name': 'QUI', 'url': '/skyrimspecialedition/mods/65343'}, {'No results': 110}],
    'enb light': [{'game_id': 1704, 'name': 'ENB Light', 'url': '/skyrimspecialedition/mods/22574'}, {'game_id': 110, 'name': 'Enhanced Lighting for ENB (ELE)', 'url': '/skyrim/mods/59733'}],
    'sky idles': [{'game_id': 1704, 'name': 'Sky Idles', 'url': '/skyrimspecialedition/mods/45794'}, {'No results': 110}],
    'nordic ui': [{'game_id': 1704, 'name': 'NORDIC UI - Interface Overhaul', 'url': '/skyrimspecialedition/mods/49881'}, {'No results': 110}],
    'ebony knight armor': [{'game_id': 1704, 'name': 'Ebony Knight Armor', 'url': '/skyrimspecialedition/mods/68062'}, {'game_id': 110, 'name': 'Ebony Knight Armor LE Port', 'url': '/skyrim/mods/112520'}],
    'animated poisons': [{'game_id': 1704, 'name': 'Animated Poisons', 'url': '/skyrimspecialedition/mods/72849'}, {'game_id': 110, 'name': 'RUSTIC ANIMATED POTIONS and POISONS', 'url': '/skyrim/mods/77541'}],
    'static mesh improvement mod improvement mod': [{'game_id': 1704, 'name': 'Static Mesh Improvement Mod Improvement Mod', 'url': '/skyrimspecialedition/mods/55543'}, {'game_id': 110, 'name': 'Static Mesh Improvement Mod Improvement Mod LE', 'url': '/skyrim/mods/110210'}],
    'proteus': [{'game_id': 1704, 'name': 'Proteus', 'url': '/skyrimspecialedition/mods/62934'}, {'game_id': 110, 'name': 'PROJECT PROTEUS', 'url': '/skyrim/mods/106919'}]
}

false_nsfw_flagged = {
    'enhanced blood textures': 'https://www.nexusmods.com/skyrimspecialedition/mods/2357',
    'glenmoril': 'https://www.nexusmods.com/skyrimspecialedition/mods/32998',
    'vigilant': 'https://www.nexusmods.com/skyrimspecialedition/mods/11849/',
    'wico': 'https://www.nexusmods.com/skyrimspecialedition/mods/2136',
    'maximum carnage': 'https://www.nexusmods.com/skyrimspecialedition/mods/43494',
    'fallrim': 'https://www.nexusmods.com/skyrimspecialedition/mods/5031',
    'xpmsse': 'https://www.nexusmods.com/skyrimspecialedition/mods/1988',
    'dummy thicc - flame atronach': 'https://www.nexusmods.com/skyrimspecialedition/mods/43408',
    'highly improved male body overhaul': 'https://www.nexusmods.com/skyrimspecialedition/mods/46311',
    'himbo': 'https://www.nexusmods.com/skyrimspecialedition/mods/46311',
    'gorecap': 'https://www.nexusmods.com/skyrimspecialedition/mods/16440',
    'dx celes nightingale': 'https://www.nexusmods.com/skyrimspecialedition/mods/4529',
}

common_acronyms = {
    'elfx': 'Enhanced Lights and FX',
    'nff': 'Nether Follower Framework',
    'ussep': 'Unofficial Skyrim Edition Patch',
    'uslep': 'Unofficial Skyrim Edition Patch',
    'mo2': 'Mod Organizer 2',
    'lotd': 'Legacy of the Dragonborn',
    'icow': 'Immersive College of Winterhold',
    'nemesis': 'Nemesis Unlimited Behavior Engine',
    'cgo': 'Combat Gameplay Overhaul',
    'mbo': 'Movement Behavior Overhaul',
    'jbo': 'Jump Behavior Overhaul',
    'tdm': 'True Directional Movement',
    'dar': 'Dynamic Animation Replacer',
    'vanilla enb': 'The Vanilla ENB',
    'scar': 'scar - Skyrim Combos AI Revolution',
    'heart breaker': 'Heart Breaker - A Killmove Mod',
    'dyndolod 3': 'DynDOLOD 3 Alpha',
    'cocks': 'Constructible Object Custom Keyword System',
    'jop': 'Joy of Perspective',
    'mic': 'More Informative Console',
    'cao': 'cathedral assets optimizer',
    'balls': 'Beautiful Artistic and Lorefriendly Loading Screens'
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

gamepass_gif = [
    'https://cdn.discordapp.com/attachments/806307229182984202/1016099201119174667/IMG_5618.gif',
    'https://cdn.discordapp.com/attachments/806307229182984202/1016100862613016587/IMG_5620.gif',
    'https://cdn.discordapp.com/attachments/806307229182984202/1016139114170564648/IMG_5622.gif',
    'https://cdn.discordapp.com/attachments/806307229182984202/1016194553348370452/IMG_5625.gif',
    'https://cdn.discordapp.com/attachments/806307229182984202/1016194832479297566/IMG_5626.gif'
]