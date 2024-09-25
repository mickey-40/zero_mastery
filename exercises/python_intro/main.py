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

some_list = [ 'a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
second_list = []


for item in some_list:
  if some_list.count(item) > 1:
    if item not in second_list:
      second_list.append(item)
      
print(second_list)

        

