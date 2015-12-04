def index_of_pupil(pupil, pupils):
    return pupils.find(pupil)


def index_of_pupils_in_group(group, pupils):
    result = []
    for pupil in group:
        result.append(pupils.find(pupil))
        pupils = pupils[pupils.find(pupil):]
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
