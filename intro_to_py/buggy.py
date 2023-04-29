import random, pdb
number_to_guess = random.randint(1, 10)
guessed_number = 0
# pdb.set_trace()
print("Please input a number between 1 and 10:> ")
user_input = input()

def canBeInt(n):
    try:    
        int(n)
        return True
    except ValueError:
        # i.e. not int-able
        return False

if canBeInt(user_input) == False:
    print("That value is not compatible!")
else:
    #print(f"You guessed a number of type {type(guessed_number)}.")
    guessed_number = int(user_input)
    if guessed_number == number_to_guess:
        print(f"Well done! {guessed_number} equals {number_to_guess}!")
    else:
        print(f"Sorry, {guessed_number} does not equal {number_to_guess}, better luck next time!")
          


