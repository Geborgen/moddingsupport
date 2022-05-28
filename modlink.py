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
import re


STRIP_REGEX = re.compile(r"[^\w]+")

def parse_query(query):
    return re.sub(STRIP_REGEX, ",", query.replace("'s", ""))


# NOTE: The below will be used in a future change. This file is silly currently since it is almost empty, but that will change soon.

# async def get_modlink(self, query, include_adult = False):
#    if query.lower() not in se_modlink_exceptions:
#        async with self.session.get("https://search.nexusmods.com/mods", params={"terms": parse_query(query), "game_id": 1704, "include_adult": str(include_adult).lower()}) as resp:
#            if resp.status == 200:
#                data = await resp.json()
#                results = data["results"]
#                if results:
#                    return results[0]
#    else:
#        return

# async def get_le_modlink(self, query, include_adult=False):
#    if query.lower() not in le_modlink_exceptions:
#        async with self.session.get("https://search.nexusmods.com/mods", params={"terms": parse_query(query), "game_id": 110, "include_adult": str(include_adult).lower()}) as resp:
#            if resp.status == 200:
#                data = await resp.json()
#                results = data["results"]
#                if results:
#                    return results[0]
#    else:
#        return
