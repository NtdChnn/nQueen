import timeit
start = timeit.default_timer()

from itertools import permutations

N = 12

def print_table():
    for row in range(N):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(N):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= N-1 and x+m <= N-1:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= N-1:
                table[y-m][x+m] = 1
            if y+m <= N-1 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False

table = [[0]*N for _ in range(N)]
numList = []
for i in range(0,N):
    numList.append(i)
perms = permutations(numList)


num_comb = 0
for perm in perms:
    for i in range(0,N):
        if put_queen(perm[i], i):
            if i == N-1:
                print_table()
                num_comb += 1
                print(f"solution{num_comb}")
                print(" ")
        else:
            break
    table = [[0] * N for _ in range(N)]

stop = timeit.default_timer()
print('Time: ', stop - start)
