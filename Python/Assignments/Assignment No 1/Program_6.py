"""
Program 6: Write a Program to check whether the Character is Alphabet or
not.
Input: v
Output: v is an alphabet.
"""

char = input("Enter Alphabete : ")

if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') :
    print(char, " is an alphabete")
else :
    print(char, " is not an alphabate")
