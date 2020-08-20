# 1) Write a program using python built in feature to remove repeated/duplicate characters/numbers

# var1 = 'organization' 
# var2 = [1,2,3,4,2,3,4,5,6,6]
# var3 = ''
# var4 = set(var1)
# for char in var4:
#     var3+=char
# print(var3)
# print(list(set(var2)))

# 2). Create a variable with following string.

# "Tom's response is "I'm good"
# s='Tom\'s response is "I\'m good'
# print(s)

# 3). Show different possible ways to get the value of mark.

# student = {
#     "name": "Tom",
#     "class": 8,
#     "mark": 75
# }

# print(student['mark']) 
# print(student.get('mark'))
# print(student.setdefault('mark',10))  

# 4) Show different possible ways to create an empty dictionary.

#     dict={}
#     dict1=dict()
  
# 5) Write a program in all possible ways to remove the ‘mark‘ element from a dictionary.

# student = {
#     "name": "Tom",
#     "class": 8,
#     "mark": 75
# }

# student.pop('mark')
# del student['mark']

# 6. Print the value of history without looping.

# sample_dict = {
#     "class": {
#         "student": {
#             "name": "Tom",
#             "mark": [
#                 ("physics", 70),
#                 ("history", 80)
#             ]
#         }
#     }
# }

# print(sample_dict['class']['student']['mark'][1][1])     

# 7) i) Get the list of all keys. ii) Get the list of all values.

# student = {
#     "name": "Tom",
#     "class": 8,
#     "marks": 75
# }

# list(student.keys())     # Getting all keys from dict
# list(student.values())   # Getting all values from dict

# 8). Write a code to sort a numerical list.

# list = ['2', '5', '7', '8', '1']

# list.sort()
# print(list) # printing the sorted list

    
# 9)Write a lambda function to add two numbers  and call the lambda function..
   
# addition = lambda num1,num2:num1+num2
# val = addition(5,4)
# print(val)

# 10). Print the common elements in the below list in optimal way.

# list_1 = [(4,), (5,), (6,), (8,)]
# list_2 = [(3,), (6,), (5,), (7,)]

# common=set(list_1).intersection(set(list_2))
# print(common)

# 11). Write a simple reg expression to search numbers in a string.

# import re
# search_list = re.findall(r'\d+', 'test_string123')
# print(search_list)

# 12) Using list comprehension, print list of all the even number from 0 to 20 and multiply each even number with 2

# even_list_mul_with_two=[num*2 for num in range(0,20) if num%2 == 0]
# print(even_list_mul_with_two)

# 13) Rewrite the following code in optimized way:

# week = {}
# week['sun'] = 0
# week['mon'] = 1
# week['tue'] = 2
# week['wed'] = 3
# week['thu'] = 4
# week['fri'] = 5
# week['sat'] = 6

# for key, value in week.items():
# 	if value%2 == 0:
# 		print(key, ':', value)
# 	else:
# 		print(key, ':', value)

# single line code:

# day_even_or_odd=[print(key, ':', value) if value%2 == 0 else print(key, ':', value) for  key, value in week.items()]

# 14) Rewrite the following code in optimized way:

# word = 'organization'
# mydict = {}
# for char in word:
#     if char not in mydict:
#         mydict[char] = 0
#     mydict[char] += 1
# print(mydict)

# mydict1 = {char:0 if char not in mydict else char:'dummy' for char in word}
# print(mydict1)\

# 15). Rewrite the following code in optimized way

# list1 = ['w', 'e', 'l', 'c', 'o', 'm', 'e']
# result = ''
# for c in list1:
#     result = result + c
# print(result)

# optiamal way:

# result=''.join(list1)
# print(result)


# 16) Rewrite the following code in optimized way:
# 	a = 1
# 	b = 2
# 	temp = a
# 	a = b
# 	b = temp
# 	print(a, b)

#optimal way:
#     a=1
#     b=2
#     a,b=b,a
#     print(a,b)

# 17. Write a simple reg expression to get port number in the route 'http://0.0.0.0:3000/tickets/dashboard/1'

# import re
# numbers = re.findall(r'\d+', 'http://0.0.0.0:3000/tickets/dashboard/1')
# print(numbers)

# 17) What does 'assert' and 'yield' keyword do in Python?

# assert:
#     a.The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
#     b.You can write a message to be written if the code returns False

#     Example:
#         x = "hello"
#         assert x == "goodbye", "x should be 'hello'"
#         output:
#             x should be hello
# yield:
#     yield is a keyword in Python that is used to return from a last yield statement to next yield statment in a function.it makes keep available of local variables even after execution one yield statement to access in other yield statement.

#     Example:
#         def mygen:
#             n=1
#             yield(n)
#             n+1=1
#             yield(n)
#         obj=mygen()
#         print(next(obj))
#         print(next(obj))

# 18. Explain 'pass', 'break' and 'continue'.

# pass:
#   The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
#     Example:
#         for x in range(10):
#             if x==5:
#                 pass
#             else:
#                 print(x)
# break:
#   The break statement is used to terminate entire loop.
#     Example:
#       for x in range(10):
#         if x==5:
#             break
#         else:
#             print(x)
# countinue:
#   The countinue statement is used to skip single iteration
#     Example:
#       for x in range(10):
#         if x==5:
#             countinue
#         else:
#             print(x)

# 19) What is the MRO in Python?    
# Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. Especially it plays vital role in the context of multiple inheritance as single method may be found in multiple super classes. To understand the concept of MRO and its need, lets examine a few cases.

# Example:
#     class A:
#     def method1(self):
#         print("from the A class")
#     class B:
#         def method1(self):
#             print("from B class")
#     class C(A,B):
#         def method2(self):
#             self.method1()
#     class D(B,A):
#         def method2(self):
#             self.method1()
#     obj=C()
#     obj.method2()#from A class it is calling method2
#     obj=D()
#     obj.method2()#from B class it is calling method2  nothing but MRO

# 20. Write a sample program with method overriding.
# ---------------------------------------------------
#     Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes
#     Example:
#     --------
#     # Defining parent class 
#     class Parent(): 
#     # Constructor 
#     def __init__(self): 
#         self.value = "Inside Parent"
          
#     # Parent's show method 
#     def show(self): 
#         print(self.value) 
          
#     # Defining child class 
#     class Child(Parent): 
      
#     # Constructor 
#     def __init__(self): 
#         self.value = "Inside Child"
          
#     # Child's show method 
#     def show(self): 
#         print(self.value) 
#     # Driver's code 
#     obj1 = Parent() 
#     obj2 = Child() 
  
#     obj1.show() 
#     obj2.show()     


# 21. Write the function to print first user 'print_first_user(user_list)' in optimal way. In this logic, print only the first email id which is having a prefix 'user' but the email id should not contain 'admin'.

# def find_users(users):
#     for user in users:
#         if user.startswith('user'):
#             email = user.split(':')
#             if not email[1].startswith('admin'):
#                 print(email[1])

# users = ['group:dev@gmail.com', 'group:admin@gmail.com', 'user:tom@gmail.com', 'user:jerry@gmail.com','user:admin@gmail.com']
# find_users(users)

          
   