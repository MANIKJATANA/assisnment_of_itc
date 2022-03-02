
#                                                            ASSIGNMENT 4


print("                                                      ASSIGNMENT 4 ")
print("\n")
print("\n")
#QUESTION 1
print("QUESTION 1")

def Tower_Of_Hanoi(n , source, destination , helper):
	if n == 0:
		return
	Tower_Of_Hanoi(n-1, source, helper, destination)
	print("Move disk",n,"from rod",source,"to rod",destination)
	Tower_Of_Hanoi(n-1, helper, destination, source)
n = 3
Tower_Of_Hanoi(n, 'A', 'C', 'B')
print("\n")

#QUESTION 2
print("QUESTION 2")
from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))


print("by using recursion ")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")




print(" with the help of  for loop ")
for i in range(n):
    for spacing  in range(n-i+1):
        # for spacing
        print(end=" ")
    for j in range(i+1):
        # by using the formula of   nCr = n!/((n-r)!*r!
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    # for new line
    print()

print("\n")
print("\n")

print(" with the help of  while loop ")

i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y+=1
    i+=1
    print()

print("\n")
print("\n")



#QUESTION 3
print("QUESTION 3")

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

# as we have to use ony built in functions only..
# using  a inbuilt function  divmod()  to find quotient and remainder 
# divmod() -> it accepts two number and returns tuple containing quotient and remainder


quotient , remainder = divmod(a,b)

print(f"Quotient obtained is  : {quotient}\nRemainder obtained is : {remainder}")

print("\na. Check whether function/values is callable or not .\n")

if callable(divmod):
    print("Function used is callable")
else:
    print("Function used is not callable ")

if callable(a):
    print(f"Value {a} used is callable")
else:
    print(f"Value {a} is not callable ")

if callable(b):
    print(f"Value {b} used is callable")
else:
    print(f"Value {b} is not callable ")

print("\nb. Check whether all the values are non zeroes or not .\n")

values = [quotient,remainder,a,b]
if 0 not in values:
    print("None of the given values and the quotient and remainder obtaineed is zero .")
else:
    if a==0 :
        print("First value of the given input is zero.")
    if b==0:
        print("Second value of the given input is zero.")
    if quotient==0:
        print("Quotient obtained is zero.")
    if remainder==0:
        print("Remainder obtained is zero.")

print("\nc. Add values (4, 5, 6) to the result and filter out the values which are greater than 4.\n")
values.extend([4,5,6])
filtered_values = sorted(list( x for x in values if x>4 ))

print("The filtered values which are greater than 4 are  :",filtered_values)

print("\nd. Convert the above result into set datatype.\n")

# considering the result mentioned in question is the result of filtured values.

new_set = set(filtered_values)

print("The result that is of values greater than 4 is converted to set :",new_set)

print("\ne. Make that set immutable.\n")

# to make a iterable like set , lists or dicstionaries immutable we use frozenset() function which
# accepts those iterables as arguments and returns a immutable object of the same form.

immutable_set = frozenset(new_set)
print("Set has been made immutable.")

print("\nf. Evaluate the maximum value from set and find out its hash value\n")
maximum_value = filtered_values[0]
for value in immutable_set :
    if value > maximum_value:
        maximum_value = value

print("Maximum value in  the set is ",maximum_value)

# Hash values are special type of coded values used to identify some values or strings or data and it changes as that data change .
# It is different if same value considered as different data type.

print("\nHash values for the  maximum value according to the considerration :")
print("if it is considered as a integer then :",hash(maximum_value))
print("if it is considered as a string then :",hash(str(maximum_value)))

print("\n")
print("\n")


#QUESTION 4
print("QUESTION 4")

class Student:
    def __init__(self,name,rollnum):
        self.name=name
        self.rollnum=rollnum
    def __del__(self):
        print("Destructor called,The object is destroyed.")


p1=Student("MANIK JATANA ",21103071)
print("object has been created  with name and rollnum as below ")
print(p1.name)
print(p1.rollnum)

del p1
print("\n")
print("\n")


print("QUESTION 5 ")
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

p1=Employee("Mehak",40000)
p2=Employee("Ashok",50000)
p3=Employee("Viren",60000)

print("part a ")
#updating salary of Mehak (employe 1) to 70000
p1.salary=70000
print(f"<a> The updated salary of {p1.name} is {p2.salary} ")

print("part b ")
#deleting the record of employe 3 ( viren)
del p3
print("Record of Viren have deleted sucessfully " )

print("\n")
print("\n")


print("\nQuestion 6. To check if friendship is true or not .\n")
george_word = input("Enter your word George :")
barbie_word = input("Enter your word Barbie and remember it must be consistig of same words as George word letters only :  ")

if len(george_word)==len(barbie_word):
    friendship=False
    for letter in george_word.lower():
        if letter not in barbie_word.lower():
            print("\nBarbie's word  deos not contain same  letters as George's word .")
            print("  FAKE FRIENDSHIP ")
            break
        else:
            friendship=True
    if friendship:
        print("\nBarbie your word  contains same  letters as George's word .")
        print(" TRUE FRIENDSHIP  ")
        
        
else:
    print("\nBarbie's word  deos not contain same  letters as George's word .")
    print("   FAKE FRIENDSHIP ")

