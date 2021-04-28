def solve(entry_value):
    final_list = []
    words_list = entry_value.split()

    # print(words_list)
    for word in words_list:
        capitalized_word = word.capitalize()
        final_list.append(capitalized_word)

    # print(type(final_list))
    capitalized_name = ' '.join(final_list)
    final_name = str(capitalized_name)

    return capitalized_name


solve("rodrigo martins lopes")
