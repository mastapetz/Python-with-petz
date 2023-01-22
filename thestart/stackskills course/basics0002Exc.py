# Create three variables mood, strength, and rank and assign a string to mood, a float to strength, and an integer to rank. The values you assign can be anything as long as they are the of the correct type.
mood = 'Cranky'
strength = 6.9
rank = 1
print(type(mood))
print(type(strength))
print(type(rank))
# Assign numbers to x, y, and z. Calculate the sum of x, y, and z in s. Print out the value of s.
x = 3
y = 9
z = 11
# s = sum(x,y,z) //not like that

s = x +y +z #wanted solution

print(s)

# Assign a list to variable temperatures. The list should contain three items, a float, an integer, and a string. 

temperature = [ 6.9, 1, 'cranky']
print(temperature)

# Assign a list to variable rainfall. The list should contain four items, a float, an integer, a string, and a list. 
# Yes, there's nothing wrong with lists containing other lists. Lists can contain any type.

rainfall = [6.9,1,'cloudy',['food',69,4.2]]
print(rainfall)

# Complete the script so that it prints out the maximum value of student_grades. In other word, your duty is to find out the appropriate function or method that returns the maximum value of a list and store its output in max_value.

student_grades = [9.1, 8.8, 7.5]

max_value = max(student_grades)

print(max_value)

# Like the previous exercise, find the proper function or method that counts how many 10.0 items there are in student_gradesand print out the output using a print()function.

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

isInGrades = student_grades.count(10.0) #wanted solution, .count not findable in help and dir
print(isInGrades)

# Like the previous exercise, find the proper function or method that converts the string in usernameinto lowercase letters and prints out the output.

username = "Python3"
# lowerUsername = lower( username) #not quite
lowerUsername = username.lower()

print(lowerUsername)