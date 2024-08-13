#Write a Program to read the five real integers from the user and find the average the and S
import math

x1,x2,x3,x4,x5 =input("Provide 5 Different Values:  ").split()
x1= int(x1)
x2= int(x2)
x3= int(x3)
x4= int(x4)
x5= int(x5)

Average=(x1+x2+x3+x4+x5)/5
x1_avg=(x1-Average)*(x1-Average)
x2_avg=(x2-Average)*(x2-Average)
x3_avg=(x3-Average)*(x3-Average)
x4_avg=(x4-Average)*(x4-Average)
x5_avg=(x5-Average)*(x5-Average)

SD= math.sqrt((x1_avg+x2_avg+x3_avg+x4_avg+x5_avg)/5)

print("Average of five no is : ",Average)
print("Standered Deviation of 5 No is : " , SD)
