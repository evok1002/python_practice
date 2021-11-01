def minor (m, i, j):
    m = [row[:j]+row[j+1:] for row in (m[:i]+m[i+1:])]
    return m
def det(m):
    if len(m) == 2:
        return (m[0][0]*m[1][1]-m[0][1]*m[1][0])
    d = 0
    for i in range(n):
        d+=((-1)**i)*m[0][i]*det(minor(m, 0, i))
    return d

n = int(input ('Input the number of the rows and columns: '))
matrix = []
for i in range(n):
    r = input('Input {0} elements of the {1} row (example - 1, 2, 3, 4): '.format(n,i+1))
    arr=r.split(', ')
    for k in range(n):
        arr[k]=int(arr[k])
    matrix.append(arr)
print('Your matrix:\n',matrix)
print('Determinant of your matrix: {0}'.format(det(matrix)))
    




