import random
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = random.choice(nums)
guess = 10
while a != guess:
    guess = int(input("Guess a number 1-9: "))
print("Well guessed!")