import csv
import random
import re

attacks_input_file = "secplus-data-attacks.csv"
enc_input_file = "secplus-data-enc.csv"
data_list = []

# Generate a random integer between 1 and 10
def get_rand(l, u):
    random_int = random.randint(l, u)
    return random_int

def gen_csv(my_csv):    
    with open(my_csv, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter='|')
        for row in csv_reader:
            data_list.append(row)
    # return data_list

gen_csv(attacks_input_file)
gen_csv(enc_input_file)

upper_limit = len(data_list)
lower_limit = 0
count = 0
number_correct = 0
total = 10
already_asked = {}
while count < total:
    print("")
    rand_int = get_rand(lower_limit, upper_limit)
    dos_type = data_list[rand_int].get('TYPE')
    desc = data_list[rand_int].get('DESCRIPTION')

    if dos_type not in already_asked:
        already_asked[dos_type] = 1
        print(desc)
        user_ans_service = input("What is the attack name? ")
        if user_ans_service.lower() == dos_type.lower():
            print("Correct!")
            print(dos_type + " -- " + desc)
            number_correct+=1
        else:
            print("Fail")
            print(dos_type + " -- " + desc)
        count+=1
    else:
        already_asked[dos_type]+=1

    # if already_asked[dos_type] < 1:

print(already_asked)
score = (number_correct / total) * 100
print("You answered " + str(number_correct) + " out of " + str(total) + " for a score of " + str(score) + "%")
