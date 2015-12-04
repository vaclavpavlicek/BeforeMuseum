def index_of_pupil(pupil, pupils):
    return pupils.find(pupil)


def index_of_pupils_in_group(group, pupils):
    result = []
    for pupil in group:
        result.append(pupils.find(pupil))
        pupils = pupils[pupils.find(pupil):]
    return result


def test_read_group_from_input_file(path_to_input_file):
    input_file = open(path_to_input_file)
    for x in range(0, 2):
        group = input_file.readline()
    return group
