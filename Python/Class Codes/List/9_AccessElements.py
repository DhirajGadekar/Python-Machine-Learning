player = ["Rohit", "Shubhman", "Virat", "Shreyash", "KL"]

print(player[0])
print(player[1])
print(player[2])
print(player[3])
print(player[4])

print(player[-1])
print(player[-2])
print(player[-3])
#print(player[-7])   IndexError : List Index out of range

#Slicing

print(player[2::])
print(player[2:4:2])
print(player[:5:3])

print(player[::3])
print(player[4:2:2])
print(player[4:2:-1])
