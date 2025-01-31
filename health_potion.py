import random

#health variable
health = 75

#gathering user input that determines difficulty level
difficulty = int(input("Please choose a difficulty level between 1 and 3. 1 is easy, 2 is medium, and 3 is hard: "))

#randomly selects an integer value between 0 and 25 which is then divided by the difficulty level
potion_health = int(random.randint(0,25) / difficulty)

#updating health
health += potion_health

#new updated health
print(f"You started off with 75 health, and now your health is {health}.")