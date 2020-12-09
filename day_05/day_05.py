def star_one():
    rows = get_input_as_strings()
    highest_id = 0
    for r in rows:
        r = r.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        id = int(r[:7], 2) * 8 + int(r[7:], 2)
        if id > highest_id:
            highest_id = id

    print(f'star one answer: {highest_id}')


def star_two():
    rows = get_input_as_strings()
    seats = set()

    for r in rows:
        r = r.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        seats.add(str(int(r[:7], 2)) + ':' + str(int(r[7:], 2)))

    missing = []
    for row in range(128):
        for col in range(8):
            seat_id = str(row) + ':' + str(col)
            surrounding_seats = [
                str(row + 1) + ':' + str(col),
                str(row - 1) + ':' + str(col),
                str(row) + ':' + str(col + 1),
                str(row) + ':' + str(col - 1)
            ]
            if seat_id not in seats and (surrounding_seats[0] in seats and
                                         surrounding_seats[1] in seats and
                                         surrounding_seats[2] in seats and
                                         surrounding_seats[3] in seats):
                missing.append(seat_id)

    print(f'star two answer: {missing}')


def get_input_as_strings():
    with open('input.txt', 'r') as fd:
        return fd.read().splitlines()


if __name__ == '__main__':
    star_one()
    star_two()
