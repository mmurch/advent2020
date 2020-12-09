from collections import deque


def star_one():
    deq = deque()
    for next_num in get_input_as_ints():
        if len(deq) < 25:
            deq.append(next_num)
            continue

        num_set = set(deq)
        if not any((next_num - num) in num_set for num in deq):
            print(f'star one answer: { next_num }')
            return

        deq.popleft()
        deq.append(next_num)


def star_two():
    magic_num = 25918798
    input = get_input_as_ints()
    for window in range(2, len(input)):
        deq = deque()
        running_sum = 0
        for next_num in input:
            deq.append(next_num)
            running_sum += next_num

            if len(deq) > window:
                running_sum -= deq.popleft()

            if running_sum == magic_num:
                print(f'star two answer: {max(deq) + min(deq)}')


def get_input_as_ints():
    with open('input.txt', 'r') as fd:
        lines = fd.read().splitlines()
        return list(map(lambda l: int(l), lines))


if __name__ == '__main__':
    star_one()
    star_two()
