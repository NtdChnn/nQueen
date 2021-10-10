import timeit
start = timeit.default_timer()

N = 12  # N x N Board
numSol = 0  			# number of solutions

b = N*[-1]  			# indices = rows, b[index] = coloumn, first init to -1
colFree = N*[1] 			# all N col are free at first
upFree = (2*N - 1)*[1] 		# all up diagonals are free at first
downFree = (2*N - 1)*[1]    		# all down diagonals are free at first

def printBoard(b):
    print(b)

def putQueen(r, b, colFree, upFree, downFree):
    global N
    global numSol
    for c in range(N): # ใล่ใส่ไปทีละ column ทุก col.
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: #ใส่ได้?
            b[r] = c    # ใส่ ที่ r, c

            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 # เปลี่ยน data struct ไม่ให้ใส่แนวนี้

            if r == N-1:       # ถ้าใส่ควีนครบแล้ว
                printBoard(b)  #print(b)
                numSol += 1
            else:
                putQueen(r+1, b, colFree, upFree, downFree)  # ใส่ควีนแถวถัดไป
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 #เอา Queen ออกเพื่อให้ได้ solution อื่น
                                                             # หรือ เพราะ queen ตัวนี้แม้ใส่ได้แต่ไม่ทำให้เกิด solution
putQueen(0, b, colFree, upFree, downFree)   #  first add at 1st  (ie. row 0)
print('number of solutions = ', numSol)

stop = timeit.default_timer()
print('Time: ', stop - start)