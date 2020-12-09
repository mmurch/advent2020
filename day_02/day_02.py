import re


def star_one():
    lines_parsed = []

    for line in (y for y in get_input_as_strings() if len(y) > 0):
        parsed = re.search("(\d+)-(\d+) (.): (.*)", line).groups()
        lines_parsed.append([int(parsed[0]), int(parsed[1]), parsed[2], parsed[3]])

    valid_count = 0
    for line in lines_parsed:
        letter_count = line[3].count(line[2])
        if line[0] <= letter_count <= line[1]:
            valid_count += 1

    print(f'star one answer: {valid_count}')


def star_two():
    answer = None

    input = get_input_as_strings()

    lines_parsed = []
    for line in (y for y in input if len(y) > 0):
        parsed = re.search("(\d+)-(\d+) (.): (.*)", line).groups()
        lines_parsed.append([int(parsed[0]), int(parsed[1]), parsed[2], parsed[3]])

    valid_count = 0
    for line in lines_parsed:
        num_match = 0
        if line[3][line[0]-1] == line[2]:
            num_match += 1

        if line[3][line[1]-1] == line[2]:
            num_match += 1

        if num_match == 1:
            valid_count += 1

    answer = valid_count

    print(f'star two answer: {answer}')


def get_input_as_strings():
    with open('input.txt', 'r') as fd:
        return fd.read().splitlines()


if __name__ == '__main__':
    star_one()
    star_two()
