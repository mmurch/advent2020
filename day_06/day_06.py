def star_one():
    answer_sets = [set()]
    for line in get_input_as_strings():
        if line == '':
            answer_sets.append(set())
        else:
            for char in line:
                if char not in answer_sets[-1]:
                    answer_sets[-1].add(char)

    print(answer_sets)

    answer = sum(len(x) for x in answer_sets)

    print(f'star one answer: {answer}')


def star_two():
    answer_counts = [{}]
    group_counts = [0]

    for line in get_input_as_strings():
        if line == '':
            answer_counts.append({})
            group_counts.append(0)
        else:
            group_counts[-1] += 1
            for char in line:
                if char not in answer_counts[-1]:
                    answer_counts[-1][char] = 0
                answer_counts[-1][char] += 1

    count = 0
    for i in range(len(group_counts)):
        for k in answer_counts[i].keys():
            if answer_counts[i][k] == group_counts[i]:
                count += 1

    print(f'star two answer: {count}')


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
