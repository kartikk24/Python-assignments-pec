
print('hello world')
x=44
y=45
print(x+y)
 

#Q1
num1=int(input('Enter number : '))
print(num1)
num2=int(input('Enter number : '))
print(num2)
num3=int(input('Enter number :' ))
print(num3)

print((num1+num2+num3)/3)

#Q2
inc=int(input("enter income : "))
num_of_dep=int(input("enter a number of dependants : "))
tax=(inc-10000)-(num_of_dep*3000)
print("tax to be paid is ",tax/5)

#Q3
sec=int(input('Enter the number of seconds : '))
print(sec)
minutes=sec/60
seconds=sec%60
print('Your ans is /n')
print(int(minutes),'minutes ',seconds,'seconds')

#Q4
a=int(25)
b=float('25')
c=float(25.0)
d=a+b+c
print(d)

#Q5
import math
for i in range(0,360,15):
    print(i, '---', round(math.sin(i*3.14/180),4),round(math.cos(i*3.14/180),4))



