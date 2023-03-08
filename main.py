import random
from time import sleep

with open("coins.txt") as fin:
    fin.seek(0)
    coins = fin.read(9999 - 0)

print('you have')
sleep(random.randint(1, 4))
print(f'{coins} banana coin/s')
input('Press enter to start mining..')

import mine