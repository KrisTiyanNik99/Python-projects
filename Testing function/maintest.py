import math
import time

name = "Ivan"
age = 23
height = 1.76
is_human = (1 + 1) == (1 + 1)

# Operations with diff data types
age = age + 1
age += 1

# if "new_var = age + name" this will be error. Cuz only can concat string to string
print("Your ages are: " + str(age) + "!")
print("You speak only " + str(is_human))

# Converting variables is like- str, int....(variable)
print("Your height is: " + str(height) + "!")
print(age + height + is_human)
print(int(age + height))

# Che data Type command and print 
print(type(name))
print(type(height))
print(type(age))
print(type(is_human))

# If we have 2 or more words we separate them with underscore
last_name = "Nikolov"

# We can use multiple assignment
f_name, iq, points = "Georgi", 90, 100 
print(f_name)
print(iq)
print(points)

Siyana = Stoicho = 25
print(Siyana)
print(Stoicho)

#================================================================================================================================
# Main String method in Python

s_name, name, f_name = "24365555222", "Kristiyanyanyan", "Bro"
print(len(name))

# If character is not found then return -1
print(name.find("a"))

# Capitalize only first character in whole string
print(name.capitalize())

print(name.upper())
print(name.lower())

# This method return true only if whole string is from digits
print("First name is : " + str(name.isdigit()) + " and Second is : " + str(s_name.isdigit()))

# This method check if your string contains only letters
print(name.isalpha())
print(s_name.isalpha())

# Check how many char combinations contains our variable
print(name.count("yan"))
print(s_name.count("2"))
print(s_name.replace("5", "7"))

# Displaying string multiple times
print(f_name * 3)

#================================================================================================================================
# Inputs

# When u have diff from string inputs u need to cast them
new_age = int(input("How old are you: "))
money = float(input("How much money you have now: "))
new_age += 1
print("Your age is: " + str(new_age) + " and you have " + str(money) + " money")

#================================================================================================================================
# Math methods

num, s_num, t_num, f_num, ff_num = 3.56, 432, 2.34554, -123.43, 432.2

# Round rounded to nearest int
print(round(num))
print(round(t_num))
print(math.ceil(t_num))
print(math.floor(num))
print(abs(f_num))

# Pow takes two param, first in number that we pow and second is how much we pow him
print(pow(num, 3))

# Max method found max value from list with numbers and min is found min value
print(max(num, s_num, t_num, f_num, ff_num))
print(min(num, s_num, t_num, f_num, ff_num))

#================================================================================================================================
# Substring and slicing

name1, name2, name3 = "Kriso1", "KkkRrrIiiSssOoo12", "Kris Boko"

# Create substring from starting and ending index 
new_name1 = name1[0:len(name1)]
# If we leave first index py by default will start from 0/ same is for last index by default py will take until end
# new_name1 = nam1[:len(name1)] - same as first
# new_name1 = nam1[0:] - same as first
# new_name1 = nam1[:] - same as first
print(new_name1)

# We have "set" which is how much we increase our index by between start and end
funkey_name = name2[::3]
print(funkey_name)

# We can reverse string very simple
reversed_name = name3[::-1]
print(reversed_name)
reversed2 = name2[5::-1]
print(reversed2)

# We can slice objects with "slice": start and end index (if we use - index we start from the end of our string)
website = "https//google.com"
website2 = "https//wikipedia.bgd"
cut = slice(7,-4)

print(website[cut])
print(website2[cut])

#================================================================================================================================
# If statements

is_human = False

if is_human :
    print("Yes im human!")
    is_human = False
    # If u want to check some condition is not true we use "not" before it
elif not is_human :
    print("You are NOT human!")
    is_human = True
    
    # If we want to check two or three things at the same time we use "and" or "or"
    if name1 == funkey_name.capitalize() and 1 == abs(-1):
        print("ALL IS EQUAL!")
        
    if name1 == funkey_name or not(new_age == 25):
        print("Not all is the same!")
else :
    print("I dont know")

#================================================================================================================================
# Loops

# some_name = None or some_name = ""
some_name = input("Type name: ")

while some_name == "" or some_name == " ": # We can use len(some_name) == 0 / not(some_name)
    print("Enter name")
    some_name = input("Now Type name: ")

print("You escape!")

while True:
    some_name = input("Enter new name: ")
    # We can break the loop
    print("You break!")
    break

for i in range(5):
    print("Normal loop: " + str(i))

# We can use two parameters in range()- first is start index and last is end!
for i in range(5, 10):
    print("Start from 5: " + str(i + 1))
    
# Also we can add and third element in range()- this is how much we want to count up or down
for i in range(0, len(name) + 5, 2):
    # We can skip iteration with "continue"
    if i == 10 or i == 12:
        continue
    print("By two: " + str(i))

for i in range(20, 0, -1):
    if i == 13:
        # Pass do nothing 
        pass
    else: 
        print("Minus loop: " + str(i))

# If we want to print letters we can just replace range with our string
for letter in funkey_name:
    print("Letter: " + letter)

# We can nest loops
rows = int(input("How big u want to be your pyramid?: "))
for i in range(rows):
    for j in range(rows - i):
        print(" ", end="")
        
    for j in range(i):
        # If we want to prevent cursor down to next line we use end=""
        print(" *", end="")
    print()

# We can just combine it with timer
for seconds in range(3, 0, -1):
    print(seconds)
    time.sleep(1)
print("Nice u finish this loop exercise!")

#================================================================================================================================
# Lists

# We can create list with square brackets and write content in them
food = ["orange", "apple", "banana"]

# With "append" method we can add another element to our list. With "insert" we can insert a items in position
food.append("pizza")
# If u try to set in insert out of bound index py will add it in the end of the list
food.insert(1, "new word")
food.insert(0, ["test1", "test3"])

# With "extend" method we can add a whole list/items to to our already existed list
food.extend(["hamburger", "tomato", "test2"])
another_food = ["avocado", "cherry"]
food.extend(another_food)
food.remove("test2") 
# With "pop" we can remove always the last element in the list
food.pop()
# We can also use "clear" with clear all elements and "sort" witch sort all elements by alphabetically
print(food[0])
print(food)

# 2d lists
drinks = ["coffee","tea", "water", 21, 3]
new_list = [drinks, another_food]
# If we want to get item need two square brackets and the index within
print(new_list)
print(new_list[0][2])

#================================================================================================================================
# Tuple

# Tuple is ordered and Unchangeable list
students = ("Bro", 24, "Nikolov","male")

# With "count" we find how many time the element is contains in the list
print(students.count("element"))

# With "index" witch is the index of our element that we search
if "Nikolov" in students:
    print(students.index(24))

for student in students:
    print(student)

# Sets

# Sets are unordered and unidexed list with no duplicate values
utensils = {"spoon","knife","fork","FORK"}
utensils.remove("FORK")
utensils.add("napkin")

dishes = {"bowl","cup","plate","bottle","knife","KNIFE","KNIFE","KNIFE"}
# We can clear all with "clear()" method
# We can add diff set one to each other
dishes.update(utensils)
# We can join two set and create entire new set 
table_dinner = dishes.union(utensils)

# We "difference()" method witch compare two sets and print what is the diff between those sets
print(dishes.difference(utensils))

for utensil in dishes:
    print(utensil)
    

index = 0
for x in table_dinner:
    index +=  1
    print(str(index) + " " + x)