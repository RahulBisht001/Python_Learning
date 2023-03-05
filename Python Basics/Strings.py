# Strings are Nothing but the collection of Characters
course = 'Python For "Beginners"'
course = "Python For 'Beginners'"

print(course)
print(type(course))

# ------ More About Strings Methods ------------

# Question ?

# what if we want to use the single and double Quotes in the same String ?
# ans -> we can put a backslash character followed by a quote ( \" or \' )
course = " \'python\' for \"Beginners\""
#
print(course)
#
# Ques -> How to Write the MultiLine Strings ??
# ans -> use triple Quotes (anyone ' or " )

msg = """
Hi Rahul , I Hope
You are Doing great and
enjoying too.
"""
print(msg)
# ---------------------------------------------------#
# Indexing
String = "Hello Python"

# Operations on String based on indexing
print(String[0])
print(len(String))  # getting the length of the String
print(String[11])  # from left to right it starts with 0 indexing
print(String[-12])  # in right to left indexing starts with 1
print(String[-2])

# ---------------------------------------#
# String method
# W3Schools = https://tinyl.io/7x88
# Python docs : https://tinyl.io/7x8B


stringName = "hello Python Programming"
print(stringName[0:5])  # it will leave the last index
print(stringName[0:])
print(stringName[:len(stringName) - 3])
strEx = stringName[:]
print(strEx)

# 1. Capitalize()
newString = stringName.capitalize()
print(newString)

# 2. upper()
newString = stringName.upper()
print(newString)

# 3. isdigit()
strEx = '234'
print(strEx.isdigit())

strEx = '323ffs3'
print(strEx.isdigit())

# 4 .islower()
strEx = 'raJU'
print(strEx.islower())

#  5.
instructor = "mosh"
stringName = "Python learning"

# Just Like template literals in JavaScript
print(stringName + " with " + f'{instructor}')

# find the first occurrence of the given value
print(stringName.find('earn'))

# Replace any Character Or subString with Give Value(String)
print(stringName.replace('P', 'Video'))
print(stringName)

# in Operator -> It checks the existence of any Character or subString in the given String
print('Python' in stringName)
