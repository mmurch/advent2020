def star_one():
    sorted_input = get_input_as_ints()
    sorted_input.sort()

    # jolt diff of 3 starts with a bonus to account for the final hop
    diffs = [0, 0, 0, 1]

    # handle first hop
    diffs[sorted_input[0]] += 1

    for i in range(1, len(sorted_input)):
        diffs[sorted_input[i] - sorted_input[i - 1]] += 1

    print(f'star one answer: {diffs[1] * diffs[3]}')


def star_two():
    sorted_input = get_input_as_ints()
    sorted_input.sort()
    sorted_input.insert(0, 0)

    seq_counts = {0: 1}
    for adapter in sorted_input:
        for next_adapter in list(filter(lambda j: adapter < j <= (adapter + 3), sorted_input)):
            if next_adapter not in seq_counts.keys():
                seq_counts[next_adapter] = 0
            seq_counts[next_adapter] += seq_counts[adapter]

    print(f'star two answer: {seq_counts[sorted_input[-1]]}')


def get_input_as_ints():
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
        return list(map(lambda l: int(l), lines))


if __name__ == '__main__':
    star_one()
    star_two()
