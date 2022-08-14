import random 

numbers = ['1' , '2', '3', '4', '5', '6' , '7' , '8' , '9']

symbols = ['!' , '#' , '$' , '%' , '&' , '*' '+']
letters = ['A' , 'B' , 'C' , 'D' , 'E', 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U', 'V' , 'W' , 'X' , 'Y' , 'Z' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z']

print("Welcome to my password generator !")

user_letter = int(input("How many letters do you want\n "))
user_symbol = int(input("How many symbols do you want\n "))
user_number = int(input("How many random numbers do you want\n "))

# password = ""
# # the number the user enter will be used as the  range of the  values 
# for character in range(1 , user_letter + 1):
#      password += random.choice(letters)
    

# for character in range(1, user_number + 1):
#     random_number = random.choice(numbers)
#     password += random_number
    
# for character in range (1 , user_symbol + 1):
#     password += random.choice(symbols)



password_list = []
for passcode in range(1 , user_number + 1):
    password_list += random.choice(numbers)
for passcode in range(1 , user_symbol + 1):
    password_list += random.choice(symbols)
for passcode in range(1 , user_letter + 1):
    password_list += random.choice(letters)
    
random.shuffle(password_list)
new_password = ""
for neb in password_list:
    new_password += neb
    
print(new_password) 

