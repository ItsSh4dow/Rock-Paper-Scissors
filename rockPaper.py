import random, sys
def mySolution():
    print('ROCK, PAPER, SCISSORS ')
    wins = 0 
    losses = 0
    ties = 0

    while True:
        print(f'{wins} wins, {losses} losses, {ties} ties')
        playerMove = input('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit\n-->').lower()
        machineMove = random.randint(1,3) # 1 to Rock, 2 to Paper, 3 Scissors 
        if(playerMove == 'r'):
            print('ROCK versus...')
            if (machineMove == 1):
                print('ROCK')
                print('It is a tie! ')
                ties +=1
            elif(machineMove==2):
                print('PAPER')
                print('You lose :( ')
                losses +=1
            else:
                print('Scissors')
                print('You win! ')
                wins +=1
        # Second move
        elif(playerMove == 'p'):
            print('PAPER versus...')
            if (machineMove == 1):
                print('ROCK')
                print('You win! ')
                wins +=1
            elif(machineMove==2):
                print('PAPER')
                print('It is a tie! ')
                ties +=1
            else:
                print('Scissors')
                print('You lose :( ')
                losses +=1
        #Third move
        elif(playerMove == 's'):
            print('SCISSORS versus...')
            if (machineMove == 1):
                print('ROCK')
                print('You lose! ')
                losses +=1
            elif(machineMove==2):
                print('PAPER')
                print('You win! ')
                wins +=1
            else:
                print('Scissors')
                print('It is a tie! ')
                ties +=1
        elif (playerMove == 'q'):
            print('See you!')
            sys.exit()
        else:
            print('Type one of r, p, s, or q.')
      

mySolution()
