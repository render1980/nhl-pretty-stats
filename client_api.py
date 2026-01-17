from dto import ClubStats, PlayerLanding, TeamStandings
import requests
from requests.models import Response
import logging.config
import logging
import json

logging.config.fileConfig("logging.conf")
log = logging.getLogger("pretty")

TEAMS_LIST_URL = "https://api.nhle.com/stats/rest/en/team"
TEAM_ROSTER_BY_SEASON_URL = "https://api-web.nhle.com/v1/roster/{}/{}"

PLAYER_LANDING_URL = "https://api-web.nhle.com/v1/player/{}/landing"

CLUB_PLAYERS_STATS_BY_SEASON_AND_GAMETYPE_URL = (
    "https://api-web.nhle.com/v1/club-stats/{}/{}/{}"
)

ALL_TEAMS_STATS_BY_SEASON_AND_GAMETYPE_URL = "https://api.nhle.com/stats/rest/en/team/summary?sort={}&cayenneExp=seasonId={}%20and%20gameTypeId={}"

# TEAM_STANDINGS_FOR_ALL_SEASONS_URL = "https://api-web.nhle.com/v1/standings-season"
TEAM_STANDINGS_BY_DATE_URL = "https://api-web.nhle.com/v1/standings/{}"

SKATER_STATS_LEADERS_BY_SEASON_AND_GAMETYPE_URL = (
    "https://api-web.nhle.com/v1/skater-stats-leaders/{}/{}?categories={}&limit={}"
)

GOALIE_STATS_LEADERS_BY_SEASON_AND_GAMETYPE_URL = (
    "https://api-web.nhle.com/v1/goalie-stats-leaders/{}/{}?categories={}&limit={}"
)

DAILY_SCORES_BY_DATE_URL = "https://api-web.nhle.com/v1/score/{}"


def check_response(resp: Response):
    """
    Check if the response is valid
    """
    if resp is None:
        return False
    status = resp.status_code
    if status not in [200, 201]:
        return False
    return True


class APIClient:
    def get_player_landing(self, player_id: int):
        """
        returns @client_dto.PlayerLanding
        """
        resp = requests.get(
            url=PLAYER_LANDING_URL.format(player_id),
            headers={"Content-Type": "application/json"},
        )
        if (check_response(resp=resp)) is False:
            log.error("Failed to get player stats")
            return None
        resp_json = resp.json()
        log.info(f"### Player landing data: {resp_json}")
        landing: PlayerLanding = PlayerLanding(**resp_json)
        return landing

    def get_team_standings(self, date: str):
        """
        returns @client_dto.TeamStandings
        """
        resp = requests.get(
            url=TEAM_STANDINGS_BY_DATE_URL.format(date),
            headers={"Content-Type": "application/json"},
        )
        if (check_response(resp=resp)) is False:
            log.error("Failed to get team stats")
            return None
        resp_json = resp.json()
        # team_stats: TeamStandings = TeamStandings.model_validate_json(resp_json)
        team_stats: TeamStandings = TeamStandings(**resp_json)
        return team_stats

    def get_club_player_stats(self, club_abbr: str, season: int, gametype: int):
        """
        returns @client_dto.ClubStats
        """
        resp = requests.get(
            url=CLUB_PLAYERS_STATS_BY_SEASON_AND_GAMETYPE_URL.format(
                club_abbr, season, gametype
            ),
            headers={"Content-Type": "application/json"},
        )
        if (check_response(resp=resp)) is False:
            log.error("Failed to get player stats")
            return None
        resp_json = resp.json()
        player_stats: ClubStats = ClubStats(**resp_json)
        return player_stats
