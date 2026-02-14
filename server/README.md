## Requirements

Installed `pyenv`

## Create a local environment

```
pyenv install 3.12.3
pyenv local 3.12.3
```

## Start server locally

```
cd server
python main.py
```

## Request examples

### Get a player stats

```
curl http://localhost:8080/player/8478402/stats
```

### Get teams standings by the date

```
curl http://localhost:8080/standings?date=2023-11-10
```

### Get stats of all players of a club in a season

```
curl http://localhost:8080/club/EDM/season/20242025/stats?game_type_id=2
```