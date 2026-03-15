import requests

BASE_URL = "http://localhost:8080"

def get_player_data(player_id):
    """Get player landing data by id

    Args:
        player_id (int)

    Returns:
        _type_: json-encoded content with player landing info
    """
    if player_id:
        response_stats = requests.get(f"{BASE_URL}/player/{player_id}/stats")
        if response_stats.status_code == 200:
            return response_stats.json()

def get_player_info(player_search_pattern):
    """Get player id by a search pattern

    Args:
        player_search_pattern (str): Player name to search for

    Returns:
        _type_: (int, str) or None
    """
    if player_search_pattern:
        response = requests.get(f"{BASE_URL}/player", params={"q": player_search_pattern})
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                player_id = result[0]['playerId']
                player_name = result[0]['name']
                other_possible_options = [f"\n{p['name']} (ID: {p['playerId']})" for p in result[1:]]
                print(f"✓ Found Player: {result[0]['name']} (ID: {player_id})")
                if other_possible_options:
                    print(f"Other possible players: {', '.join(other_possible_options)}")
                return (player_id, player_name)
            else:
                print(f"✗ Player not found")
        else:
            print(f"✗ Error searching Player {player_search_pattern}: {response.status_code}")
    return None

def get_table_with_players_subset_data(fields, subset_a, subset_a_names, subset_b, subset_b_names):
    data = []
    for field in fields:
        row = {'Metric': field}
        if subset_a:
            row[subset_a_names] = subset_a.get(field, 0)
        else:
            row[subset_a_names] = '-'
        if subset_b:
            row[subset_b_names] = subset_b.get(field, 0)
        else:
            row[subset_b_names] = '-'
        data.append(row)
    return data