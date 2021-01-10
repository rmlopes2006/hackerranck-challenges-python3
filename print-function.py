n = int(input())

my_list = []
string = ''

while n > 0:
    my_list.append(n)
    n -= 1

my_list.reverse()

for item in my_list:
    item = str(item)
    print(type(item), item)
    string += item

# test
print(my_list)
# for item in list:
#     print(type(item), item)
print(string)
