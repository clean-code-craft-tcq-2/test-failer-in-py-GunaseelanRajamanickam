printed_list = []

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            if i * 5 + j > 9:
                print(f'{i * 5 + j} | {major} | {minor}')
                printed_list.append(f'{i * 5 + j} | {major} | {minor}')
            else:
                print(f'{i * 5 + j}  | {major} | {minor}')
                printed_list.append(f'{i * 5 + j}  | {major} | {minor}')
    return len(major_colors) * len(minor_colors), printed_list


result, printed_list = print_color_map()
assert(result == 25)
test_string_first = printed_list[0]
test_string_last = printed_list[-1]
assert(test_string_first.find('|') == test_string_last.find('|'))
assert(len(test_string_first.split(' | ')[0]) == len(test_string_last.split(' | ')[0]))
print("All is well (maybe!)\n")
