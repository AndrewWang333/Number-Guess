import random
print("Enter a number from 1-100 nub")
n= int(input())
x= random.randint(1,101)
while(x!=n):
   	if(n>x):
		print("your guess is higher than the number")
		n= int(input())
	elif(n<x):
		print("your guess is lower than the number")
		n= int(input())

print("you guessed the number!")
	