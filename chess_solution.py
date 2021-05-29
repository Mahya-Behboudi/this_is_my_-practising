from testing12 import test
def share_diagonal(x0,y0,x1,y1):
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    return dx==dy
# test(not share_diagonal(5,2,2,0))
# test(share_diagonal(5,2,3,0))
# test(share_diagonal(5,2,4,3))
# test(share_diagonal(5,2,4,1))

def col_clashes(bs,c):
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):           # Look at all columns to the left of c
            return True
    return False      
                                 # No clashes - col c has a safe placement.
test(not col_clashes([6,4,2,0,5], 4))
test(not col_clashes([6,4,2,0,5,7,1,3], 7))

# More test cases that should mostly clash
# test(col_clashes([0,1], 1))
# test(col_clashes([5,6], 1))
# test(col_clashes([6,5], 1))
# test(col_clashes([0,6,4,3], 3))
# test(col_clashes([5,0,7], 2))
# test(not col_clashes([2,0,1,3], 1))
# test(col_clashes([2,0,1,3], 2))

def has_clashes (permu_col):
    for i in range(1,len(permu_col)):
        if col_clashes(permu_col, i):
            return True
    return False
# test(not has_clashes([6,4,2,0,5,7,1,3])) # Solution from above
# test(has_clashes([4,6,2,0,5,7,1,3]))     # Swap rows of first two
# test(has_clashes([0,1,2,3]))             # Try small 4x4 board
# test(not has_clashes([2,0,3,1]))         # Solution to 4x4 case
def main():
    import random
    rng = random.Random()
    bd = list(range(8))
    mun_found = 0
    tries =0
    while mun_found <10:
        rng.shuffle(bd)
        tries += 1
        if not  has_clashes(bd):
            print("found solution {0} in {1} tries".format(bd,tries))
            tries =0
            mun_found +=1
main()
