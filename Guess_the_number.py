import random
import time

n=random.randint(1,30)
number_of_guesses=1
print("You have to guess the number between 1 and 30")
time.sleep(1)
total_guesses=int(input("How many total number of guesses do you want ? "))

while(number_of_guesses<=total_guesses):
	time.sleep(1)
	x=int(input("Enter your guessed number : "))
	if x not in range(1,31):
		print("Wrong Input (Guess won't be counted)")
	else:
		if(x<n):
			print("Your number is lesser than the required number. Try harder!")
		elif(x>n):
			print("Your number is greater than the required number. Try again!")
		else:
			break
		print("Total guesses left : ",total_guesses - number_of_guesses)
		number_of_guesses+=1

time.sleep(1)

if(x==n):
	print("Yay! You guessed it right ")
	time.sleep(1)
	print("Number of guesses you took : ",number_of_guesses)
else:
	print("You ran out of guesses!")
	time.sleep(1)
	print("The correct number was : ",n)