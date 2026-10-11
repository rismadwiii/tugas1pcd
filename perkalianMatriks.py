A = [
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
]

B = [
    [[9, 10],
     [11, 12]],

    [[13, 14],
     [15, 16]]
]

# Menampilkan Matrix A
print("Matrix A:")
for i in range(2):
    print("Matrix ke-", i + 1)
    for j in range(2):
        print(A[i][j])

# Menampilkan Matrix B
print("\nMatrix B:")
for i in range(2):
    print("Matrix ke-", i + 1)
    for j in range(2):
        print(B[i][j])

# Proses perkalian Matrix
hasil = []
for i in range(2):
    matrix = []
    for j in range(2):
        baris = []
        for k in range(2):
            nilai = (
                A[i][j][0] * B[i][0][k]
                + A[i][j][1] * B[i][1][k]
            )
            baris.append(nilai)
        matrix.append(baris)
    hasil.append(matrix)

# Menampilkan hasil
print("\nHasil Perkalian Matrix A x B:")
for i in range(2):
    print("Matrix ke-", i + 1)
    for j in range(2):
        print(hasil[i][j])