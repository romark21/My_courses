# a = [[1, 2, 4, 5, 6], [4, 5, 1, 6]]
# b = []
#
# for i in a:
#     for j in i:
#
#         if [i][j] == 2:
#             b = [i, - 1][j] + [i, 1][j]
#             print(b, end=' ')

a = [[1, 2, 4, 5, 6],
     [4, 5, 1, 6, 3]]

print(len(a))
print(len(a[0]))
print(a[-1])

b = []

for i in range(len(a)-1):
    for j in range(len(a[i])-1):
        b = a[(i+1) % len(a)][j] + a[i-1][j] + a[i][j-1] + a[i][(j+1) % len(a[0])]

        print(b, end=' ')
    print(a[-1][-1] + a[1][-1] + a[0][-2] + a[0][1])
    [print(' '.join(map(str, row))) for row in b]
    print()

for i in range(len(a)):
    for j in range(len(a[i])-1):
        print(a[i][j])
        # b = a[i + 1][j] + a[i - 1][j] + a[i][j - 1] + a[i][j + 1]



    #     print(b, end=' ')
    # print()



string = m = []
while string != 'end':
    string = input()
    m.append(list(map(int, string.split(' ')))) if string != 'end' else None
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1) % li][j], m[i][j-1], m[i][(j+1) % lj]]) for j in range(lj)] for i in range(li)]
[print(' '.join(map(str, row))) for row in new]
