import random

print("Please enter your first name:> ")
first_name = str(input().strip())

print("Please enter your second name:> ")
last_name = str(input().strip())

full_name = first_name.title() + " " + last_name.title()
print(f"Your full name (as entered): {full_name}")

full_name_no_spaces = full_name.replace(" ", "")
random_name_index = random.randint(0, len(full_name_no_spaces))

def number_suffix(index_numb):
    index_numb += 1
    if index_numb == 11:
        suffix = "th"
    elif index_numb % 10 == 1:
        suffix = "st"
    elif index_numb % 10 == 2:
        suffix = "nd"
    elif index_numb % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    return suffix

print(f"The {random_name_index + 1}{number_suffix(random_name_index)} letter of your name is: \"{full_name_no_spaces[random_name_index]}\".")
