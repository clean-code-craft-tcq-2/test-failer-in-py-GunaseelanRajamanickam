
def size(cms):
    try:
        if cms >= 34 and cms < 38:
            return 'S'
        elif cms >= 38 and cms < 42:
            return 'M'
        elif cms >=42 and cms < 44:
            return 'L'
        else:
            return 'Not a Valid tshirt size'
    except TypeError:
        print("TypeError: Check size entered")


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
assert(size(38) == 'M')
assert(size(42) == 'L')
assert(size(0) == 'Not a Valid tshirt size')
assert(size(-20) == 'Not a Valid tshirt size')
print("All is well (maybe!)\n")
