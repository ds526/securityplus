import csv
import random
import re
from fuzzywuzzy import fuzz, process

attacks_input_file = "secplus-data-attacks.csv"
enc_input_file = "secplus-data-enc.csv"
ports_input_file = "secplus-data.csv"
data_list = []

# Generate a random integer between 1 and 10
def get_rand(l, u):
    random_int = random.randint(l, u)
    return random_int

def gen_csv(my_csv):    
    with open(my_csv, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter='|')
        for row in csv_reader:
            print(row)
            data_list.append(row)
    # return data_list

def get_ratio(a,b):
    return fuzz.ratio(a, b)

gen_csv(attacks_input_file)
gen_csv(enc_input_file)
gen_csv(ports_input_file)
# print(data_list)

upper_limit = len(data_list)
lower_limit = 0
count = 0
number_correct = 0
total = 10
already_asked = {}

while count < total:
    print("")
    rand_int = get_rand(lower_limit, upper_limit)
    answer = data_list[rand_int].get('ANSWER')
    desc = data_list[rand_int].get('QUESTION')

    if answer not in already_asked:
        already_asked[answer] = 1
        print(desc)
        user_ans_service = input("Answer? ")
        # print("ANSWERRRRR>>> " + answer)
        print("Ratio is: " + str(get_ratio(user_ans_service.lower(), answer.lower())))
        if user_ans_service.lower() == answer.lower():
            print("Correct!")
            print(answer + " -- " + desc)
            number_correct+=1
        else:
            print("Fail")
            print(answer + " -- " + desc)
        count+=1
    else:
        already_asked[answer]+=1

    # if already_asked[answer] < 1:

print(already_asked)
score = (number_correct / total) * 100
print("You answered " + str(number_correct) + " out of " + str(total) + " for a score of " + str(score) + "%")
