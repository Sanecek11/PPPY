
size = 9
for i in range(2, size + 1):
    for j in range(2, size + 1):
        res = i * j
        end = " " if j != size else ""
        print(f'{res:2}', end=end)
    print()
