from os import path
import random
d = path.dirname(__file__)
print("d:", d)
print('hsl(0, 0%%, %d%%)' % random.randint(60, 100))