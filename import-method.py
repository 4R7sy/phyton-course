import math
import random
## You choose a number
n1 = int(input("Write your first number: "))
## And the Bot too
n2 = random.randint(1, 50)
##We plus them
r = n1 + n2
##Find the Square root
sr = math.sqrt(r)
##And finally we can print it
print("So {} + {} is {}, and your square root is {}.".format(n1, n2, r, sr))