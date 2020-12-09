def star_one():
    answer = None
    input = get_input_as_ints()

    set_of_things = set()
    for num in input:
        set_of_things.add(2020 - num)

    for num in input:
        if num in set_of_things:
            answer = num * (2020 - num)

    print(f'star one answer: {answer}')


def star_two():
    answer = None
    input = get_input_as_ints()

    for num in input:
        for num2 in input:
            for num3 in input:
                if (num + num2 + num3) == 2020:
                    answer = num * num2 * num3

    print(f'star two answer: {answer}')


def get_input_as_ints():
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
        return list(map(lambda l: int(l), lines))


if __name__ == '__main__':
    star_one()
    star_two()
