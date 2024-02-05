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

import re

STRIP_RE = re.compile(r"^(?:\W+|\W+)$")
SPECIAL_RE = re.compile(r"\W+")


def parse_query(query):
    return SPECIAL_RE.sub(",", STRIP_RE.sub("", query.replace("'s", ""))).lower()


class RequestHandler:
    def __init__(self, session):
        self.session = session

    async def search_mods(self, query, game_id, include_adult):
        async with self.session.get(
            url="https://api.nexusmods.com/mods",
            params={
                "terms": parse_query(query),
                "game_id": game_id,
                "include_adult": str(include_adult).lower(),
                "timeout": 15000
                }
        ) as resp:
            if resp.status == 200:
                if (results_data := await resp.json()):
                    return results_data
                else:
                    return str("No results")
