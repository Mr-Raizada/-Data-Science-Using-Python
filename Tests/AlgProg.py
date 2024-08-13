#Write a Program to compuute the value of the fallowing algbraic Exp
#1+x/y+x^x / 2+y/x+y^x

import math

x,y = input("Please provide with the Numbers : " ).split()
x=int(x)
y=int(y)

Equation = (1+ x/y +pow(x, x))/(2+y/x+pow(y,x))

print("The Solution for the equation is : ", Equation)
