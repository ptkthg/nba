import pandas as pd

def read_winner(year):
    for champion in recent_champions:
        if champion["year"] == year:
            return champion["team"]
    return f"Não encontramos o vencedor do ano {year}."

champions = {"Boston Celtics": 17, "Los Angeles Lakers": 16, "Chicago Bulls": 6, "San Antonio Spurs": 5, "Golden State Warriors": 6}

for team, titles in champions.items():
    print(f'{team} tem {titles} títulos.')

top_players = ["Michael Jordan", "Kareem Abdul-Jabbar", "LeBron James", "Bill Russell", "Magic Johnson"]

print("\nOs cinco jogadores mais vitoriosos na NBA são:")
for player in top_players:
    print(player)

recent_champions = recent_champions = [
    {"team": "Los Angeles Lakers", "year": 2020, "mvp": "LeBron James", "points": 25.4, "rebounds": 7.9, "assists": 10.6},
    {"team": "Toronto Raptors", "year": 2019, "mvp": "Kawhi Leonard", "points": 27.0, "rebounds": 7.3, "assists": 2.2},
    {"team": "Golden State Warriors", "year": 2018, "mvp": "Kevin Durant", "points": 26.4, "rebounds": 6.8, "assists": 5.4},
    {"team": "Golden State Warriors", "year": 2017, "mvp": "Kevin Durant", "points": 25.1, "rebounds": 8.3, "assists": 4.8},
    {"team": "Cleveland Cavaliers", "year": 2016, "mvp": "LeBron James", "points": 26.4, "rebounds": 8.6, "assists": 7.4},
    {"team": "Golden State Warriors", "year": 2015, "mvp": "Andre Iguodala", "points": 16.3, "rebounds": 5.8, "assists": 4.0},
    {"team": "San Antonio Spurs", "year": 2014, "mvp": "Kawhi Leonard", "points": 16.5, "rebounds": 7.2, "assists": 2.3},
    {"team": "Miami Heat", "year": 2013, "mvp": "LeBron James", "points": 26.8, "rebounds": 8.0, "assists": 7.3},
    {"team": "Dallas Mavericks", "year": 2011, "mvp": "Dirk Nowitzki", "points": 26.0, "rebounds": 9.0, "assists": 2.2},
    {"team": "Los Angeles Lakers", "year": 2010, "mvp": "Kobe Bryant", "points": 27.0, "rebounds": 5.4, "assists": 5.0}
]

print("\nOs últimos 10 campeões da NBA e seus MVPs são:")
for champion in recent_champions:
    print(f'{champion["year"]}: {champion["team"]} - MVP: {champion["mvp"]}')

year = int(input("\nEm que ano você deseja saber o vencedor? "))
winner = read_winner(year)
print(f'O vencedor do ano {year} foi {winner}')

mvp_df = pd.DataFrame(recent_champions)
print("\nEstatísticas dos MVPs nos últimos 10 anos:")
print(mvp_df[["mvp", "points", "rebounds", "assists"]])
