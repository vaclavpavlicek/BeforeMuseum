def index_of_pupil(pupil, pupils):
    return pupils.find(pupil)


def index_of_pupils_in_group(group, pupils):
    result = []
    for pupil in group:
        result.append(pupils.find(pupil))
        pupils = pupils[pupils.find(pupil):]
    return result
