import copy


def star_one():
    code = []
    for line in get_input_as_strings():
        splt = line.split(' ')
        code.append([splt[0], int(splt[1])])

    acc = get_acc(code, set(), 0, 0)[0]

    print(f'star one answer: {acc}')


def star_two():
    code = []
    for line in get_input_as_strings():
        splt = line.split(' ')
        code.append([splt[0], int(splt[1])])

    for i in range(len(code)):
        code_copy = copy.deepcopy(code)
        if code_copy[i][0] == 'jmp':
            code_copy[i][0] = 'nop'
        elif code_copy[i][0] == 'nop':
            code_copy[i][0] = 'jmp'

        acc_state = get_acc(code_copy, set(), 0, 0)
        if acc_state[1] == 'terminated':
            print(f'star two answer: {acc_state[0]}')


def get_acc(code, visited, acc, step):
    if step in visited:
        return acc, 'loop'

    visited.add(step)
    next_step = step + 1

    if code[step][0] == 'acc':
        acc += code[step][1]
    elif code[step][0] == 'jmp':
        next_step = step + code[step][1]

    if next_step == len(code):
        return acc, 'terminated'

    return get_acc(code, visited, acc, next_step)


def get_input_as_strings():
    with open('input.txt', 'r') as fd:
        return fd.read().splitlines()


if __name__ == '__main__':
    star_one()
    star_two()
