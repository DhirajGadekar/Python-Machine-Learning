"""
3. Write a Python program to count the number of even and odd numbers in a series of numbers
   Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    Expected Output :
    Number of even numbers : 5
    Number of odd numbers : 4
"""

number = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = 0
odd_count = 0

for i in number :
    if i % 2 == 1 :
        even_count += 1
    else :
        odd_count += 1

print("Number of even numbers : {}".format(even_count))
print("Number of odd numbers : {}".format(odd_count))
