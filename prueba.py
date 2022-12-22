# seed the pseudorandom number generator
from random import seed
from random import random
# seed random number generator
seed(3)
# generate some random numbers
print(100*random(), random(), random())
# reset the seed
seed(1)
# generate some random numbers
print(random(), random(), random())