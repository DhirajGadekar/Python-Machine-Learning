"""
2. Write a Python program that accepts a word from the user and reverses it.

"""

word = input("Enter String : ")
start = 0
end = len(word) - 1;

reverse = ""
for i in range(len(word) - 1, -1, -1) :
    reverse += word[i]

print(reverse)
