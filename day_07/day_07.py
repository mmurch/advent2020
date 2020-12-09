import re


def star_one():
    lookup = {}
    for line in (y for y in get_input_as_strings() if len(y) > 0):
        container_bag = re.search("(^.*?) bags", line).groups()[0]
        contained_bags = re.findall("(\d+) (.+?) bag", line)

        for bag_type in contained_bags:
            if bag_type[1] not in lookup.keys():
                lookup[bag_type[1]] = set()
            lookup[bag_type[1]].add(container_bag)

    parent_bags = set()
    working_bags = []
    working_bags.extend(lookup['shiny gold'])
    while len(working_bags) > 0:
        for bag in working_bags:
            working_bags.remove(bag)
            parent_bags.add(bag)
            if bag in lookup.keys():
                for new_parent in lookup[bag]:
                    working_bags.append(new_parent)

    print(f'star one answer: {len(parent_bags)}')


def star_two():
    lookup = {}
    for line in (y for y in get_input_as_strings() if len(y) > 0):
        container_bag = re.search("(^.*?) bags", line).groups()[0]
        contained_bags = re.findall("(\d+) (.+?) bag", line)
        lookup[container_bag] = contained_bags

    bag_count = -1
    working_bags = ['shiny gold']
    while len(working_bags) > 0:
        bags_to_add = []
        for bag in working_bags:
            working_bags.remove(bag)
            bag_count += 1
            for child_bag in lookup[bag]:
                for i in range(int(child_bag[0])):
                    bags_to_add.append(child_bag[1])
        working_bags.extend(bags_to_add)

    print(f'star two answer: {bag_count}')


def get_input_as_strings():
    with open('input.txt', 'r') as fd:
        return fd.read().splitlines()


if __name__ == '__main__':
    star_one()
    star_two()
