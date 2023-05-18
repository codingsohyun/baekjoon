array = []

for i in range(9):
    dwarf = int(input())
    array.append(dwarf)

total = sum(array)

for i in range(8):
    for j in range(i+1, 9):
        if (array[i]+array[j] == total-100):
            save = [i,j]
            break

del array[save[0]]
del array[save[1]-1]

array.sort()

for i in array:
    print(i)
