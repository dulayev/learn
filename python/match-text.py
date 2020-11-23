import collections

MatchState = collections.namedtuple('MatchState', ['match_count', 'transitions'])

def create_match_machine(text):
    state_machine = []
    state = MatchState(0, {})
    state_machine.append(state)

    def func_recur(state, start_pos):
                

    func_recur(state, 0)

    for i in range(len(text)):
        
    return state_machine

def exec_match_machine(machine, text):
    state = machine[0]

    for c in text:
        if c in state.transitions:
            state = machine[state.transitions[c]]
        else:
            return state.match_count

machine = create_match_machine("fox")
count = exec_match_machine(machine, "fox on street")
assert(count == 3)
