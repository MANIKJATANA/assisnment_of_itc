# creating list
marks_of_students=[]
 
# taking input
print("enter the marks of 5 students ")

# adding marks 
i=0
for i in range (5):
    mark=float(input("Enter mark of Student  " ))
    marks_of_students.append(mark)
   
    # sorting
marks_of_students.sort()
 
# printing
print(marks_of_students)
