# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 14:06:25 2025

@author: dhruv
"""
#Input the integer n for which numbers are to be considered
n=int(input("Input a value of n"))
#Input the integer l for with lth digit will be displayed
l=int(input("Enter the digit you wish to find"))
digit=[]
h=0
for i in range(1,n+1):
    if i<=9:
        digit.append(i)
    else:
        k=str(i)
        for m in range(0,len(k)):
            d=int(k[m])
            digit.append(d)
#print(digit)
print("The digit you wished to find",digit[l-1])
r=int(input("Enter a number which will be consider the digit to find the number"))
y=(r//2)+10
newdigit=[]
for i in range(1,y+1):
    if i<=9:
        newdigit.append(i)
        h+=1
        if r-1==h:
            NumNd=i
    else:
        k=str(i)
        for m in range(0,len(k)):
            d=int(k[m])
            newdigit.append(d)
            h=h+1
            if r==h:
                NumNd=int(k)
#print(newdigit)
print("The digit number",r, "is from the number",NumNd)
