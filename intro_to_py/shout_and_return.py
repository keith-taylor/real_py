user_input = input("Please input a string of text:> ")

def shout_and_return(input_str):
    """
    Requests a string from the user and returns that string in upper case.
    """
    loud_input = input_str.upper()
    return(loud_input)

print(shout_and_return(user_input))

n = 0
while n < 5:
    print("n")
    n += 1