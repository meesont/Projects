import random as r
numTimes = int(input('Enter the number of times to flip a coin: '))

heads, tails = 0, 0

def flipCoin():
    choice = r.choice([True, False])
    # print(choice)
    if(choice):
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(numTimes):
        if(flipCoin() == True):
            heads += 1
        else:
            tails += 1

    print(f'Heads - {heads}')
    print(f'Tails - {tails}')
