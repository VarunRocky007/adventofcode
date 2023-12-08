import fileinput

list_of_games = {}
count = 1
for games in fileinput.input(files="day_two_input"):
    list_of_games.update({count: games.split(":")[-1].strip().split(";")})
    count += 1
processed_list_of_games = {}
possible_games = 0
for game in list_of_games.keys():
    prob_of_cube = []
    for probs in list_of_games[game]:
        prob_of_colors = {"red": 0, "green": 0, "blue": 0}
        for prob in probs.split(","):
            prob_of_colors.update({prob.strip().split()[-1]:int(prob.strip().split()[0])})
        prob_of_cube.append(prob_of_colors)
    processed_list_of_games.update({game:prob_of_cube})
print(processed_list_of_games)
for game in processed_list_of_games.keys():
    temp = False
    for probs_of_cube in processed_list_of_games[game]:
        if probs_of_cube["red"] <= 12 and probs_of_cube["blue"] <= 14 and probs_of_cube["green"] <= 13:
            temp = True
        else:
            temp = False
            break
    if temp:
        possible_games+=game
print(possible_games)



