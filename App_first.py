"""
##############################################
# I ALSO HAVE TO ADD THIS CODE TO GITHUB NOW
# I AM CHANGING THE CODE AND PUSH IT TO GITHUB
##############################################





character_name = "Luka"
character_age = "40"
is_male = False
print("There once was a man named " + character_name + ",")
print("He was "+ character_age +" years old.")
character_name = "faizan"
character_age = "100"
print("He really liked the name " + character_name + ",")
print("but didn't like being "+ character_age +".")




phrase= "Faizan is AWESOME"
print(phrase.replace("Faizan","Luka"))


from math import *
my_num = -5.095
print(sqrt(64))




Name = input("Enter your name : ")
Age = input("Enter your age : ")
print("Welcome " + Name + "!")
print("You are " + Age + " years old.")

"""

# Basic Calculator
"""
Num1 = input("Enter first number : ")
Num2 = input("Enter second number : ")
result = float(Num1) + float(Num2)
print(result)
"""
#Mad Libs Game
"""
Color = input("Enter the color : ")
Plural_noun = input("Enter the Plural noun : ")
Celeb = input("Enter the celebrity name : ")

print(Color + " are cool")
print(Plural_noun + " are blue")
print("i love " + Celeb)
"""

#LISTs
"""
friends = ["Luka","Junaid",3,True,"Ali","Roza","Abeer"]
friends[5] = "Toby"
friends[2] = 7
print(friends[1:6])
"""


#LISTs Functions

"""
lucky_numbers = [2, 4, 6,6,6,6, 8, 10,12]
friends = ["Ali","Luka","Tabby","Saad","Junaid","Junaid","Junaid","Junaid","Roza"]
#friends.extend(lucky_numbers)    #adding  list at the end of another list
#friends.append("Qasim")          #adding individual elements to a list
#friends.insert(3,"Boyko")        #inserting an individual element at a particular position of a list
#friends.remove("Saad")           #removing an element of a list
#friends.clear()                  #remove all the elements from the list
#friends.pop()                    #remove/pop the last element of the list
#print(friends.index("Boyko"))    #To see if certiáin element is in the list or not
#print(friends.count(6))
#print(friends.count("Junaid"))   #To count the number of similar elements in the list
#friends.sort()                   #sort the list in an ascending order or alphabetical order
#print(friends)
#lucky_numbers.reverse()           #reverse the order of the list
#print(lucky_numbers)
best_friends = friends.copy()     #making another list and copying an other list into it
print(best_friends)

"""

#TUPLES
"""
coordinates = (4,5,6,7,8)
print(coordinates)
"""


#FUNCTIONS
"""
def say_hi(name,age):
    print(name + " " + str(age) + " first function")
#print("Top")
say_hi("faizans",29)            #Calling the function.To execute the function, you mustt have to call it.
#print("Bottom")
say_hi("lukas",26)
"""

#RETURN STATEMENT
"""
def cube(num):
    return num*num*num
result = cube(4)
print(result)
"""

#IF STATEMENT   (Boolean Varibales)
"""
is_male = True         #Boolean Variable
is_tall = False
if is_male and is_tall:                             #is_male has to be true otherwise ELSE statement will be executed
    print("Faizan,you are a male or tall or both ")
elif is_male and not(is_tall):                      #not negates the value of is_tall
    print("Faizan, you are a short male ")
elif not(is_male) and is_tall:
    print("Faizan, you are not a male but you are tall ")
else:
    print("Faizan,you are neither a male nor tall")
"""

#IF STATEMENT  (Comparison)
"""
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >=num3 :       #when comparing strings we use  "" == "" these operators. != symbol for not equal
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(23,34,56))

"""

#BUILDING A CALCULATOR
"""
num1 = float(input("Enter the first number : "))           #By default input is converted in to a string, so we have to convert it in a number
num2 = float(input("Enter the second number : "))
op = input("Enter the functionality : ")
if op == "":
     print(num1 + num2)
elif op == "-" :
     print(num1 - num2)
elif op == "*" :
     print(num1 * num2)
elif op == "/":
     print(num1 / num2)
else:
     print("Error: Please enter the correct operator")

"""

#DICTIONARIES
"""
month_conversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

#print(month_conversions["Mar"])
print(month_conversions.get("Luv","Not a valid key"))          #Access the value of Luv and if the key is invalid then print "Not a valid key"
"""

# WHILE LOOP
"""
i= 1
while i <= 10:
      print(i)
      i += 1              # i= i + 1
print("Loop is finished")
"""

#BUILDING A GUESSING GAME
"""
Secret_word = "Faizan"
Guesses = 1
User_Guess = ""
Tries = 3




while User_Guess != Secret_word and Guesses <= 3:
      print(" You have " + str(Tries) + " tries left ")
      User_Guess = input("Enter Your Guess : " )
      Guesses = Guesses + 1
      Tries = Tries - 1

      if User_Guess ==Secret_word and Guesses <= 3:
            print("Congrats! You guessed correctly. You win!")

      if Guesses > 3:
            print("Game Over! You lose ")
 """

# FOR LOOP
"""
for letter in "Faizan Shafi" :
    print(letter)
"""
"""
friends = ["Ali","Karen","Roza","Luka","Smith","Fiza","Cena"]
for friend in friends:
    print(friend)
"""
"""
friends = ["Ali","Karen","Roza","Luka","Smith","Fiza","Cena"]

for index in range(len(friends)):
 # print(index)
   print(friends[index])
"""

#EXPONENT FUNCTION
"""
print(2**3)      # 2^3
"""

"""
def raise_to_power (base_num, power_num):

    result = 1
    for index in range(power_num):
        result = result * base_num

    return result

print(raise_to_power(2,4))

"""

#2D LIST AND NESTED LOOPS
"""
number_grid = [                 #2d list is basically a grid
 [2,4,6],
 [1,3,7],
 [5,7,9],[0]
]
print(number_grid[1][1])
"""

#use the nested for loop to print the elements of this grid
"""
number_grid = [
 [2,4,6],
 [1,3,7],
 [5,7,9],[0]
]

for a in number_grid:

      for b in a:
            print(b)

"""

#BUILDING A BASIC TRANSLATOR

"""
def translate(phrase):

      result = ""
      for a in phrase:
            if a in "AEIOUaeiou":
               result = result + "g"
            else:
                  result = result + a

      return result

print(translate(input("Enter the name : ")))


"""

#TRY EXCEPT
"""


try:
      number = 10 / 0
      number=int(input("Enter the number : "))
      print(number)

except ZeroDivisionError as err:
      print(err)

except ValueError:
      print("Invalid Input")

"""

#READING FILES
"""
Employee_file = open("Faizan.txt","r")

#print(Employee_file.readlines()[1])

for a in Employee_file.readlines():
    print(a)



Employee_file.close()

"""

#WRITING FILES
"""

#Employee_file = open("Faizan.txt","a")                   #appending the file i-e adding something at the end of the file

#Employee_file.write("\nFaizan - Customer")


Employee_file = open("Faizan_Shafi.txt","w")             #OVERWRITING the file _Also can be used to creat a NEW file


Employee_file.write("Faizan - Python_coding")


Employee_file.close()

"""
"""

#MODULES  ( python file that we can import in our current python file)

import useful_tools       #useful_tools is another py file that i want to use in this py file

print(useful_tools.random_varibale_or_function)


PIP install    #Pip (in command prompt ) is used to install python modules(files). It is a package manager (allows us to manage,install ,uninstall different 3rd party external modules.
"""
#CLASSES AND OBJECTS      (OBJECT is an instance of a CLASS)

#CLASS is basically our own data type of our choice
"""
from Student import Student         #from Student file import Student class

Student1 = Student("Faizan","Electrical",3.1,False)
Student2 = Student("Luka","Bio",4,False)
print(Student2.is_on_probation)
"""

#MULTIPLE CHOICE QUIZ
"""
from Question import Question

question_prompts = [

    "What is the color of apple?\n (a) Red/Green\n (b) Purple\n (c) Orange \n\n" ,
    "What is the color of bannana?\n (a) Teil\n (b) Magenta\n (c) Yellow \n\n" ,
    "What is the color of stawberries?\n (a) Yellow\n (b) Red\n (c) Blue \n\n"
]



questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]



def run_test(questions):
    score = 0
    for question in questions:                                    #Why it is question?
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got" + str(score) + "/" + str(len(questions)) + " correct" )

run_test(questions)

"""

#OBJECT FUNCTIONS









