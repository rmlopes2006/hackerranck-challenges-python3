"""
Lists
Consider a list (list = []). You can perform the following commands:

1. insert i e : Insert integer e at position i.
2. print: Print the list.
3. remove e : Delete the first occurrence of integer e.
4. append e : Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop : Pop the last element from the list.
7. reverse : Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will
be of the 7 types listed above. Iterate through each command in order and perform the corresponding
operation on your list.
"""

n = int(input())

my_list = [0, 1, 2, 3]

while n > 0:
    print('Você agora pode digitar {} comandos.'.format(n))
    print('Entre com um comando válido:')
    user_input = str(input())

    # print
    if user_input == 'print':
        print(my_list)
        n -= 1
    # reverse
    elif user_input == 'reverse':
        my_list.reverse()
        print(my_list)
        n -= 1
    # sort
    elif user_input == 'sort':
        my_list.sort()
        print(my_list)
        n -= 1
    # pop
    elif user_input == 'pop':
        my_list.pop()
        print(my_list)
        n -= 1
    # remove
    elif user_input.startswith('remove'):
        user_input_string_list = user_input.split(' ')
        # print(user_input_string_list, type(user_input_string_list), type(user_input_string_list[-1]))
        user_input_string_list[-1] = int(user_input_string_list[-1])
        # print(type(user_input_string_list[-1]))
        if user_input_string_list[-1] in my_list:
            my_list.remove(user_input_string_list[-1])
            print(my_list)
            n -= 1
        else:
            print('Você deve informar um elemento que esteja na lista.')
    # append
    elif user_input.startswith('append'):
        user_input_string_list = user_input.split(' ')
        user_input_string_list[-1] = int(user_input_string_list[-1])

        my_list.append(user_input_string_list[-1])
        print(my_list)
        n -= 1
    # insert
    elif user_input.startswith('insert'):
        user_input_string_list = user_input.split(' ')
        print(user_input_string_list)

        user_input_string_list[-2] = int(user_input_string_list[-2])
        user_input_string_list[-1] = int(user_input_string_list[-1])
        my_list.insert(user_input_string_list[-2], user_input_string_list[-1])
        print(my_list)

        n -= 1
    else:
        print('Você precisa digitar um comando válido.')






