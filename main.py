def star_one():
    print(f'star one answer: { "shrug" }')


def star_two():
    print(f'star two answer: { "shrug" }')


def get_input_as_strings():
    with open('input.txt', 'r') as fd:
        return fd.read().splitlines()


def get_input_as_ints():
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
        return list(map(lambda l: int(l), lines))


if __name__ == '__main__':
    star_one()
    star_two()
