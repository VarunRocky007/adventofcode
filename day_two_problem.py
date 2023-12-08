import fileinput

list_of_games = {}
count = 1
for games in fileinput.input(files="day_two_input"):
    list_of_games.update({count: games.split(":")[-1].strip().split(";")})
    count += 1
processed_list_of_games = {}
sum_of_max_cubes = 0
for game in list_of_games.keys():
    prob_of_cube = []
    for probs in list_of_games[game]:
        prob_of_colors = {"red": 0, "green": 0, "blue": 0}
        for prob in probs.split(","):
            prob_of_colors.update({prob.strip().split()[-1]: int(prob.strip().split()[0])})
        prob_of_cube.append(prob_of_colors)
    processed_list_of_games.update({game: prob_of_cube})
print(processed_list_of_games)
for game in processed_list_of_games.keys():
    temp = False
    red = 1
    blue = 1
    green = 1
    for probs_of_cube in processed_list_of_games[game]:
        if red < probs_of_cube["red"]:
            red = probs_of_cube["red"]
        if blue < probs_of_cube["blue"]:
            blue = probs_of_cube["blue"]
        if green < probs_of_cube["green"]:
            green = probs_of_cube["green"]
    print(red+green+blue)
    sum_of_max_cubes += red * green * blue
print(sum_of_max_cubes)
