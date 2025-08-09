def diamond_pattern(n):
    mid = n // 2
    for i in range(1,mid+1):
        print(f"{' ' * (mid-i)}{'*'*(2*i-1)}")
    for j in range(mid, 0, -1):
        print(f"{' '* (mid-j)}{'*'*(2*j-1)}")

diamond_pattern(11)