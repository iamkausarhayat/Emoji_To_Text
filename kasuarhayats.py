# # import random

# # print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

# # low = int(input("Enter the Lower Bound: "))
# # high = int(input("Enter the Upper Bound: "))

# # print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

# # num = random.randint(low, high) 
# # ch = 7                       # Total allowed chances
# # gc = 0                        # Guess counter

# # while gc < ch:
# #     gc += 1
# #     guess = int(input('Enter your guess: '))

# #     if guess == num:
# #         print(f'Correct wow mashallah saqib . allah aap ko khush rakeee, congratulation50! The number is {num}. You guessed it in {gc} attempts.')
# #         break

# #     elif gc >= ch and guess != num:
# #         print(f'Sorry! The number was {num}. Better luck next time.')

# #     elif guess > num:
# #         print('Too high! Try a lower number.')

# #     elif guess < num:
# #         print('Too low! Try a higher number.')


# def square(n):
#     """Taken a number n , return the square of number n"""
#     print(n**2)
#     square(5)
#     print(square)
#     print(square.__doc__)
def fact(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * fact(n-1)

print(fact(5))  
