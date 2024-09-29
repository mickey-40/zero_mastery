# name = input('What is your name?')

# print('hello ' + name)

# Fundamental Data Types
# int & float 
# print(4+4)
# print(2-4)
# print(type(2*4))
# print(type(2/4))

# print(2**3)
# print(5//2)
# print(5%4)

# Math functions
# print(round(3.1))
# print(round(3.9))
# print(abs(3.1))
# print(abs(-3.1))

# operator precedence

# ()
# **
# * /
# + -
# print((5 + 4) * 10 / 2)

# print(((5 + 4) * 10) / 2)

# print((5 + 4) * (10 / 2))

# print(5 + (4 * 10) / 2)

# print(5 + 4 * 10 // 2)

# bin data types
# print(bin(5))
# print(int('0b101', 2))


# bool
# str
# list
# tuple
# set
# dict

#Classes -> custom types

# Specialized data types

None

# variables- snake_case 
# pi = 3.14 #can be changed
# PI = 3.14 #is a constant and can not be changed
# multiple assignments
# a,b,c = 4,2,1
# print(a, b, c)

# expressions-piece of code that produces a value
# statements-statement that preforms an action

# augmented assignment operator
# some_value = 5
# some_value += 2
# print(some_value)

# String
# str - uses ‘ ‘ or “ “ anything can go into the single or double quotes
# Long_string = ‘’’
# Wow
# O O 
# —
# ‘’’ 3 single quotes for long strings or multi-line strings

# String concatenation adding strings together

# ‘Hello’ + ‘Mickey’

# Escape Sequences

# Inside a string \ lets python know that the next thing is a string or different functions like tab or go to next line

# Formated strings

# name = ‘Johnny’
# age = 55

# print(f’hi {name}. You are {age} years old’)

# Python 2
# name = ‘Johnny’
# age = 55

# print(’hi {}. You are {} years old’.format(name,age))

# Change order

# print(’hi {1}. You are {0} years old’.format(name,age))

# Create Variables

# print(’hi {0}. You are {1} years old’.format(name=’sally’,age=100))

# String Indexes

# sentence = ‘Me me me’

# Indexes start at 0 so sentence[0] = ‘M’

# String slicing
# #  [start : stop : stepover]

# So sentence[0:2] = ‘Me’

# So sentence[0 : 8 : 2] = ‘Mmm’

# Sentence[: : -1] = ‘em em eM’

# Strings are Immutabile 

# Type Conversion
# Example:
# birth_year = int(input(‘what year were you born?’))

# age = 2024 - birth_year

# print(f‘your age is:{age}’)

# List is a data structure

# The square brackets keeps different data types

# amazon_cart = [ ‘notebook’, ‘sunglasses’]

# print(amazon_cart[0])

# List slicing same as strings

# amazon_cart = [ ‘notebook’, ‘sunglasses’, ‘toys’, ‘grapes’]

# print(amazon_cart)

# Matrix
# matrix = [
#   [1,2,5],
#   [3,4,6],
#   [9,0,7]
# ]

# print(matrix[0][1])

# bastet = ['a', 'b', 'c', 'd', 'e']

# print('a' in bastet)
# List unpacking
# Example:
# a,b, c, *other = [1,2,3,4,5,6,7]

# print(a) output = 1
# print(b) output = 2
# print(c) output = 3
# print(other) output = [4,5,6,7]

# a,b, c, *other, d = [1,2,3,4,5,6,7,8]

# print(a) output = 1
# print(b) output = 2
# print(c) output = 3
# print(other) output = [4,5,6,7]
# print(d) output = 8 last element

# Dictionary (dict) - data type and structure

# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 10:35:42 2020

# @author: saura
# """
# my_dict = {
#     'a' : [1,2,3],
#     'b' : "hello",
#     'c' : True
#     }

# my_list = [
#     {
#     'a' : [1,2,3],
#     'b' : "hello",
#     'c' : True
#     },
#     {
#     'a' : [4,5,6],
#     'b' : "bye",
#     'c' : False
#     }
#     ]

# print(my_dict["a"])
# print(my_dict["a"][1])
# print(my_list[1]["a"][2])

# Dictionary keys have to be immutable 


# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 11:33:18 2020

# @author: saura
# """
# my_tuple = (1,2,3,4,5,2)
# print(my_tuple[0])
# print(my_tuple[1:2])    # be carefull here, we also get a 'comma' when we just store a signle tuple value
# print(my_tuple[0:2])
# print(my_tuple[::-2])
# print(2 in my_tuple)

# # my_tuple[0] = 4     # it will be an error, because tuple are immutable
# print(my_tuple)

# print(my_tuple.count(2))
# print(my_tuple.index(5))

# my_dict = {
#     "age": 45,
#     (1,2): "hello"
#     }
# print(my_dict)
# print(my_dict.items())   # returns key:value pair as a tuple
# print(my_dict[(1,2)])

# a,b,c,*other = (1,2,3,4,5,6,7,8,9)  # it stores as list if the variable has more than 1 item, otherwise as int.
# print(a)
# print(type(a))
# print(other)
# print(type(other))


# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 11:55:22 2020

# @author: saura
# """
# my_set = {1,2,3,4,5,5,5}
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# # print(my_set[0])  # we cannot do this, it produces an error, because set is an unordered collection of objects
# print(len(my_set))

# print(5 in my_set)
# print(my_set)

# print(list(my_set))

# new_set = my_set.copy()
# print(my_set.clear())
# print(my_set)
# print(new_set)

# my_list = [1,2,3,4,5,5,5]
# print(set(my_list))     # this way we can remove the duplicate items from the list

# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 12:15:33 2020

# @author: saura
# """
# # this is very similar to Venn diagrams.

# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}

# # .difference()
# # .discard()
# # .difference_update()
# # .intersection()
# # .isdisjoint()
# # .issubset()
# # .issuperset()
# # .union()

# print("\ndifference")
# print(my_set.difference(your_set))
# print(my_set)

# print("\ndiscard")
# print(my_set.discard(5))
# print(my_set)

# print("\ndifference_update")
# print(my_set.difference_update(your_set))
# print(my_set)

# my_set = {1,2,3,4,5}

# print("\nintersection")
# print(my_set.intersection(your_set))
# print(my_set & your_set)

# print("\nisdisjoint")
# print(my_set.isdisjoint(your_set))
# my_set = {1,2,3}
# print(my_set.isdisjoint(your_set))

# print("\nissubset")
# print(my_set.issubset(your_set))
# my_set = {4,6,8}
# print(my_set.issubset(your_set))

# print("\nissuperset")
# print(my_set.issuperset(your_set))
# print(your_set.issuperset(my_set))

# print("\nunion")
# my_set = {1,2,3,4,5}
# print(my_set.union(your_set))
# # or
# print(my_set | your_set)

# Ternary Operator

# condition_if_true if condtion else condition_if_else

# is_friend = False

# can_message = "message allowed" if is_friend else "not allowed to message"

# print(can_message)

# Short Circuiting- when one is true or false and does not check the second condition
# is_Friend = True
# is_User = True

# if is_Friend or is_User:
#   print('best friends forever')

# is_magician = True
# is_expert = True

# if is_magician and is_expert:
#   print("you are a master magician")
# elif is_magician and not is_expert:
#   print('at least you\'re getting there')
# else:
#   print('you need magic powers')

# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# sum = 0
# for item in my_list:
#   sum += item
#   counter+=1

# print(sum)
# print(counter)

# for number in range(0,100):
#   print(number)

# for number in range(0,100,2):
#   print(number)

# for i,char in enumerate('Hellooo'):
#   print(i, char)

# want to be told what the index of 50 is
# for i,char in enumerate(list(range(100))):
#   if char == 50:
#     print(i)

# print * when it is a 1 and a empty space when 0

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for a_list in picture:
#   the_picture = ''
#   for item in a_list:
#     if item == 0:
#       the_picture += ' '
#     else:
#       the_picture += '*'
#   print(the_picture)
# # alternate answer
# for a_list in picture:
#   for item in a_list:
#     if item == 0:
#       print(' ', end='')
#     else:
#       print('*', end='')
#   print('')


# check for duplicates in a list

# some_list = [ 'a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# second_list = []


# for item in some_list:
#   if some_list.count(item) > 1:
#     if item not in second_list:
#       second_list.append(item)
      
# print(second_list)

        

# Python basics
# print()

# Data Types
# int - integer
# float - floating point number
# bool
# str
# list
# tuple
# set
# dict
# complex-  only use if doing complex math like real numbers
# Bin- returns binary 

# Math operators
# ** exponent 2 power of 3 - 2 ** 3
# // divide floor 5 // 2 = 2 returns an integer
# Modulo % 5 % 2 = 1 returns remainder 

# Math functions
# round()
# abs()

# # expressions-piece of code that produces a value
# # statements-statement that preforms an action

# # augmented assignment operator
# some_value = 5
# some_value += 2
# print(some_value)

# String
# str - uses ‘ ‘ or “ “ anything can go into the single or double quotes
# Long_string = ‘’’
# Wow
# O O 
# —
# ‘’’ 3 single quotes for long strings or multi-line strings

# String concatenation adding strings together

# ‘Hello’ + ‘Mickey’

# Escape Sequences

# Inside a string \ lets python know that the next thing is a string or different functions like tab or go to next line

# Formated strings

# name = ‘Johnny’
# age = 55

# print(f’hi {name}. You are {age} years old’)

# Python 2
# name = ‘Johnny’
# age = 55

# print(’hi {}. You are {} years old’.format(name,age))

# Change order

# print(’hi {1}. You are {0} years old’.format(name,age))

# Create Variables

# print(’hi {0}. You are {1} years old’.format(name=’sally’,age=100))

# String Indexes

# sentence = ‘Me me me’

# Indexes start at 0 so sentence[0] = ‘M’

# String slicing
# #  [start : stop : stepover]

# So sentence[0:2] = ‘Me’

# So sentence[0 : 8 : 2] = ‘Mmm’

# Sentence[: : -1] = ‘em em eM’

# Strings are Immutabile 

# Type Conversion
# Example:
# birth_year = int(input(‘what year were you born?’))

# age = 2024 - birth_year

# print(f‘your age is:{age}’)

# List is a data structure

# The square brackets keeps different data types

# amazon_cart = [ ‘notebook’, ‘sunglasses’]

# print(amazon_cart[0])

# List slicing same as strings

# amazon_cart = [ ‘notebook’, ‘sunglasses’, ‘toys’, ‘grapes’]

# print(amazon_cart

# # Matrix
# # matrix = [
# #   [1,2,5],
# #   [3,4,6],
# #   [9,0,7]
# # ]


# # print(matrix[0][1])


# bastet = ['a', 'b', 'c', 'd', 'e']


# print('a' in bastet)




# List unpacking
# Example:
# a,b, c, *other = [1,2,3,4,5,6,7]

# print(a) output = 1
# print(b) output = 2
# print(c) output = 3
# print(other) output = [4,5,6,7]

# a,b, c, *other, d = [1,2,3,4,5,6,7,8]

# print(a) output = 1
# print(b) output = 2
# print(c) output = 3
# print(other) output = [4,5,6,7]
# print(d) output = 8 last element

# Dictionary (dict) - data type and structure

# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 10:35:42 2020

# @author: saura
# """
# my_dict = {
#     'a' : [1,2,3],
#     'b' : "hello",
#     'c' : True
#     }

# my_list = [
#     {
#     'a' : [1,2,3],
#     'b' : "hello",
#     'c' : True
#     },
#     {
#     'a' : [4,5,6],
#     'b' : "bye",
#     'c' : False
#     }
#     ]

# print(my_dict["a"])
# print(my_dict["a"][1])
# print(my_list[1]["a"][2])

# Dictionary keys have to be immutable 


# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 11:33:18 2020

# @author: saura
# """
# my_tuple = (1,2,3,4,5,2)
# print(my_tuple[0])
# print(my_tuple[1:2])    # be carefull here, we also get a 'comma' when we just store a signle tuple value
# print(my_tuple[0:2])
# print(my_tuple[::-2])
# print(2 in my_tuple)

# # my_tuple[0] = 4     # it will be an error, because tuple are immutable
# print(my_tuple)

# print(my_tuple.count(2))
# print(my_tuple.index(5))

# my_dict = {
#     "age": 45,
#     (1,2): "hello"
#     }
# print(my_dict)
# print(my_dict.items())   # returns key:value pair as a tuple
# print(my_dict[(1,2)])

# a,b,c,*other = (1,2,3,4,5,6,7,8,9)  # it stores as list if the variable has more than 1 item, otherwise as int.
# print(a)
# print(type(a))
# print(other)
# print(type(other))


# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 11:55:22 2020

# @author: saura
# """
# my_set = {1,2,3,4,5,5,5}
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# # print(my_set[0])  # we cannot do this, it produces an error, because set is an unordered collection of objects
# print(len(my_set))

# print(5 in my_set)
# print(my_set)

# print(list(my_set))

# new_set = my_set.copy()
# print(my_set.clear())
# print(my_set)
# print(new_set)

# my_list = [1,2,3,4,5,5,5]
# print(set(my_list))     # this way we can remove the duplicate items from the list

# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 12:15:33 2020

# @author: saura
# """
# # this is very similar to Venn diagrams.

# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}

# # .difference()
# # .discard()
# # .difference_update()
# # .intersection()
# # .isdisjoint()
# # .issubset()
# # .issuperset()
# # .union()

# print("\ndifference")
# print(my_set.difference(your_set))
# print(my_set)

# print("\ndiscard")
# print(my_set.discard(5))
# print(my_set)

# print("\ndifference_update")
# print(my_set.difference_update(your_set))
# print(my_set)

# my_set = {1,2,3,4,5}

# print("\nintersection")
# print(my_set.intersection(your_set))
# print(my_set & your_set)

# print("\nisdisjoint")
# print(my_set.isdisjoint(your_set))
# my_set = {1,2,3}
# print(my_set.isdisjoint(your_set))

# print("\nissubset")
# print(my_set.issubset(your_set))
# my_set = {4,6,8}
# print(my_set.issubset(your_set))

# print("\nissuperset")
# print(my_set.issuperset(your_set))
# print(your_set.issuperset(my_set))

# print("\nunion")
# my_set = {1,2,3,4,5}
# print(my_set.union(your_set))
# # or
# print(my_set | your_set)






# Docstrings- information you put in a function

# Def test(a):
# 	‘’’
# 	Info: this function tests and prints param 
# 	‘’’
# 	print(a)

# If you type test(‘a’) and hover over it. It will show you your docstring on that function or use help() by type help(test) and it will do the same thing

# *args and **kargs (arg and karg can be any word but do not change it. The * and ** are the important part)


# Def func(*args):
# 	print(args) //wll print out all the params 
# 	return sum(args) /will return 15


# func(1,2,3,4,5)

# def func(*arg, **kwargs):
# 	print(kwargs) prints dictionary 
# 	Total = 0
# 	For items in kwargs.values():
# 		Total += items
# 	Return sum(args) + total // return 30

# func(1,2,3,4,5, num=5, num1=10)

# Rule: param, *arg, default param, **kwargs

# There is new syntax := that assigns values to variables as part of a larger expression. It is affectionately known as “the walrus operator” due to its resemblance to the eyes and tusks of a walrus.
# In this example, the assignment expression helps avoid calling len() twice:
# if (n := len(a)) > 10:
#     print(f"List is too long ({n} elements, expected <= 10)")


# A similar benefit arises during regular expression matching where match objects are needed twice, once to test whether a match occurred and another to extract a subgroup:
# discount = 0.0
# if (mo := re.search(r'(\d+)% discount', advertisement)):
#     discount = float(mo.group(1)) / 100.0


# The operator is also useful with while-loops that compute a value to test loop termination and then need that same value again in the body of the loop:
# # Loop over fixed length blocks
# while (block := f.read(256)) != '':
#     process(block)


# Another motivating use case arises in list comprehensions where a value computed in a filtering condition is also needed in the expression body:
# [clean_name.title() for name in names
#  if (clean_name := normalize('NFC', name)) in allowed_names]
#  Scope rules:
# 1 start with local
# 2 Parent local
# 3 Global 
# 4 built in python function










# OPP 

# class is the blueprint of what you are going to make.

# class BigObject: # Class uses camelcasing instead of snakecase 
# 	#code
# 	pass # because no code is here

# obj1 = BigObject() #instanciate
# obj2= BigObject() #instanciate
# obj3 = BigObject() #instanciate

# Exercise Cats Everywhere

# Given the below class:

# class Cat:
#     species = 'mammal'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# #Answers:
# # 1 Instantiate the Cat object with 3 cats.
# cat1 = Cat('cat1', 5)
# cat2 = Cat('Cat2', 7)
# cat3 = Cat('Cat3', 3)


# # 2 Create a function that finds the oldest cat.
# def oldest_cat(*args):
#     return max(args)


# # 3 Print out: "The oldest cat is x years old.".
# # x will be the oldest cat age by using the function in #2
# print(f'Oldest Cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

# inheritance
# class User:
#   def sign_in(self):
#     print('logged in')

# class Wizard(User):
#   pass

# class Archer(User):
#   pass


# bob_w = Wizard()


# class SuperList(list):
     
#   def __len__(self):
#     return 1000

# super_list1 = SuperList()

# print(len(super_list1))
# super_list1.append(5)
# print(super_list1)
# super_list1[0]
# print(issubclass(SuperList, list))

# lambda expressions- no name annoumous functions only used once

# from functools import reduce
# my_list = [1,2,3]

# def multiply_by2(item):
#   return item*2

# def only_odd(item):
#   return item%2 != 0

# print(list(map(lambda item: item*2, my_list)))
# print(my_list)

# Square exercise

# my_list = [ 5, 4, 3]

# print(list(map(lambda item: item * item, my_list )))

# list sorting
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# a.sort(key=lambda x: x[1])

# print(a)

# list, set, dictionary Comprehensions

# format 
#  my_list = [param for param in iterable]



# my_list = [char for char in 'hello']
# this replaces
# for char in 'hello':
#   my_list.append(char)

# my_list2 = [num for num in range(0, 100)]

# or
# for num in range(0, 100):
#   my_list2.append(num)

# my_list3 = [num**2 for num in range(0,100)]

# my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
# sets are the same as list
# dictionaries are different
# simple_dict = {
#   'a': 1,
#   'b': 2
# }
# my_dict = {key:value**2 for key,value in simple_dict.items() }

# my_dict = {num: num*2 for num in [1,2,3]}

# print(my_dict)

# comprehension exercise find the duplicates

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n','n']

# duplicates = list(set([value for value in some_list if some_list.count(value) > 1 ]))

# print(duplicates)

# decorators - gives functions more features @

# def my_decorator(func):
#   def wrap_func():
#     print('********')
#     func()
#     print('********')
#   return wrap_func

# @my_decorator
# def hello():
#   print('helloooo')

# hello()
# with a param
# def my_decorator(func):
#   def wrap_func(*args, **kwargs):
#     print('*******')
#     func(*args, **kwargs)
#     print('********')
#   return wrap_func

# @my_decorator
# def hello(greeting, emoji):
#   print(greeting, emoji)


# hello('hi', ':)')
# from time import time

# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1} s')
#     return result
#   return wrapper


# @performance
# def long_time():
#   for i in range(100000000):
#     i*5

# long_time()

# Error Handling
# while True:
#   try:
#     age = int(input('What is your age?'))
#     print(age)
#   except:
#     print('please enter a number')
#   else:
#     print('thank you')
#     break

# def sum(num1, num2):
#   try:
#     return num1 + num2
#   except TypeError as err:
#     print(err)

# print(sum('1', 2))

# while True:
#   try:
#     age = int(input('What is your age?'))
#     print(age)
#   except:
#     print('please enter a number')
#   else:
#     print('thank you')
#     break
#   finally:
#     print('ok, i am finally done')

while True:
  try:
    age = int(input('What is your age?'))
    print(age)
    raise Exception('hey cut it out')
  except:
    print('please enter a number')
  else:
    print('thank you')
    break
  finally:
    print('ok, i am finally done')