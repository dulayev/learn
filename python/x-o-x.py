import random

def SomebodyWins(field, who): # who can be who or 'o'
    if field[0][0] == who and field[1][1] == who and field[2][2] == who:
        return True
    if field[0][2] == who and field[1][1] == who and field[2][0] == who:
        return True
    
    if field[0][0] == who and field[0][1] == who and field[0][2] == who:
        return True
    if field[1][0] == who and field[1][1] == who and field[1][2] == who:
        return True
    if field[2][0] == who and field[2][1] == who and field[2][2] == who:
        return True
    
    if field[0][0] == who and field[1][0] == who and field[2][0] == who:
        return True
    if field[0][1] == who and field[1][1] == who and field[2][1] == who:
        return True
    if field[0][2] == who and field[1][2] == who and field[2][2] == who:
        return True 

    return False

def Replace(text, pos, replace_with):
    return text[:pos] + replace_with + text[pos + 1:]

def PrintField(field):
    for line in field:
        print('|' + line + '|')

def InputHumanMove(field, play_for): # play_for is 'x' or 'o'
    move_good = False
    while not move_good:

        move = int(input("Let's make a move! Enter number 1-9:"))
        if move < 1 or move > 9:
            print("Enter number 1-9!")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if field[row][col] != ' ':
            print("Cell is occupied")
            continue

        move_good = True
        field[row] = Replace(field[row], col, play_for)

def ComputerMove(field, play_for): # play_for is 'x' or 'o'
    move_good = False
    while not move_good:
        
        row = int(random.uniform(0, 2.99))
        col = int(random.uniform(0, 2.99))
        
        if field[row][col] != ' ':
            continue
        
        move_good = True
        field[row] = Replace(field[row], col, play_for)

def FieldFull(field):
    if " " in  field[0] + field[1] + field[2]:
        return False
    else:
        return True


def Test():    
    assert SomebodyWins(["xoo", "oxo", "oox"], 'x')
    assert SomebodyWins(["oox", "oxo", "xoo"], 'x')
    assert SomebodyWins(["oox", "oxo", "ooo"], 'o')
    assert SomebodyWins(["xxx", "   ", "   "], 'x')
    assert SomebodyWins(["x  ", "x  ", "x  "], 'x')
    some_field = ["x  ", " o ", " x "]
    PrintField(some_field)
    InputHumanMove(some_field, 'x')
    PrintField(some_field)
    print()
    ComputerMove(some_field, 'o')
    PrintField(some_field)
    assert Replace("mouse", 0, "l") == "louse"
    assert Replace("pool", 3, "r") == "poor"
    
            
#Test()        
    
# clear field
field = ["   ", "   ", "   "]
game_over = False
while not game_over:
    InputHumanMove(field, "x")
    PrintField(field)
    if SomebodyWins(field, "x"):
        print("Human won!")
        game_over = True
        break
    if FieldFull(field):
        print("Game over")
        game_over = True
        break
    ComputerMove(field, "o")
    print()
    PrintField(field)
    if SomebodyWins(field, "o"):
        print("Human lost!")
        game_over = True
        break
    if FieldFull(field):
        print("Game over")
        game_over = True
        break
    

   
    
    

# do step until somebody wins
# computer plays X, human plays O

# input human step

# check if human won, if won print 'you win' and exit
# if no empty cells print 'draw' and exit

# make computer step

# check if computer won, print 'you lost' and exit
# if no empty cells print 'draw' and exit
