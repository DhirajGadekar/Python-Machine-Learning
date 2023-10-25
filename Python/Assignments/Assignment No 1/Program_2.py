"""
2. Program 2: Write a Program to check whether the number is Negative,
Positive or equal to Zero.
Input: -2
Output: -2 is the negative number
"""

num = int(input("Enter Value : "))

if num > 0 :
	print(num, " is the positive number")
elif num < 0 :
	print(num, " is the negative number");
else :
	print(num, " is neither positive nor negative");
