import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
temp_pw = []

#select specified random # of letters
l=0
while l < nr_letters:
    temp_value = letters[random.randint(0,len(letters)-1)]
    temp_pw.append(temp_value)
    l+=1
#select specified random # of numbers
n=0
while n < nr_numbers:
    temp_value = numbers[random.randint(0,len(numbers)-1)]
    temp_pw.append(temp_value)
    n+=1
#select specified random # of symbols
s=0
while s < nr_symbols:
    temp_value = symbols[random.randint(0,len(symbols)-1)]
    temp_pw.append(temp_value)
    s+=1

#randomly arrange the previously selected random values for each type
password = ""
i=0
while i < len(temp_pw):
    password = password + str(temp_pw.pop(random.randint(0,len(temp_pw)-1)))
print(password)
print(len(password))
if input("do you want to generate another password y/n?").lower() == "n":
    generate = "n"