import copy

players = ['Peter', 'Huan']


moves = [lambda s: s + 3, lambda s: s * 2 + 1]

win = lambda s: s >= 85

cases = []

def game(player_index, pile, made_moves):
    for move_index in range(len(moves)):
        new_pile = moves[move_index](pile)
        
        new_moves = copy.deepcopy(made_moves)
        
        new_moves[player_index] += str(move_index)
        print(player_index, pile, '->', new_pile, new_moves[player_index])
        if win(new_pile):
            cases.append(new_moves)
            print(new_pile, new_moves)
        else:
            game((player_index + 1) % 2, new_pile, new_moves)

for s in range(43, 44):
    cases = []
    result = game(0, s, ['',''])
    #print(cases)
    
    
    #if result == (1, 1) or result == (2, 1):
    #    print(s)

