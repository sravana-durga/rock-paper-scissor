import symbol
import random

  
def game():
        computer_score = 0
        user_score = 0
        choices = {1:'rock',2:'paper',3:'scissor'}
        for i in range(3):
            try:
                print()
                op = int(input('Enter 1 to choose rock:\nEnter 2 to choose paper:\nEnter 3 to choose scissor:\n'))
                if op in (1, 2, 3):
                    computer = random.randint(1,3)
                    
                    op = choices[op]
                    computer = choices[computer]
                    print(f'Your choice is:{op}',f'Computer choice is:{computer}',sep='\t\t\t\t')
                    for i in range(19):
                        print(symbol.options[f'{op}'][i],symbol.options[f'{computer}'][i],sep='\t')
                    print()


                    if op == computer:
                        print('The game is Draw')

                    elif (op == 'rock' and computer == 'paper') or (op == 'paper' and computer == 'scissor') or (op == 'scissor' and computer == 'rock') :
                        computer_score+=1
                        print("Computer won")
                        
                    
                    else:
                        user_score+=1
                        print("You won")
                        
                    
                else:
                    print('Invalid input')
                    computer_score+=1

            except Exception:
                print('Invalid input')

        print('TOTAL SCORES:')
        print('Your Score is:',user_score)
        print('Computer Score is:',computer_score)
        if user_score == computer_score:
            print('Game is Draw')
        elif user_score>computer_score:
            print('You won')
        else:
            print('Computer won')
        op = input('Want to play again(Y/n)? ')
        if op.upper() == 'Y':
            game()
        else:
            print('---------THANK YOU----------')


if __name__ == '__main__':
    print('------------------WELCOME TO-----------------------')
    print('----------ROCK,PAPER AND SCISSCOR GAME-------------')

    print('''RULES:
1. There are 3 chances in this game.
2. Enter valid input, or else you will loose a chance''')
     
    op = input('Want to play(Y/N)?:')
    if op.upper() == 'Y':
        game()

    else:
        print('---------THANK YOU----------')


