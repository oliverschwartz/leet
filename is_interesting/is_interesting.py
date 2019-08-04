# from https://leetcode.com/discuss/interview-question/350312/google-onsite-interesting-string

def is_interesting(s):
    n = len(s)
    if n == 0: return False
    i = -1
    adv = 0
    while True:

        # move through str
        while adv > 0 and i < n:
            i += 1
            adv -= 1
        
        # adv was too high, we overshot
        if i >= n:
            return False

        # we hit it spot on
        elif adv == 0 and i == n - 1:
            return True

        # need to go to nextr str
        elif adv == 0:
            i += 1
            if not s[i].isdigit():
                return False
            adv = int(s[i])
