print("QUESTION 1")
s1="Python is a case sensitive language"
print("A    The length of string is             ",len(s1)) 
print("B    The reversed string is              ",s1[-1::-1])
# STORED a case sensitive IN A NEW STRING #c
s2=s1[10:26] 
#REPLACED "a case sensitive" with "object oriented"  #D
s2.replace("a case sensitive","object oriented")  
print("E    index of a is                       ",s1.find('a'))
print("F    string after removing whitespaces   ",s1.replace(" ",""))
print("\n \n \n")



name=input("ENTER YOUR name                 ")
SID=int (input("ENTER YOUR SID                  "))
department=input("ENTER YOUR department           ")
CGPA=float(input("ENTER YOUR CGPA                 "))
print("Hey %s,"%name,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%department,"and my CGPA is %f"%CGPA)
print("\n \n \n")



print("QUESTION 3")
a=56
b=10
print("A    a&b    ",a&b)
print("B    a|b    ",a|b)
print("C    a^b    ",a^b)
print("D Left shift of a 2 bits \n            ",a<<2) 
print("D Left shift of b 2 bits \n            ",b<<2) 

print("E    Right shift a with 2 bits \n            ",a>>2)
print("E    Right shift b with 4 bits \n            ",b>>4)
print("\n \n \n")



print("QUESTION 4")
n1 = input("Enter first number:         ")
n2 = input("Enter second number:        ")
n3 = input("Enter third number:         ")

if (n1 >= n2) and (n1 >= n3):
   largest = n1
elif (n2 >= n1) and (n2 >= n3):
   largest = n2
else:
   largest = n3

print("THE LARGEST NUMBER IS        ",largest)
print("\n \n \n")



print("QUESTION 5")
s=input("Enter the string ")
#checking whether name exist or not 
if (s.find('name') != -1):
    print ("Yes")
else:
    print ("No")
print("\n  \n \n")


print("QUESTION 6")
#taking input of sides of triangle a , b , c
a=int(input("Enter  first side of triangle "))
b=int(input("Enter  second side of triangle "))
c=int(input("Enter  third side of triangle "))
#condition for triangle
if(a>=(b+c)):
    print("No")
elif(b>=(a+c)):
    print("No")
elif(c>=(a+b)):
    print("No")
elif(a<0 or b<0 or c<0):
    print("no")
else:
    print("Yes")

