import sys
sys.stdin=open("../input.txt", "r")

n, m = map(int, input().split())
ch = [0]*(n+1)
res = [0]*n
cnt = 0
def DFS(L):
    global cnt
    if L == m :
        for i in range(m):
            print(res[i], end = ' ')
        print()
        cnt += 1
    else :
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0

DFS(0)
print(cnt)