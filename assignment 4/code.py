
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




print(" with the help of loops ")
for i in range(n):
    for spacing  in range(n-i+1):
        # for spacing
        print(end="  ")
    for j in range(i+1):
        # by using the formula of   nCr = n!/((n-r)!*r!
        print(factorial(i)//(factorial(j)*factorial(i-j)), end="    ")
    # for new line
    print()

print("\n")
print("\n")

#QUESTION 3
print("QUESTION 3")

def fun(a,b):
    quotient=a//b
    remainder=a%b
    print("The quotient is-",quotient)
    print("The remainder is-",remainder)
    result=[quotient,remainder]
    return result


print("PART A ")
a=int(input("ENTER the first number-"))
b=int(input("ENTER the second number-"))
result=fun(a,b)
print(result)
print("Callable-",callable(fun))

print("PART B")
print("a is zero-",a==0)
print("b is zero-",b==0)
print("quotient is zero-",result[0]==0)
print("remainder is zero-",result[1]==0)
if(a==0):
    print("a is zero")

print("PART C")
#adding 4 5 6 in the result
d=[4,5,6]
result=result+d
print(result)
alist=[]
for i in result:
    if i>4:
        alist.append(i)
print("The values greater than 4-",alist)

print("PART D")
#converted the list to a set
aset=set(alist)
print(aset)

print("PART E")
#immutable set
immutable_set=frozenset(aset)
print("The required immutable set IS        ",immutable_set)

print("   PART F ")
#max value from the set
#hash value
maxval=0
for i in immutable_set:
    if i>maxval:
        maxval=i
print("The required max value is-",maxval)
print("The required hash value is-",hash(maxval))

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
print(p1.name)
print(p1.rollnum)

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


#QUESTION 6
print("QUESTION 6 ")
def anagram(word):
    if len(word)==1:
        return [word]
    partial_words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        


George_word=input("Please give a word  ")
George_word=George_word.lower()
Possible_words=anagram(George_word)


Barbie_word=input("Give a word-  ")
Barbue_word=Barbie_word.lower()

print("Possible Words-",Possible_words)

# If Barbie's word lies in the list,then their friendship is real.

if Barbie_word in Possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")
    
