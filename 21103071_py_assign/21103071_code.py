#                                                            ASSIGNMENT 3


print("                                                      ASSIGNMENT 3 ")
print("\n")
print("\n")
#QUESTION 1

# Write a Python program to count the number of occurrences of each word or character in the string entered by the user. (Count the Number of Occurrences of each character only if the single word is entered by the user).

#QUESTION1
print("Question 1")
a=str(input("Enter the string : "))
#To split all the elements of string in a list
list=a.split() 
#initializing an empty dictionary
dict={} 
#if statement will be implemented when a single word is entered
if list.__len__()==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
#else statement eill be implemented when more than one word is entered in a string
else:                   
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")



#QUESTION 2
# Write a python script to print next date of input date. It must meet following conditions(use if-elif).


from pickle import TRUE
from subprocess import list2cmdline
print("Question 2")
def Next_Date():
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    #while loop is used so that if any wrong date is entered  then date will be entered again
    while(True):                 
        day=int(input("Enter the date  "))
        if(1<=day<=31):
            break
        else:
            print("Please enter a valid date")
    #while loop is used so that if any wrong month is entered  then month will be entered again
    while(True):                  
        month=int(input("Enter the month "))
        if(1<=month<=12):
            break
        else:
            print("Please enter a valid month")
    #while loop is used so that if any wrong year is entered  then year will be entered again
    while(True):                
        year=int(input("Enter the year "))
        if(1800<=year<=2025):
            break
        else:
            print("Please enter year from 1800 to 2025 only")

    
    if month in list1 :    
        if(day==31):
            day=1
            month=month+1
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("invalid try again ")
            Next_Date()
    
    elif month in list2 :
        if(day==30):
            day=1
            month=month+1  
            print(day,"/",month,"/",year)   
        elif(day<30):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("Invalid try again ") 
            Next_Date()      
    elif month in list3:
        if(year % 4 == 0):  
            if(day==29):
                day=1
                month=month+1
                print(day,"/",month,"/",year)
            elif(day<29):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("Invalid input try again")
                Next_Date()
        else:
            if(day==28):
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif(day<28):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("Invalid input try again")
                Next_Date()
    elif month in list4:
        if(day==31):
            day=1
            month=1
            year+=1  
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("Invalid input try again")
            Next_Date()
        
    else:
        print("Invalid input try again")
        Next_Date()
Next_Date()
print("\n")



# Question 3 
# Write a Python program to create a list of tuples with the first element as the number and Second element as the square of the number.
print("Question 3")
#input list
inputlist = input('Enter all the numbers in a single line separated by space')
user_list = inputlist.split()
# print list
print('list: ', inputlist)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
squarelist =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]

print(squarelist)

print("\n")


# Question 4 :
# Write a program to prompt the user for a grade between 4 and 10. If the grade is out of range print error message. If the grade is between 4 and 10 Print thegrade
print("Question 4")

def input_point():
    point = int(input("Enter Grade Point: "))
    # check if the grade point meets the conditions
    if point>10 or point<4:
        print("Invalid input try again ")
        point = input_point()
    return point
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")


# Question 5 
# Pattern Printing

print("\n\nQuestion 5: Pattern printing.\n")
x = 6
for rows in range(x):
    # printing spaces
    for space in range(rows):
        print(' ', end='')
    # printing alphabet
    for alphabet in range(2*(x-rows)-1):
        print(chr(65 + alphabet), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n")

# Question 6
# Write a python script that repeatedly ask user to enter name and SID of students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and values are student’s name.

# accepting input and checking whether user gave correct input

print("\n\nQuestion 6 : Dictionary functions and sorting.\n")
program_flow = True
user_data={}
while(program_flow):
    student_name = input("Enter name : ")
    input_ok = False
    while(input_ok == False):
        student_sid = input("Enter  SID  :")
        if student_sid.strip().isdigit():
            input_ok = True  
        else:
            print("\nSID can only be a combination of numbers!!! ")
        
    user_data[student_sid]=student_name
    str = "k"
    while(str.lower()!="y" and str.lower()!="n"):
        str=input("\nDo you want to store more student data (Y/N) : \n")
        if str.lower()=="n":
            program_flow = False
        elif str.lower()!="y" :
            print("\nPlease enter Y or N only!!!\n")
    
# a. Print students details stored in the dictionary.

print("\nStudent data in the order as entered by the user : ")
for student_sid , student_name in user_data.items() :
    print(student_sid," : ",student_name)

# b. Sort dictionary using student names.
sorted_names = sorted(user_data.values())
new_user_data ={}
for student_name in sorted_names:
    for student_sid , names in user_data.items():
        if(names==student_name):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student names :")
for student_sid ,student_name  in new_user_data.items() :
    print("{:<15}:{:<15}".format(student_sid,student_name))

# c. Sort dictionary using student sids.

sorted_sids = sorted(user_data.keys())
new_user_data ={}
for student_sids in sorted_sids:
    for student_sid , student_name in user_data.items():
        if(student_sid==student_sids):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student sids :")
for student_sid,student_name in new_user_data.items() :
    print(student_sid," : ",student_name)

# d. Search a student details with SID and print name of that student.

input_ok = False
while(input_ok == False):
    search_sid = input("\nEnter the SID whose name you want to search :")
    if search_sid.strip().isdigit():
        input_ok = True
    else:
        print("\nSID can only be a combination of numbers!!! ")

if search_sid in user_data:
    print("\nName of the student with SID {} is {}.".format(search_sid,user_data[search_sid]))
else:
    print("SID {} is not present in our data.".format(search_sid))
    


#QUESTION7
print("\n")
print("\n")
print("QUESTION 7")
#  Function to display the Fibonacci sequence
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
no_of_terms=int(input("Enter the number of terms  "))
if no_of_terms <= 0:     # Check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(fibo(i))
       sum=sum+fibo(i)
avg=float(sum/no_of_terms)
print("Average of fibbonacii series till n is ",avg)
print("\n")


# Question 8.
# Given the sets below, write python statement to:
# Set1= {1, 2, 3, 4, 5}
# Set2= {2, 4, 6, 8}
# Set3= {1, 5, 9, 13, 17}
print("Question 8 :  Set methods -  union , intersection , difference .")

#given sets are 
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}


# a. new set containing elements from set 1 and set 2 both but not the common one 
new_set = Set1.union(Set2) - Set1.intersection(Set2)
print("set of all elements that are in Set1 and Set2 but not both : ", new_set)

# b.  new set of all elements that are in only one of the three sets Set1, Set2 and Set3.

unique_element_set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("set of all elements that are in only one of the three above  sets : ",unique_element_set)

# c.new set of elements that are exactly two of the sets Set1, Set2 and Set3.  

exactly_two = ((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("set of elements that are exactly two of the sets : ",exactly_two)

# d.set of all integers in the range 1 to 10 that are not in Set1.

set_of_integers = set(x for x in range(1,11)) - Set1
print("\nNew set of all integers in the range 1 to 10 that are not in Set1 :", set_of_integers)

# e. Create a new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3.

set_new = set(x for x in range(1,11)) - (Set1|Set2|Set3)
print("\nNew set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3:",set_new)
