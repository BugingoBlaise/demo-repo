#name = input('Enter your name please :')
###color = input ('Enter your favourite color ')
#print('Hello '+name, 'you like ' + color)


# birth = input('Enter birth_year: ')
# age = 2022-int(birth)
# print( age)

# course='blaisemugisha'
# print(len(course))

# course='blaisemugisha'
# print(course.upper())

# course='blaisemugisha'
# print(course.replace('mugisha','Bugingo'))


##MISSION FAILED
# course='blaisemugisha'
# print('blaise' in course)
# if course= True
#     print('deal done')
# else
# print('mision failed')

# import math
# x = 3.6
# print(math.floor(x))

#failed mission
# price = 1000000
# has_good_credit = True
# get=input('enter amounnt')
# if has_good_credit:
#     get = 0.1 * price
#
# else:
#     get = 0.2 * price
#     print(f"Down Payment: ${get}")

#
# resp=input('Enter any number')
# if resp>0:
#     print('positive number')
#               else if resp<0 :
#         print('Negative number')
#         else:
#         print('Zero')



# temp=30
# if temp>30 :
#     print('hot day')
#         #  elif temp<=20 :
#         #
#         # print("moderate")
# else:
#     print("cold day")


# name="abcdefghijklmnopqrstuvwxyz"
#
# if len(name)<3:
#     print("Name must be atleast 3 characters")
# elif len(name)>50:
#     print("name must be a maximum of 50 characters")
# else:
#     print("looks good")


# weight=int(input("Enter Weight: "))
# unit=input("(L)bs or (K)g : ")
#
# if unit.upper()=='L':
#     converted=weight*0.45
#     print(f"You are {converted} kilos")
# else:
#     converted=weight/0.45
#     print(f"You are {converted} pounds")

# i=1
# while i<=5:
#     print(i)
#     i= i+1
#
# print("done")

# i=1
# while i<=5:
#     print('*'*i)
#     i= i+1
#
# print("done")


# #GAME
# guess=9
# guess_count=0
# guess_limit=3
#
# while guess_count<guess_limit:
#     user=int(input('Enter guess: '))
#     guess_count+=1
#     if user==guess :
#         print("well done")
#         break
# else:
#     print("out of guesses!! you failed")


#GAME 2
# command=""
# started=False
# while True:
#     command=input("> ").lower()
#     if command=="start":
#         if started:
#             print("car already started!")
#         else:
#             started=True
#             print("car started")
#
#     elif command=="stop":
#         if not started:
#             print("Car already stopped!!")
#         else:
#             started= False
#             print("Car stopped")
#     elif command=="help":
#         print("""
# start---to start the car
# stop----to stop the car
# quit----to quit
# help----to help
#         """)
#     elif command=="quit":
#         print("Byee !!!")
#         break


# # FOR LOOPS
# for item in 'python':
#     print(item)

# for item in [1,2,3,4,5]:
#     print(item)

# for item in ['Mosh','john','blaise']:
#     print(item)

# for item in range(5,11,2):
#     print(item)


# prices=[10,20,30]
# total= 0
# for price in prices:
#      total+=price
# print(f"Total= {total}")


# for x in range(4):
#     for y in range(4):
#         print(f"({x},{y})")

# x=int(input("enter any number"))
# if x>0:
#     print("positive")
# elif x<0:
#     print("negative number")
# else:
#     print("the number is zero")

# F challenge
# numbers=[5,2,5,2,2]
# for x_count in numbers:
#     print('x'*x_count)

# LETTER F
# numbers=[5,2,5,2,2]
# for x_count in numbers:
#     output=''
#     for count in range(x_count):
#         output+='x'
#     print(output)
# LETTER L

# names=['JOHN','BOB','MOSH','SARAH','MARY']
# # names[0]='jon'
# print(names)
# # for x in names:
# #     print(x)

# largest number
# numbers=[3,6,2,15,4,10]
# max=numbers[0]
# for number in numbers :
#     if number>max:
#         max=number
#
# print(max)

# matrix=[
#    [1,2,3],
#    [4,5,6],
#     [7,8,9]
# ]
# # matrix[0][1]=20
# print(matrix[0][1])

# numbers= [5,4,6,3,21,1]
# numbers2=numbers.copy()
# numbers.append(10)
# print(numbers2)
# # numbers.append(20)
# # numbers.insert(0,5)
# # numbers.remove(5)
# # numbers.clear()
# # numbers.pop()
# # numbers.sort()
# # numbers.reverse()
# # print(numbers)
# # print(numbers.index(5))

# numbers=[2,2,4,6,3,4,6,1]
#
# for number in numbers:
#      print(number)

# removing dupicates
# numbers=[2,2,4,6,3,4,6,1]
# uniques=[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# TUPLES() && LISTS[]
# nbr=(1,2,3)
# x,y,z=nbr
# print((nbr[0])
#

#DICTIONARIES
# customer={
#     "name":"John Smith",
#     "age":30,
#     "is_verified":True
# }
# #print(customer["name"])
# #print(customer.get("name"))
# #customer["name"]="Jack Smith"
# customer["birth_date"]="Jan 1 1980"
# print(customer["birth_date"])
# #print(customer["name"])
# #print(customer.get("birth_date","JANUARY 1 2001"))

# number conversion to strings
# phone=input("Phone: ")
# digits_mapping={
#     '1':'one',
#     '2':'two',
#     '3':'three',
#     '4':'four',
#     '5':'five'
# }
# output=""
# for ch in phone:
#     output+=digits_mapping.get(ch,"!")+" "
# print(output)

#EMOJI CONVERTER
# message=input(">")
# words=message.split(' ')
# emojis={
#     ":)": "😂",
#     "):": "😪"
# }
# output=""
# for word in words:
#     output += emojis.get(word, word)+" "
# print(output)

#USING FUNCTIONS
# def greet_user():
#     print('Hi there')
#     print('Welcome abroad')
#
#
# print('start')
# greet_user()
# print('finish')




# def greet_user(first_name,l_name):
#
#     print(f'Hi {first_name} {l_name}!!')
#     print('Welcome on board')
#
#
# print('start')
# greet_user('JOHN','Smith')
# print('finish')

#passing argument
# def square(number):
#     return number*number
#
#
# m=int(input('enter nbr'))
# # square(m)
# print(square(m))


#emoji converter

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😂",
#         "):": "😪"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))

#EXCEPTIONS

# try:
#   age=int(input('Age: '))
#   income=20000
#   risk=income/age
#   print(f'age is {age} ')
#   print(f'risk {risk}')
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')


# CLASSES

# class Point:
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("Draw")
#
#
# point1=Point()
# point1.move()
# point1.draw()
# point1.x=10
# point1.y=20
# print(point1.x)
# print(point1.y)
#
# point2=Point()
# point2.x=1
# print(point2.x)


#CONSTRUCTORS////FAILED
# class Point:
#     def __int__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("Draw")


# point = Point(10,20)
#
# print(point.x)
#


# Exercise

# class Person:
#     def __init__(self,name):
#         self.name= name
#
#     def talk(self):
#         print(f"Hey I am {self.name} I talk less!!")
#
#
# john=Person("John Smith")
# # print(john.name)
# john.talk()
#
# bob=Person("Bob Smith")
# bob.talk()


# INHERITANCE

# class mammals:
#     def walk(self):
#           print("Walk")
#
#
# class Dog(mammals):
#     def bark(self):
#         print("balk")
#
#
# class Cat(mammals):
#
#     def annoying(self):
#         print("annoying cat")
#
#
# dog1=Dog()
# dog1.walk()
# cat1=Cat()
# cat1.annoying()

#MODULES

# import conveters
# from conveters import lbs_to_kg
# lbs_to_kg(100)
# print(conveters.lbs_to_kg(100))

# EXERCISE
# numbers =[10,3,6,20]
# max=numbers[0]
# for number in numbers:
#     if number>max:
#         max=number
#
# print(max)

from utils import find_max

numbers=[5,100,200,50,70,900,6]

maximum=find_max(numbers)

print(maximum(numbers))


