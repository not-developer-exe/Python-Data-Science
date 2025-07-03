# First code
# print('Hello World!')

# Variables
# Write anything, add '=',it becomes variable in Python

# abc = 10

# Ways to declare variables

# adityaSingh = 10 # Camel Case
# adityasingh = 10 # Snake Case
# AdityaSingh = 10 # Pascal Case 


# Data Types
#refer notes

# Strings and Conversion

# a = 'A'
# print(ord(a))

# a = 65
# print(chr(a))

#String Slicing

# a = 'Aditya KODR'
# print(a[4::1])

# Type Conversion
#a = 10
# print(type(a))

#a = str(a) # Leooo, int bnn gya str
#print(type(a))

# age = int(input("Enter your age: "))
#print(type(age))
#print(f"My age is {age}")

# Operators
# Arithmetic, comparison, logical, and much more
#print(1+2) #Addition
#print(2-1) #Sub
#print(2*3) #Multiply
#print(12/4) #Division
#print(12//4) #Floor Division
#print(2**5) #Exponential

# Assignment Operator
# Assigns value to any variable

# Compound Assignment Operations

#a = 20
#a += 20
#a += 40
#a += 60
#print(a)

# Comparison Operator
# == : Equals to
# != : Not equals to
# < : Less Than
# > : Greater Than
# <= : Less than Equals to
# >= : Greater than Equals to

#Logical Operators

# AND 
# Any one condition gets false, the output becomes false

# print( 10 < 20 and 12 > 10)

# OR 
# And one condition should get true, the output becomes true

# print( 12 < 10 or 23 == 45 or 10 > 5)

# NOT - reverses the boolean ans



# Conditional Statements

# if 

#a = 13

#if a > 10:
    #print('Kch kch huaaaaa')
    

# if - else

#a  = 10;
#if a < 9:
#    print('abcd')
#else:
#    print('bcded')

# if - elif - else

# money = int(input('Provide the amount given by mummy: '))

# if money <= 10 :
#     print('Choco bar')
# elif money == 20:
#     print('Mango Dolly')
# else:
#     print('Mehngi wali ice-cream')

# Questions....

# 1: accept 2 numbers and print the bigger

# a = int(input('enter first num: '))
# b = int(input('Enter second num: '))

# if a > b:
#     print("a is bigger")
# elif b > a:
#     print("b is bigger")
# else:
#     print("both are equal")

# 2 : accept the gender and greet

# gen = input('please specify ur gender (M or F): ')
# if gen == 'M' or gen == 'm':
#     print("Good Morning Sir")
# elif gen == "F" or gen == 'f':
#     print("Good Morning Ma'am")
# else:
#     print('Error happened, please choose M or F')


# 3 : even or odd

# number = int(input('Enter number: '))
# if number%2 == 0:
#     print('EVEN')
# else:
#     print('ODD')

# 4: Valid Voter

# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# if age < 18:
#     print(f"{name} is not a valid voter, you'll be able to vote in {18 - age} years")
# else:
#     print(f"{name} is a valid voter")
    
# 5 : Leap year

# year = int(input('Enter the year: '))

# if year%100 == 0 and year % 400 == 0:
#     print('Leap year')
# elif year % 100 != 0 and year % 4 == 0:
#     print('Leap year')
# else:
#     print('nahi h yrrrrr')

# 6 : elif ladder

# temp = int(input('Enter temp: '))

# if temp < 0:
#     print('bhai, jamm gyaa')
# elif temp >= 0 and temp <10:
#     print('Acchi thand hai')
# elif temp >=10 and temp < 20:
#     print('Bardasht kar skte hai')
# elif temp >=20 and temp < 30:
#     print('Maza aa gya')
# elif temp >=30 and temp < 40:
#     print('thoda paseena aane lga hai')
# else:
#     print('Mummy, itni grmiiiiiiiii')

# Loop - for and while

# # for loop
# for i in range(1, 11, 1): #range(start, stop, steps) Always remember, that stop has to be n+1 for better output like here i needed till 10 so the stop counter is at 11. 
#     print(i)


# 20 to 50

# for i in range(20, 51):
#     print(i)

# from 16 to 1

# for i in range(16, 0, -1):
#     print(i)

# from -3 to -15
# for i in range(-3, -16, -1):
#     print(i)

# print 7 ki table

# for i in range(7, 71, 7):
#     print(i)

# for loop on strings

# a = "ADITYA"

# for i in range(0, 6, 1):
#     print(a[i])

# Alternate or widely used
# for i in range(len(a)):
#     print(a[i])

# 