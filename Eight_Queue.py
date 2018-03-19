__metaclass__=type;
def conflict(state, nextX):
    nextY = len(state);
    for i in range(nextY):
        # 如果在统一水平线上或者对角线上(垂直距离相等)
        if abs(state[i] - nextX) in (0, nextY-i):
            return True;
    return False;
