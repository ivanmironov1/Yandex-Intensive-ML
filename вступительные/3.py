n, x, y = map(int, input().split())


count = 0
for i in range(1, n):
    len_i = len(str(i))
    count_i = 0
    for j in str(i):
        if int(j) in [x, y]:
            count_i += 1
    if count_i == len_i:
        count += 1
print(count)