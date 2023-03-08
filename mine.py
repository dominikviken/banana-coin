from os import system
from random import randint
from time import sleep

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '#', '!']
wordList = ['iskaffe', 'iste', 'cola']

for x in wordList:
    wordList[wordList.index(x)] = " ".join(x)

randomLetters = []
x = 0
y = 0

printLength = 30
coinChance = 1000

system('cls')

def giveCoins(arg):
    with open("coins.txt") as fin:
        fin.seek(0)
        coins = fin.read(9999 - 0)
        coins = int(coins)
        coins += arg
    f = open("coins.txt", 'w')
    f.write(str(coins))
    f.close()

while x != printLength:
    letter = letters[randint(0, (len(letters)-1))]
    randomLetters.append(letter)
    x += 1
    
    if x == printLength:
        printLength = randint(5, 30)
        sleep(0.075)
        randomLettersJoin = ' '.join(randomLetters)
        print(randomLettersJoin)
        
        for x in wordList:
            if x in randomLettersJoin:
                print('found ' + ''.join((x.split(' '))) + '!')
                print('got 5 banana coins!')
                giveCoins(5)
                sleep(5)
                system('cls')
            
        randomLetters.clear()
        if randint(1, coinChance) == coinChance:
            print('got banana coin!')
            giveCoins(1)
            sleep(2)
            system('cls')
        x = 0