import fileinput

list_of_games = []
for games in fileinput.input(files="day_two_input"):
    list_of_games.append(games.split(":")[-1].strip())
print(list_of_games)