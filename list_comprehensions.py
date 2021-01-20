"""
x, y, z, n - serão entradas do usuário (int)
(i, j, k) são coordenadas 3D e (i + j + k != n)
0 <= i <= x
0 <= j <= y
0 <= k <= z
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

lista_x = range(x + 1)
lista_y = range(y + 1)
lista_z = range(z + 1)

l = [[x, y, z] for x in lista_x for y in lista_y for z in lista_z if x + y + z != n]
print(l)

# lista = [x for x in range(10)]
# print(lista)
#
# lista_1 = [[x, y] for x in range(4) for y in range(3)]
# print(lista_1)
#
# resultado = []
# for x in [1, 2, 3]:
#     for y in [4, 5, 6]:
#         resultado.append([x, y])
#
# print(resultado)
