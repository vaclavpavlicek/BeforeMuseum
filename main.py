def index_of_pupils_in_group(group, all_pupils):
    result = []
    size_of_all_pupils = len(all_pupils)
    for pupil in group:
        result.append(all_pupils.find(pupil) + size_of_all_pupils - len(all_pupils) + 1)
        all_pupils = all_pupils[all_pupils.find(pupil):]
    return result


def read_group_from_input_file(path_to_input_file):
    input_file = open(path_to_input_file)
    group = read_line_from_input_file(input_file, 2)
    group = group[:group.find('\n')]
    return group


def read_all_pupils_from_input_file(path_to_input_file):
    input_file = open(path_to_input_file)
    group = read_line_from_input_file(input_file, 3)
    return group


def read_line_from_input_file(input_file, line_number):
    line = ''
    for x in range(0, line_number):
        line = input_file.readline()
    return line


def find_group_of_pupils(input_file):
    group = read_group_from_input_file(input_file)
    all_pupils = read_all_pupils_from_input_file(input_file)
    indexes_of_pupils_in_group = index_of_pupils_in_group(group, all_pupils)
    return indexes_of_pupils_in_group


def generate_output_file(indexes_of_pupils_in_group):
    indexes_of_pupils_in_group = map(str, indexes_of_pupils_in_group)
    result = ' '.join(indexes_of_pupils_in_group)
    output_file = open('output.txt', 'w')
    output_file.write(result)
    return result

if __name__ == '__main__':
    generate_output_file('in')
