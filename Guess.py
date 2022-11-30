import random
import sys


def genNum():
    numKey = random.randint(1, sys.maxsize)
    return numKey


numKey = genNum()
while True:
    print 'Can you guess the number?'
    answer = input('Guess : ')
    if answer.isdigit():
        if int(answer) < numKey:
            print str(answer) + ' is to low!'
        elif int(answer) > numKey:
            print str(answer) + ' is to high!'
        elif int(answer) == numKey:
            print str(answer) + ' is correct!'
            con = input('Continue? :')
            if con.lower() == 'yes':
                numKey = genNum()
                continue
            elif con.lower() == 'no':
                print 'Quitting!'
                quit()
    else:
        print 'You need to use numbers!'
        continue
