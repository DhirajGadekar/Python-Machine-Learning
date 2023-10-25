"""
Program 5: Write a Program to take an integer ranging from 0 to 6 and print
corresponding weekday (week starting from Monday)
Input: 2
Output: Wednesday.
"""

num = int(input("Enter Value : "))

if num == 0 :
        print("Monday")
elif num == 1 :
	print("Tuesday")
elif num == 2 :
	print("Wednesday")
elif num == 3 :
	print("Thursday")
elif num == 4 :
	print("Friday")
elif num == 5 :
	print("Saturday")
elif num == 6 :
	print("Sunday")
else :
	print("Invalid Data")
