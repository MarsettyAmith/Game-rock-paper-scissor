import random
def gamewin(pc, you):
    if pc == you:
        print('Its a Tie!')
    elif pc == 'r':
        if you=='p':
            print('You win!')
        elif you == 's':
            print('You lose!')
    elif pc == 'p':
        if you=='s':
            print('You win!')
        elif you == 'r':
            print('You lose!')
    elif pc == 's':
        if you=='r':
            print('You win!')
        elif you == 'p':
            print('You lose!')
            # return pc , you
print("pc Turn completed now its")
randNo = random.randint(1, 3)
if randNo == 1:
    pc = 'r'
if randNo == 2:
    pc = 'p'
if randNo == 3:
    pc = 's'
you = input('Your turn :Rock(r) Paper(p) Scissor(s)\n')
a = gamewin(pc, you)

print(f'computer chose {pc}')
print(f'You chose {you}')