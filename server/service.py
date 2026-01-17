import logging
import logging.config
from cachetools import TTLCache
from client_api import APIClient

from dto import PlayerLanding

logging.config.fileConfig("logging.conf")
log = logging.getLogger("pretty")

# Cache with a max size of 10000 and a TTL of 1 day
player_langings_cache = TTLCache(maxsize=10000, ttl=86400)
team_standings_cache = TTLCache(maxsize=10000, ttl=86400)
club_player_stats_cache = TTLCache(maxsize=10000, ttl=86400)

api_client = APIClient()


class APIService:
    """
    Service with caching abilities atop of client api.
    """

    def fetch_player_landing(self, player_id: int):
        """
        Fetch player landing data from cache.
        If not found in cache - fetch from API and store in cache.

        returns @dto.PlayerLanding
        """
        cache_key = f"{player_id}"
        if cache_key in player_langings_cache:
            log.debug(f"Player landing data for {player_id} found in cache.")
            return player_langings_cache[cache_key]
        log.debug(
            f"Player landing data for {player_id} not found in cache. Fetching from API."
        )
        landing: PlayerLanding = api_client.get_player_landing(player_id)
        player_langings_cache[cache_key] = landing
        return landing

    def fetch_team_standings(self, date: str):
        """
        Fetch team standings data from cache.
        If not found in cache - fetch from API and store in cache.

        :param date: Standings on a specific date. Example - 2023-11-10.

        returns @dto.TeamStandings

        """
        cache_key = f"{date}"
        if cache_key in team_standings_cache:
            log.debug(f"Team standings data for {date} found in cache.")
            return team_standings_cache[cache_key]
        log.debug(
            f"Team standings data for {date} not found in cache. Fetching from API."
        )
        standings = api_client.get_team_standings(date)
        team_standings_cache[cache_key] = standings
        return standings

    def fetch_club_player_stats(
        self, club_abbr: str, season_id: int, game_type_id: int
    ):
        """
        Fetch club player stats data from cache.
        If not found in cache - fetch from API and store in cache.

        :param club_abbr: Example - EDM
        :param season_id: Example - 20242025
        :param game_type_id: Example 2

        returns @dto.ClubStats
        """
        cache_key = f"{club_abbr}_{season_id}_{game_type_id}"
        if cache_key in club_player_stats_cache:
            log.debug(f"Club player stats data for {club_abbr} found in cache.")
            return club_player_stats_cache[cache_key]
        log.debug(
            f"Club player stats data for {club_abbr} not found in cache. Fetching from API."
        )
        stats = api_client.get_club_player_stats(club_abbr, season_id, game_type_id)
        club_player_stats_cache[cache_key] = stats
        return stats
