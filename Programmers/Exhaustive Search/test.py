lim = 100
n = 5

def search(chosen, curr, cnt):
    if (cnt == n):
        for i in search:
            print(i)
    
    for i in range(curr + 1, lim + 1):
        chosen[cnt] = i

        search(chosen, curr, cnt + 1)

def main():
    chosen = []
    
    search(chosen, 0, 0)