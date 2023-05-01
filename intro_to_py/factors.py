
def calculate_factor_list(f_user_int):
    factor_list = [1]
    for i in range (2,f_user_int+1):
        if f_user_int % i == 0:
            factor_list.append(i)
    if f_user_int == 1:
        print("The only factor of one is one.")        
    else:
        last_item_in_list = factor_list.pop(-1)
        print(f"The factors of {f_user_int} are: {', '.join(map(str,(factor_list)))} and {last_item_in_list}. ")

try:
    user_int = int(input("Please enter an interger:> "))
    calculate_factor_list(user_int)
except ValueError:
    print("That is not an integer. ")
    







