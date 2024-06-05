print('the rules are Rock beats scissor, scissor beat paper, and paper beats rock.')
computer_score=0
player_score=0
import random
op='y'
while op=='y':
    computer_choice=random.choice(['rock','paper','scissor'])
    player_input=input('Enter Rock, Paper or scissor: ')
    player_input=player_input.lower()
    print('players choice: ',player_input)
    print('computer_choice: ',computer_choice)
    if(player_input==computer_choice):
        print('TIE')
    elif ((computer_choice=='rock'and player_input=='scissor')or(computer_choice=='paper'and player_input=='rock')or(computer_choice=='scissor'and player_input=='paper')):
        print('computer won this turn')
        computer_score=computer_score+1
    else:
        print('player won this turn')
        player_score=player_score+1
    op=input("IF You Want to Continue press y: ")
print('player score: ',player_score)
print('computer score: ',computer_score)
if(computer_score==player_score):
    print("it's a tie match")
elif(computer_score<player_score):
    print('Player Wins!')
else:
    print('Computer Wins')

