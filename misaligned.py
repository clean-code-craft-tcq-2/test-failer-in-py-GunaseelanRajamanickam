printed_list = []

def print_color_map(formatString, printOnConsole):
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            formatted_string = formatString((i * 5 + j), major, minor)
            printOnConsole(formatted_string)
    return len(major_colors) * len(minor_colors)

def printOnConsole(formatted_string):
  print(formatted_string)

def formatString(index, major, minor):
    if index > 9:
        formatted_string = f'{index} | {major} | {minor}'
    else:
        formatted_string = f'{index}  | {major} | {minor}'
    return formatted_string

def printOnConsole_stub(formatted_string):
    printed_list.append(formatted_string)
    return None

def formatString_stub(index, major, minor):
    if index > 9:
        formatted_string = f'{index} | {major} | {minor}'
    else:
        formatted_string = f'{index}  | {major} | {minor}'
    return formatted_string


result = print_color_map(formatString_stub, printOnConsole_stub)
assert(result == 25)
test_string_first = printed_list[0]
test_string_last = printed_list[-1]
assert(test_string_first.find('|') == test_string_last.find('|'))
assert(printed_list[9].find('|') == printed_list[10].find('|'))
assert(printed_list[10].find('|') == printed_list[11].find('|'))
assert(len(test_string_first.split(' | ')[0]) == len(test_string_last.split(' | ')[0]))
print("All is well (maybe!)\n")
