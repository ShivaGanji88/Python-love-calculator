# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_names_string = name1 + name2
string_convert_lower = combine_names_string.lower()

t = string_convert_lower.count("t")
r = string_convert_lower.count("r")
u = string_convert_lower.count("u")
e = string_convert_lower.count("e")

adding_letters_true = t + r + u + e

l = string_convert_lower.count("l")
o = string_convert_lower.count("o")
v = string_convert_lower.count("v")
e = string_convert_lower.count("e")

adding_letters_love = l + o + v + e
covert_number_to_string = str(adding_letters_true) + str(adding_letters_love)

if int(covert_number_to_string) < 10 or int(covert_number_to_string) > 90:
    print(f"Your score is {covert_number_to_string}, you go together like coke and mentos.")

elif int(covert_number_to_string) > 40 and int(covert_number_to_string) < 50:
    print(f"Your score is {covert_number_to_string}, you are alright together.")

else:
    print(f"Your score is {covert_number_to_string}.")        
