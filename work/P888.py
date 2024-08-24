def mex(s):
    i = 0
    while i in s: i += 1
    return i

def moves(state):
    for i in range(len(state)):
        for j in [1, 2, 4, 9]:
            if state[i] >= j:
                state[i] -= j
                yield state.copy()
                state[i] += j
        z = state.pop(i)
        for j in range(1, z//2):
            state.append()

