"""
Program 1: Write a Program to Find a Maximum between two numbers
	Input: 1 2
	Output: 2 is Max number between 1 & 2 
"""

num1 = int(input("Enter value 1 : "))
num2 = int(input("Enter value 2 : "))

if num1 > num2 :
	print(num1 , " is Max number betwwen ", num1, " & ", num2);
elif num1 < num2 :	
	print(num2 , " is Max number betwwen ", num1, " & ", num2);
else :
	print(num1 , " & ", num2 , " are Equal.");
