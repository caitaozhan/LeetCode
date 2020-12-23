'''

Given an input string (s) and a pattern (p), 
implement wildcard pattern matching with support for ‘?’ where ‘?’ matches zero or one arbitrary character.

Example 1:
Input: s = “aa”, p=“a”
Output: False

Example 2:
Input: s=“microsoft”, p=“m?croso?ft”
Output: True

Example 3:
Input: s=“google”, p=“go?pple”
Output: False

'''


def match(s: str, p: str) -> bool:
    '''recursive matching
    '''
    if len(s) == 0 and len(p) == 0:
        return True
    if len(s) == 0 or len(p) == 0:
        return False
    if s[0] == p[0]:
        return match(s[1:], p[1:])
    else:
        if p[0] != '?':
            return False
        else:
            return match(s[1:], p[1:]) or match(s, p[1:])


def match2(s: str, p: str) -> bool:
    '''(determine) FSM matching
    '''
    # step 1: build the FSM
    transition = {}
    state = 0
    final_states = []
    i = 0
    while i < len(p):
        ch = p[i]
        if ch != '?':
            transition[(state, ch)] = state + 1
            state += 1
            i += 1
        else:                    # ch == '?'
            if i != len(p) - 1:  # i is not the last index
                transition[(state, ch)] = state + 1
                pre_state = state
                state += 1
                i += 1
                ch = p[i]
                transition[(state, ch)] = state + 1
                transition[(pre_state, ch)] = state + 1
                state += 1
                i += 1
            else:
                transition[(state, ch)] = state + 1
                final_states.append(state)        # if ? is the last char, then there will be two final states
                state += 1
                i += 1
    final_states.append(state)
    # step 2: start running the FSM
    states = set([0])
    for ch in s:
        new_states = set()
        for state in states:
            for token in [ch, '?']:
                nxt_state = transition.get((state, token))
                if nxt_state:
                    new_states.add(nxt_state)
        states = new_states
    for final in final_states:
        if final in states:
            return True
    return False


def match3(s: str, p: str):
    '''dp matching
    '''
    m, n = len(s), len(p)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if s[i - 1] == p[j - 1]:
            #     dp[i][j] = dp[i - 1][j - 1]                  # match
            # if p[j - 1] == '?':
            #     dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1]  # match or skip
            dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1]        # simplify to only this line
    return True if dp[m][n] else False


def test1():
    s = 'microsoft'
    p = 'm?croso?ft'
    print('recursive:', match(s, p))
    print('FSM      :', match2(s, p))
    print('dp       :', match3(s, p))
    print('')


def test2():
    s = 'microsoft'
    p = 'm?croso?ft?'
    print('recursive (bug):', match(s, p))
    print('recursive (fix):', match(s+'1', p+'1'))
    print('FSM            :', match2(s, p))
    print('dp             :', match3(s, p))
    print('')

test1()
test2()
