import random
chance=5
a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print=("welcome to number guessing game")
b=random.choice(a)
print("a numberfrom 0-15")
while chance!=0:
c=int(input("guess my number:"))
if (b==c):
print("your the winner")
break
else:
print("try again")
chance = chance-1
print("Game over,answer is:",b)
