def add (*args):
    all_number=[n for n in args]
    return sum(all_number)

print(add(3,5,1,2))
print(add(23,12,2))


def calculate(**kwargs):
