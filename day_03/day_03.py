def star_one():
    answer = trees_for_slope(get_input_as_strings(), 3, 1)
    print(f'star one answer: {answer}')


def star_two():
    answer = (trees_for_slope(get_input_as_strings(), 1, 1) *
              trees_for_slope(get_input_as_strings(), 3, 1) *
              trees_for_slope(get_input_as_strings(), 5, 1) *
              trees_for_slope(get_input_as_strings(), 7, 1) *
              trees_for_slope(get_input_as_strings(), 1, 2))
    print(f'star two answer: {answer}')


def trees_for_slope(grid, slope_x, slope_y):
    visited = []
    x = 0
    y = 0

    while y < len(grid):
        visited.append(grid[y][x])
        x += slope_x
        x %= len(grid[0])
        y += slope_y

    return sum(1 for loc in visited if loc == '#')


def get_input_as_strings():
    with open('input.txt', 'r') as fd:
        return fd.read().splitlines()


if __name__ == '__main__':
    star_one()
    star_two()
