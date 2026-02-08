import logging
import logging.config
from fastapi import FastAPI
from service import APIService

logging.config.fileConfig("logging.conf")
log = logging.getLogger("pretty")

app = FastAPI()
service = APIService()


@app.get("/")
async def root():
    return {"message": "NHL Stats Fetcher"}


@app.get("/player/{player_id}/stats")
async def get_player_stats(player_id: int):
    """Get a player stats. Example: `curl http://localhost:8080/player/8478402/stats`

    Args:
        player_id (int): player id

    Returns:
        _type_: @dto.PlayerLanding
    """
    return service.fetch_player_landing(player_id=player_id)
    # return {"message": f"player_id={player_id}"}


@app.get("/standings")
async def get_team_standings(date: str):
    """Get teams standings by the date. Example: `curl http://localhost:8080/standings?date=2023-11-10`

    Args:
        date (str): Date in YYYY-MM-DD format. Example - 2023-11-10.

    Returns:
        _type_: @dto.TeamStandings
    """
    return service.fetch_team_standings(date=date)
    # return {"message": f"date={date}"}


@app.get("/club/{club_abbr}/season/{season_id}/stats")
async def get_club_player_stats(club_abbr: str, season_id: int, game_type_id: int):
    """Get stats of all players of a club in a season. Example: `curl http://localhost:8080/club/EDM/season/20242025/stats?game_type_id=2`
    
    game_type_id = 2 (regular season), = 3 (playoff)

    Args:
        club_abbr (str): Example: EDM
        season_id (int): Example: 20242025
        game_type_id (int): Example: 2

    Returns:
        _type_: @dto.ClubStats
    """
    return service.fetch_club_player_stats(
        club_abbr=club_abbr, season_id=season_id, game_type_id=game_type_id
    )
    # return {
    #     "message": f"club_abbr={club_abbr} season_id={season_id} game_type_id={game_type_id}"
    # }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
