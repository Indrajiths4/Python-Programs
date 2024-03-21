def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the elements of the matrix row-wise (separate numbers by spaces):")
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transposed_matrix = transpose(matrix)
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
