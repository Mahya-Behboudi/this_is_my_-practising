# 
import random
from  chess_solution import has_clashes
def main():
    found_num = 0
    tries = 0
    while found_num < 10:
        l = list(range(8))
        random.shuffle(l)
        tries +=1
        if not has_clashes(l):
            print("found solution {0} in {1} tries".format(l,tries))
            tries = 0
            found_num +=1
main()
