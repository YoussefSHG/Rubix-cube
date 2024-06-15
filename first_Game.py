import random

game = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for i in range(1, 7):
    lt = []
    for x in range(9):
        lt.append(i)
    game[i] = lt
modelgame = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
for i in range(1, 7):
    lt = []
    for x in range(9):
        lt.append(i)
    modelgame[i] = lt

positions = {'ST': [0,1,2], 'SM': [3,4,5], 'SB': [6,7,8], 'TL': [0,3,6], 'TM': [1,4,7], 'TR': [2,5,8]}
rounds = [[1, 2, 3, 4], [1, 6, 3, 5], [2, 6, 4, 5]]
replacers = [1,2,3]

cw = [6,3,0,7,4,1,8,5,2]
acw = [2,5,8,1,4,7,0,3,6]

n = 1
s = ['ST', 'SM', 'SB', 'TL', 'TM','TR']
p = False

# rubix mechanics
def play(inp):
    temp = []
    round = []
    if inp in ['ST', 'SM', 'SB']:
        round = rounds[0]
    elif inp in ['TR', 'TM', 'TL'] and n in [1, 5, 3, 6]:
        round = rounds[1]
    elif inp in ['TR', 'TM', 'TL'] and n in [2, 4]:
        round = rounds[2]

    for r in round:
        for i in positions[inp]:
            temp.append(game[r][i])
    for i in  replacers:
        temp.insert(i-1, temp[-i])
    for i in range(3):
        del temp[12]
    m = 0
    for r in round:
        for i in positions[inp]:
            game[r][i] = temp[m]
            m += 1

    if inp in ['ST', 'SB', 'TR', 'TL']:
        if round == rounds[0]:
            if inp == 'ST':
                RF = 5 
                R = 'acw'
            elif inp == 'SB':
                RF = 6
                R = 'cw'
            elif inp == 'TR':
                if n == 4:
                    RF = 1
                else:
                    RF = n+1
                R = 'acw'
            elif inp == 'TL':
                if n == 1:
                    RF = 4
                else:
                    RF = n-1
                R = 'cw'
        else:
            if inp == 'ST':
                if n == 5:
                    RF = 3
                    R ='acw'
                else:
                    RF = 1
                    R = 'cw'
            elif inp == 'SB':
                if n == 5:
                    RF = 1
                    R = 'acw'
                else:
                    RF = 3
                    R = 'cw'
            elif inp == 'TR':
                RF = 2
                R = 'acw'
            elif inp == 'TL':
                RF = 4
                R = 'cw'
        T1 = []
        if R == 'cw':
            for i in cw:
                T1.append(game[RF][i])
        elif R == 'acw':
            for i in acw:
                T1.append(game[RF][i]) 
        game[RF] = T1
    return game

#display info
ind = '-------------'

def faces(game):
    line0 = '1 {0}{1}{2}  2 {3}{4}{5}  3 {6}{7}{8}'.format(game[1][0], game[1][1], game[1][2], game[2][0], \
        game[2][1], game[2][2], game[3][0], game[3][1], game[3][2])
    line1 = '  {0}{1}{2}    {3}{4}{5}    {6}{7}{8} \t\t 5 '.format(game[1][3], game[1][4], game[1][5], game[2][3],\
        game[2][4], game[2][5], game[3][3], game[3][4], game[3][5])
    line2 = '  {0}{1}{2}    {3}{4}{5}    {6}{7}{8}'.format(game[1][6], game[1][7], game[1][8], game[2][6],\
        game[2][7], game[2][8], game[3][6], game[3][7], game[3][8])
    line3 = '\t\t\t      4  1  2  3 '
    line4 = '4 {0}{1}{2}  5 {3}{4}{5}  6 {6}{7}{8}'.format(game[4][0], game[4][1], game[4][2], game[5][0],\
        game[5][1], game[5][2], game[6][0], game[6][1], game[6][2])
    line5 = '  {0}{1}{2}    {3}{4}{5}    {6}{7}{8} \t\t 6 '.format(game[4][3], game[4][4], game[4][5], game[5][3],\
        game[5][4], game[5][5], game[6][3], game[6][4], game[6][5])
    line6 = '  {0}{1}{2}    {3}{4}{5}    {6}{7}{8}'.format(game[4][6], game[4][7], game[4][8], game[5][6],\
        game[5][7], game[5][8], game[6][6], game[6][7], game[6][8])
    return line0, line1, line2, line3, line4, line5, line6

def help():
    line0 = 'Commands:'
    line1 = 'play ST: to rotate top coloumn     modes help: for commands                    show 1 to 6: to show selected face'
    line2 = '     SM: to rotate middle column           faces: for showing all faces  '
    line3 = '     SB: to rotate bottom column           stats: for showing your status'
    line4 = '     TL: to rotate left row         '
    line5 = '     TM: to rotate middle row       '
    line6 = '     TR: to rotate right row                                                    eg(mode help)'
    return line0, line1, line2, line3, line4, line5, line6

def stats():
    line0 = 'Stats:'
    line1 = ''
    line2 = 'e5bat dema8ak fel 7et '
    line3 = ''
    line4 = ''
    line5 = ''
    line6 = ''
    return line0, line1, line2, line3, line4, line5, line6   

# displayer
def display(game, mode):
    line0 = mode[0]
    line1 = mode[1]
    line2 = mode[2]
    line3 = mode[3]
    line4 = mode[4]
    line5 = mode[5]
    line6 = mode[6]
    display = '{ind}\t{l0}\n| {0} | {1} | {2} |\t{l1}\n{ind}\t{l2}\n| {3} | {4} | {5} |\t{l3}\n{ind}\t{l4}\n| {6} | {7}' \
          ' | {8} |\t{l5}\n{ind}\t{l6}\n'.format(
    game[n][0], game[n][1], game[n][2], game[n][3], game[n][4], game[n][5], game[n][6], game[n][7], game[n][8],
    ind=ind, l0=line0, l1=line1, l2=line2, l3=line3, l4=line4, l5=line5, l6=line6)
    return display

def error(inp):
    while True:
        if inp[0] not in ['MODE', 'PLAY', 'SHOW'] or inp[0] == 'MODE' and inp[1] not in ['HELP', 'STATS', 'FACES'] or inp[0] == 'PLAY' and \
    inp[1] not in positions or inp[0] == 'SHOW' and int(inp[1]) not in game:
            inp = str(input('unkown command please reenter command\n')).upper().split()
        else:
            break
    return inp

mode = faces(game)
m = 'f'

inp = input('enter no. of random moves: ')
for i in range(int(inp)):
    r = random.randint(0,5)
    game = play(s[r])
    mode = faces(game)
    print('Face {0}\n{1}please enter your next move.\n'.format(n, display(game, mode)))


inp = str(input('Face {0}\n{1}please enter your next move.\n'.format(n, display(game, mode)))).upper().split()
inp = error(inp)

if inp[0] == 'MODE':
    if inp[1] == 'HELP':
        mode = help()
        m = 'h'

    if inp[1] == 'FACES':
        mode = faces(game)
        m = 'f'

    if inp[1] == 'STATS':
        mode = stats()
        m = 's'
    
    print(display(game, mode))

if inp[0] == 'PLAY':
    if m == 'f':
        mode = faces(game)
    elif m == 's':
        pass
    print(display(play(inp[1]), mode))
    p = True

if inp[0] == 'SHOW':
    n = int(inp[1])
    print(display(game, mode))

while True:
    inp = str(input('enter command\n')).upper().split()
    inp = error(inp)
    if inp[0] == 'PLAY':
        game = play(inp[1])
        if m == 'f':
            mode = faces(game)
        elif m == 's':
            pass
        print(display(game, mode))
        p = True

    if inp[0] == 'MODE':
        if inp[1] == 'HELP':
            mode = help()
            m = 'h'

        if inp[1] == 'FACES':
            mode = faces(game)
            m = 'f'

        if inp[1] == 'STATS':
            mode = stats()
            m = 's'

        print(display(game, mode))

    if inp[0] == 'SHOW':
        n = int(inp[1])
        print(display(game, mode))

    if game == modelgame and p == True:
        print(game, modelgame)
        break