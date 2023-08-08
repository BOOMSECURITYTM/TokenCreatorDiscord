import random

char = 'abcdefghijklmnopqrstuvwz123456789'

for i in range(100* 1000* 10):
    frist = ''.join((random.choice(char)for i in range(24)))

    sec = ''.join((random.choice(char)for i in range(6)))

    endR = ''.join((random.choice(char)for i in range(26)))

    resualt = frist + '.' + sec + endR

    output = open('Tokens.txt' , 'a')
    output.write(resualt + '\n')

    print(f'' + resualt, end='')
