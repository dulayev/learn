n = 7

def ArrangeBrackets(spare_left, spare_right, state, depth):
    if spare_left == 0:
        for i in range(spare_right):
            state += ')'
        print(''.join(state))
    else:
        # add left anyway
        ArrangeBrackets(spare_left - 1, spare_right, state + ['('], depth + 1)
        if depth > 0:
            ArrangeBrackets(spare_left, spare_right - 1, state + [')'], depth - 1)

ArrangeBrackets(n, n, [], 0)
