N = 5

array = []
for i in range(N):
    x = int(input())
    if x < 100:
        if x % 10 == 0:
            array.append(x)
            continue
        else:
            continue

#print(array)

total = 0
for i in range(N):
    total += array[i]

s_array = sorted(array)

avg = total // N
print(avg)
print(s_array[2])


