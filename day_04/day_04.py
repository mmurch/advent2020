import re


def star_one():
    input_as_strings = get_input_as_strings()
    passports = parse_passports(input_as_strings)
    answer = sum(1 for p in passports if ('byr' in p.keys() and
                                          'iyr' in p.keys() and
                                          'eyr' in p.keys() and
                                          'hgt' in p.keys() and
                                          'hcl' in p.keys() and
                                          'ecl' in p.keys() and
                                          'pid' in p.keys()))

    print(f'star one answer: {answer}')


def star_two():
    input_as_strings = get_input_as_strings()
    passports = parse_passports(input_as_strings)

    answer = list(p for p in passports if (
        'byr' in p.keys() and
        'iyr' in p.keys() and
        'eyr' in p.keys() and
        'hgt' in p.keys() and
        'hcl' in p.keys() and
        'ecl' in p.keys() and
        'pid' in p.keys()) and (
        is_valid_byr(p['byr']) and
        is_valid_iyr(p['iyr']) and
        is_valid_eyr(p['eyr']) and
        is_valid_hgt(p['hgt']) and
        is_valid_hcl(p['hcl']) and
        is_valid_ecl(p['ecl']) and
        is_valid_pid(p['pid'])))
    print(f'star two passports: {answer}')
    print(f'star two answer: {len(answer)}')


def parse_passports(lines):
    # first flatten lines
    flattened = []
    current_line = []
    for l in lines:
        if l == '':
            flattened.append(current_line)
            current_line = []
        else:
            splt = l.split(' ')
            for item in splt:
                current_line.append(item)

    if len(current_line) > 0:
        print('hit end cleanup')
        flattened.append(current_line)

    passports = []
    for flt in flattened:
        dict = {}
        for kvp in flt:
            kvp_splt = kvp.split(':')
            dict[kvp_splt[0]] = kvp_splt[1]
        passports.append(dict)
    return passports


def is_valid_byr(byr):
    try:
        return 1920 <= int(byr) <= 2002
    except Exception as ex:
        return False


def is_valid_iyr(iyr):
    try:
        return 2010 <= int(iyr) <= 2020
    except Exception as ex:
        return False


def is_valid_eyr(eyr):
    try:
        return 2020 <= int(eyr) <= 2030
    except Exception as ex:
        return False


def is_valid_hgt(hgt):
    try:
        inch_index = hgt.find('in')
        cm_index = hgt.find('cm')

        if inch_index == -1 and cm_index == -1:
            return False

        if inch_index > -1:
            num = int(hgt[:inch_index])
            return 59 <= num <= 76
        if cm_index > -1:
            num = int(hgt[:cm_index])
            return 150 <= num <= 193
    except Exception as ex:
        return False


def is_valid_hcl(hcl):
    try:
        pattern = re.compile('^#(?:[0-9a-f]{6})$')
        return pattern.match(hcl)
    except Exception as ex:
        return False


def is_valid_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_pid(pid):
    try:
        int(pid)
        return len(pid) == 9
    except Exception as ex:
        return False


valid_fns = {
    'byr': is_valid_byr,
    'iyr': is_valid_iyr,
    'eyr': is_valid_eyr,
    'hgt': is_valid_hgt,
    'hcl': is_valid_hcl,
    'ecl': is_valid_ecl,
    'pid': is_valid_pid
}


def get_input_as_strings():
    with open('input.txt', 'r') as fd:
        return fd.read().splitlines()


if __name__ == '__main__':
    star_one()
    star_two()
