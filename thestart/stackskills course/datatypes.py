#list [] item, ... mutable
studentGrades =[9.1,  8.8, 7.5]

gradeSum = sum(studentGrades)
gradeLength = len(studentGrades)

avgGrade = gradeSum / gradeLength
print(avgGrade)

#dictionaries {} key: value = item mutable
#can be filled from external files with extras
studentGradeswName ={"Mary": 9.1, "Sam": 8.8, "John": 7.5}

gradeSum = sum(studentGradeswName.values())
gradeLength = len(studentGradeswName)

avgGrade = gradeSum / gradeLength
print(avgGrade)

#tuples () item,... imutable 
myTuple = (2,4,9)