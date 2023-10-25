"""
Program 9: Write a program to check whether the input character is a vowel or
consonant
Input: ‘a’
Output: vowel
Input: ‘b’
Output: consonant
"""

char = input("Enter value of char : ")

if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' ):

    print("vowel")
else :
    print("Consonant")
