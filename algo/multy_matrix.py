def multiply(matrix1, matrix2):
    result = []
    for k in matrix1:
        b = []
        for i in zip(*matrix2):
            res = sum([a*b for a,b in zip(k, i)])
            b.append(res)
        result.append(b)

    return result

#example
m1 = [[1, 2, 3],
      [3, 1, 1],
      [3, 4, 3]
      ]

m2 = [[4, 2, 2, 4, 8],
      [3, 1, 4, 3, 5],
      [1, 5, 6, 9, 7]
      ]

m3 = multiply(m1, m2)

for item in m3:
    print(item)

#>>>[12, 14, 22, 28, 32]
#>>>[16, 12, 16, 24, 36]
#>>>[27, 25, 40, 51, 65]







