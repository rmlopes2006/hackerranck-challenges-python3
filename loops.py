n = int(input())
my_list = []

while n >= 0:
    my_list.append(n)
    n -= 1

my_list.reverse()
my_list.pop()

for number in my_list:
    print(number ** 2)

# Test
print(my_list)
print(type(my_list))

