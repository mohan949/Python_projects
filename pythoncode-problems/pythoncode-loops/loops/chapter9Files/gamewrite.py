
import random


def game():
    print(' you are playing the game.. ')
    score = random.randint(1, 100)
    print(score)
    with open('myfiles.txt','r') as f:
        highscore = f.read()
        if(highscore=='' ):
            highscore = int(score)
    
    print(f'your score is {score}')
    if (score>highscore):
        with open('myfiles','w') as f :
            f.write(str(score))

    return score


game()



