s = 0
l = 0
for i in range(1, 6):
    for j in range(1, i + 1):
        l += 1
        s += i + j
print(s, l)
