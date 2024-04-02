import requests
from bs4 import BeautifulSoup

def get_nba_players_stats():
    url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    players = []

    # Find the table containing player stats
    table = soup.find('table', {'id': 'per_game_stats'})

    # Check if the table is found
    if table:
        # Extract data from each row of the table
        rows = table.find_all('tr')[1:]  # Skip header row
        for row in rows:
            player_data = {}
            columns = row.find_all('td')
            if columns:  # Check if columns are found
                player_data['name'] = columns[0].text
                player_data['team'] = columns[1].text
                player_data['points_per_game'] = columns[28].text
                player_data['rebounds_per_game'] = columns[22].text if len(columns) >= 23 else ""
                player_data['assists_per_game'] = columns[23].text if len(columns) >= 24 else ""
                # Add more stats as needed
                players.append(player_data)
            else:
                print("No columns found for row:", row)

    else:
        print("Table not found on the webpage.")

    return players

if __name__ == "__main__":
    nba_players_stats = get_nba_players_stats()
    for player in nba_players_stats:
        print(player)
