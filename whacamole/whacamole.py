# from https://leetcode.com/discuss/interview-question/350139/google-phone-screen-whac-a-mole

def whack(holes, w):
    n = len(holes)
    if w >= n: return sum(holes)
    i, j = 0, w - 1
    tot = 0
    cumu = sum(holes[0:w])
    while j < n:
        cumu += (holes[j] - holes[i])
        tot = max(cumu, tot)
        i += 1
        j += 1
    return tot