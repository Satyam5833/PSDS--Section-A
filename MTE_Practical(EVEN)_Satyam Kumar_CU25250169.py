def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))

        arr.sort(key=lambda num: (bin(num ^ x).count('1'), num))

        print(*arr)

solve()
