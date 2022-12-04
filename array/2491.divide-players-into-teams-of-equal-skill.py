''' 

You are given a positive integer array skill of even length n where skill[i] denotes 
the skill of the ith player. Divide the players into n / 2 teams of size 2 such that 
the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to 
divide the players into teams such that the total skill of each team is equal.

'''


class Solution:
    '''solution during the contest 322, a little bit complicated
    '''
    def dividePlayers(self, skill: List[int]) -> int:
        summ = sum(skill)
        teams = len(skill) // 2
        if summ % teams != 0:
            return -1
        team_sum = summ // teams
        skill = Counter(skill)
        ans = 0
        keys = set(skill.keys())
        while len(keys) > 0:
            a = keys.pop()
            b = team_sum - a
            if a == b:
                if skill[a] % 2 == 1:
                    return -1
                else:
                    num_team = skill[a] // 2
                    ans += a * a * num_team
            else:
                if skill[a] != skill[b]:
                    return -1
                else:
                    ans += a * b * skill[a]
                    keys.remove(b)
        return ans



class Solution:
    '''sorting and two pointers, the key is to pair the smallest to the largest
    '''
    def dividePlayers(self, skill: List[int]) -> int:
        summ = sum(skill)
        num_teams = len(skill) // 2
        if summ % num_teams != 0:
            return -1

        team_sum = summ // num_teams
        skill.sort()
        i = 0
        j = len(skill) - 1
        ans = 0
        while i < j:
            if skill[i] + skill[j] != team_sum:
                return -1
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans