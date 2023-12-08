import fileinput
from word2number import w2n

list_of_calibration_inputs = []
for calibration_inputs in fileinput.input(files="day_one_input"):
    list_of_calibration_inputs.append(calibration_inputs)

print(list_of_calibration_inputs)
calibration_points = []
sum_of_points = 0
for calibration_input in list_of_calibration_inputs:
    inputs = [*calibration_input]
    temp = []
    temp_number_word = []
    first_value = ""
    for character_index in range(0,len(inputs)):
        if inputs[character_index].isdigit():
            first_value = inputs[character_index]
            temp_number_word = []
            break
        else:
            temp_number_word.append(inputs[character_index])
        if len(temp_number_word) > 0:
            for word_number in w2n.american_number_system:
                if "".join(temp_number_word).find(word_number) != -1:
                    first_value = [*str(w2n.word_to_num(word_number))][0]
                    inputs[character_index] = ""
                    temp_number_word = []
                    break
        if first_value != "":
            break
    second_value = ""
    temp_number_word = []
    for character_index in range(len(inputs)-1,-1,-1):
        if inputs[character_index].isdigit():
            second_value = inputs[character_index]
            temp_number_word =[]
            break
        else:
            temp_number_word.insert(0,inputs[character_index])
        if len(temp_number_word) > 0:
            for word_number in w2n.american_number_system:
                if "".join(temp_number_word).find(word_number) != -1:
                    second_value = [*str(w2n.word_to_num(word_number))][-1]
                    temp_number_word = []
                    break
        if second_value != "":
            break
    print("".join(inputs)+" "+first_value +" " + second_value+",")
    calibration_points.append(int(first_value + second_value))
print(sum(calibration_points))