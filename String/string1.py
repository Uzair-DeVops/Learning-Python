# # # "Quaid e Azam" : '   '
# # # # uzair
# # #     #  uzair
# # #            # uzair
# # #                  uzair
# # #                      uzair
# # #                 uzair
# # #             uzair
# # #         uzair
# # #     uzair
# # # uzair

# # # string_1 = ''' 'hello' 
# # # "world" '''
# # # print(string_1)



# # # Accessing character in String using index
# # 1
# # # String1 = "GeeksForGeeks"
# # # print("Initial String: ", String1)

# # # print(String1[7])
# # # print(String1[-7])
# # # print(String1[20])

# # # Slicing

# # # Creating a String
# # # String1 = "GeeksForGeeks"
# # # print("Initial String: ")
# # # print(String1)

# # # # Printing 3rd to 12th character
# # # print("\nSlicing characters from 5-8: ")
# # # print(String1[5:8])

# # # Python String Reversed

# # name = "Uzair Yasin "
# # # [start : end : step]
# # # print(name[0:7:3])
# # print(name[::-2])
# # print(name)



# # # 1 . n a e (10 times) (index)
# # # 2 . my name is this (10 times) (slicing)
# # # 3 .   6 step (20 times )
# # # # 4 . 10 string (10 times) 

# # # Python Program to Update
# # # character of a String

# # String1 = "Hello, I'm a Geek"
# # print("Initial String: ")
# # print(String1)

# # # Updating a character of the String
# # ## As python strings are immutable, they don't support item updation directly
# # ### there are following two ways
# # #1
# # list1 = list(String1)
# # print(list1)
# # list1[2] = 'p'
# # String2 = ''.join(list1)
# # print("\nUpdating character at 2nd Index: ")
# # print(String2)

# #2
# # String3 = String1[0:2] + 'p' + String1[3:]
# # print(String3)


# # Deleting/Updating from a String

# # name = "Uzair Yasin"
# # print(name)
# # list1 = list(name)
# # print(list1)
# # print(type(list1))

# # list1[0]= "Z"
# # string1 = " ".join(list1)
# # print(string1)


# # Type casting
# # # name = "Uzair Yasin"
# # # integer = int(name)
# # float1 = 2.0
# # print(type(float1))
# # print(float1)
# # integer2 = int(float1) 
# # print(type(integer2))
# # print(integer2)
# # # print(type(name))
# # # print(type(integer))

# # Escape Sequence 
# # name = "Muhammad \"Uzair\" 'Yasin'"
# # # \n to move to nxt line
# # # \t to add space equals to one tab or 4 space bars
# # # \"uzair\"

# # print(name)

# # strig 5 time convert list  , 5  tuple , 5 set
# # 10 times
# quote = "\"Quaid-e-Azam\" said : \n\t\t\tWork , Work and Work" 
# print (quote)

#  String Methods

#  Lower func = to make all characters in lower case
# name = "UZAIR YASIN"
# name2 = name.lower()
# print(name)
# print(name2)

#  Upper func = to make all characters in Upper case
# name = "Uzair yasin"
# name2 = name.upper()
# print(name)
# print(name2)

#  Title func = to make the first character of the word  in Upper case
# name = "uzair yasin"
# name2 = name.title()
# print(name)
# print(name2)

#  swapcase func = to make all  Upper case into lower and all the lower case in upper case
# name = "MUHAMMAD uzair YASIN"
# name2 = name.swapcase()
# print(name)
# print(name2)

# #  Capitalize func = to make all first character of the first word in Upper case and make all other lower case
# name = "uzaiR YaSiN"
# name2 = name.capitalize()
# print(name)
# print(name2)

#  Casefold func = to make all characters in lower case  same as lower case func
# name = "ß"
# name2 = name.casefold()
# name3 = name.lower()
# print(name)
# print(name2)
# print(name3)

# # center() = to create space if you gave any other
# name = "Uzair YaSin"
# name2 = name.center(70, ".")
# print(name)
# print(name2)

# Endswith() 

# string = "geeksforgeeks"
# print(string.endswith("geek"))

# text = "geeks for geeks."

# result = text.endswith('for geeks.')
# print (result)

# result = text.endswith('geeks.')
# print (result)

# result = text.endswith('for geeks.')
# print (result)

# result = text.endswith('geeks for geeks.')
# print (result)

# text = "geeks for geeks."

# result = text.endswith('eks', 12 , 15)
# print(result)



 
# # expantabs()

# string = "i\tlove"

# # using expandtabs to insert spacing
# print (string)
# print(string.expandtabs(16))
# print()

# Find()
# string = " hello world is the first code of every first programmer first"
# print(string.find("de"))
# print(string.find("first" ,21))
# print(string.find("first" ,41))

