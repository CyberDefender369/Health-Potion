import random

#declaring health variable
health = 50

#gathering user input that determines difficulty level
difficulty = int(input("Please choose a difficulty level between 1 and 3. 1 is easy, 2 is medium, and 3 is hard: "))

#potion_health randomly selects an integer value between 25 and 50
#which is then divided by the difficulty variable
potion_health = int(random.randint(25,50) / difficulty)

#updating health
health += potion_health

#displaying new updated health
print(health)