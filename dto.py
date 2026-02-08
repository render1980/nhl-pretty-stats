from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class BaseDTO(BaseModel):
    model_config = ConfigDict(extra="ignore")

class ClientTeamName(BaseDTO):
    default: str


## Player landing (info)
class PlayerName(BaseDTO):
    default: str


class PlayerTotalStats(BaseDTO):
    assists: Optional[int] = None
    avgToi: Optional[str] = None
    faceoffWinningPctg: Optional[float] = None
    gameTypeId: Optional[int] = None
    gameWinningGoals: Optional[int] = None
    gamesPlayed: Optional[int] = None
    goals: Optional[int] = None
    otGoals: Optional[int] = None
    pim: Optional[int] = None
    plusMinus: Optional[int] = None
    points: Optional[int] = None
    powerPlayGoals: Optional[int] = None
    powerPlayPoints: Optional[int] = None
    season: Optional[int] = None
    shorthandedGoals: Optional[int] = None
    shorthandedPoints: Optional[int] = None
    shots: Optional[int] = None
    shootingPctg: Optional[float] = None


class CareerTotals(BaseDTO):
    regularSeason: PlayerTotalStats
    playoffs: PlayerTotalStats


class PlayerSeasonStats(BaseDTO):
    gameTypeId: Optional[int] = None
    season: Optional[int] = None
    gamesPlayed: Optional[int] = None
    goals: Optional[int] = None
    leagueAbbrev: Optional[str] = None
    pim: Optional[int] = None
    points: Optional[int] = None
    assists: Optional[int] = None
    gameWinningGoals: Optional[int] = None
    powerPlayGoals: Optional[int] = None
    shorthandedGoals: Optional[int] = None
    shots: Optional[int] = None


class PlayerLanding(BaseDTO):
    playerId: int
    isActive: bool
    currentTeamId: Optional[int] = None
    currentTeamAbbrev: Optional[str] = None
    firstName: PlayerName
    lastName: PlayerName
    careerTotals: CareerTotals
    seasonTotals: List[PlayerSeasonStats]


## Skater stats leaders
class SkaterStatsLeadersPlayer(BaseDTO):
    id: int
    first_name: PlayerName
    last_name: PlayerName
    sweater_number: int
    team_abbrev: str
    team_name: ClientTeamName
    position: str
    value: int


class SkaterStatsLeaders(BaseDTO):
    assists: List[SkaterStatsLeadersPlayer]
    goals: List[SkaterStatsLeadersPlayer]
    points: List[SkaterStatsLeadersPlayer]


## Goalie stats leaders
class GoalieStatsLeadersPlayer(BaseDTO):
    id: int
    first_name: PlayerName
    last_name: PlayerName
    sweater_number: int
    team_abbrev: str
    team_name: ClientTeamName
    position: str
    value: int


class GoalieStatsLeaders(BaseDTO):
    wins: List[GoalieStatsLeadersPlayer]
    shutouts: List[GoalieStatsLeadersPlayer]


## Team standings
class TeamStandingsTeamName(BaseDTO):
    default: str


class TeamStanding(BaseDTO):
    conferenceAbbrev: Optional[str] = None
    conferenceHomeSequence: Optional[int] = None
    conferenceL10Sequence: Optional[int] = None
    conferenceName: Optional[str] = None
    conferenceRoadSequence: Optional[int] = None
    conferenceSequence: Optional[int] = None
    date: str
    divisionAbbrev: Optional[str] = None
    divisionHomeSequence: Optional[int] = None
    divisionL10Sequence: Optional[int] = None
    divisionName: Optional[str] = None
    divisionRoadSequence: Optional[int] = None
    divisionSequence: Optional[int] = None
    gameTypeId: Optional[int] = None
    gamesPlayed: Optional[int] = None
    goalDifferential: Optional[int] = None
    goalDifferentialPctg: Optional[float] = None
    goalAgainst: Optional[int] = None
    goalFor: Optional[int] = None
    goalsForPctg: Optional[float] = None
    homeGamesPlayed: Optional[int] = None
    homeGoalDifferential: Optional[int] = None
    homeGoalsAgainst: Optional[int] = None
    homeGoalsFor: Optional[int] = None
    homeLosses: Optional[int] = None
    homeOtLosses: Optional[int] = None
    homePoints: Optional[int] = None
    homeRegulationPlusOtWins: Optional[int] = None
    homeRegulationWins: Optional[int] = None
    homeTies: Optional[int] = None
    homeWins: Optional[int] = None
    l10GamesPlayed: Optional[int] = None
    l10GoalDifferential: Optional[int] = None
    l10GoalsAgainst: Optional[int] = None
    l10GoalsFor: Optional[int] = None
    l10Losses: Optional[int] = None
    l10OtLosses: Optional[int] = None
    l10Points: Optional[int] = None
    l10RegulationPlusOtWins: Optional[int] = None
    l10RegulationWins: Optional[int] = None
    l10Ties: Optional[int] = None
    l10Wins: Optional[int] = None
    leagueHomeSequence: Optional[int] = None
    leagueL10Sequence: Optional[int] = None
    leagueRoadSequence: Optional[int] = None
    leagueSequence: Optional[int] = None
    losses: Optional[int] = None
    otLosses: Optional[int] = None
    pointPctg: Optional[float] = None
    points: Optional[int] = None
    regulationPlusOtWinPctg: Optional[float] = None
    regulationPlusOtWins: Optional[int] = None
    regulationWinPctg: Optional[float] = None
    regulationWins: Optional[int] = None
    roadGamesPlayed: Optional[int] = None
    roadGoalDifferential: Optional[int] = None
    roadGoalsAgainst: Optional[int] = None
    roadGoalsFor: Optional[int] = None
    roadLosses: Optional[int] = None
    roadOtLosses: Optional[int] = None
    roadPoints: Optional[int] = None
    roadRegulationPlusOtWins: Optional[int] = None
    roadRegulationWins: Optional[int] = None
    roadTies: Optional[int] = None
    roadWins: Optional[int] = None
    seasonId: Optional[int] = None
    shootoutLosses: Optional[int] = None
    shootoutWins: Optional[int] = None
    streakCode: Optional[str] = None
    streakCount: Optional[int] = None
    teamName: TeamStandingsTeamName
    ties: Optional[int] = None
    waiversSequence: Optional[int] = None
    wildcardSequence: Optional[int] = None
    winPctg: Optional[float] = None
    wins: Optional[int] = None


class TeamStandings(BaseDTO):
    wildCardIndicator: bool
    standings: List[TeamStanding]


## Club stats
class ClubStatsSkater(BaseDTO):
    playerId: int
    firstName: PlayerName
    lastName: PlayerName
    positionCode: str
    gamesPlayed: int
    goals: int
    assists: int
    points: int
    plusMinus: int
    penaltyMinutes: int
    powerPlayGoals: int
    shorthandedGoals: int
    gameWinningGoals: int
    overtimeGoals: int
    shots: int
    shootingPctg: float
    avgTimeOnIcePerGame: float
    avgShiftsPerGame: float
    faceoffWinPctg: float


class ClubStatsGoalie(BaseDTO):
    playerId: int
    firstName: PlayerName
    lastName: PlayerName
    gamesPlayed: int
    gamesStarted: int
    wins: int
    losses: int
    overtimeLosses: int
    goalsAgainstAverage: float
    savePercentage: float
    shotsAgainst: int
    saves: int
    goalsAgainst: int
    shutouts: int
    goals: int
    assists: int
    points: int
    penaltyMinutes: int
    timeOnIce: int


class ClubStats(BaseDTO):
    season: str
    gameType: int
    skaters: List[ClubStatsSkater]
    goalies: List[ClubStatsGoalie]


## All teams stats
class TeamStatsData(BaseDTO):
    faceoff_win_pct: float
    games_played: int
    goals_against: int
    goals_against_per_game: float
    goals_for: int
    goals_for_per_game: float
    losses: int
    ot_losses: int
    penalty_kill_net_pct: float
    penalty_kill_pct: float
    point_pct: float
    points: int
    power_play_net_pct: float
    power_play_pct: float
    regulation_and_ot_wins: int
    season_id: int
    shots_against_per_game: float
    shots_for_per_game: float
    team_full_name: str
    team_id: int
    ties: int
    wins: int
    wins_in_regulation: int
    wins_in_shootout: int


class AllTeamsStats(BaseDTO):
    data: List[TeamStatsData]


## Teams and rosters
class Team(BaseDTO):
    id: int
    franchise_id: int
    full_name: str
    league_id: int
    raw_tri_code: str
    tri_code: str


class RosterPlayerName(BaseDTO):
    default: str


class RosterPlayerInfo(BaseDTO):
    id: int
    first_name: RosterPlayerName
    last_name: RosterPlayerName
    sweater_number: int
    position_code: str
    shoots_catches: str
    height_in_centimeters: int
    weight_in_kilograms: int
    birth_date: str
    birth_country: str


class TeamRoster(BaseDTO):
    forwards: List[RosterPlayerInfo]
    defensemen: List[RosterPlayerInfo]
    goalies: List[RosterPlayerInfo]
