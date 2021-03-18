def get_interval_from_list(lst: list) -> list:
    return list(zip(lst[::2], lst[1::2]))


def get_joint_interval(t1: tuple, t2: tuple) -> tuple:
    start = t2[0] if t1[0] <= t2[0] else t1[0]
    end = t1[1] if t1[1] <= t2[1] else t2[1]
    return (start, end) if start < end else None


def get_all_joint_intervals(l1: list, l2: list) -> list:
    joint_intervals = []
    for i1 in l1:
        for i2 in l2:
            joint_interval = get_joint_interval(i1, i2)
            if joint_interval is not None:
                joint_intervals.append(joint_interval)
    return joint_intervals


def appearance(intervals: dict):
    lesson_intervals = get_interval_from_list(intervals['lesson'])
    pupil_intervals = get_interval_from_list(intervals['pupil'])
    tutor_intervals = get_interval_from_list(intervals['tutor'])

    joint_intervals = get_all_joint_intervals(lesson_intervals, pupil_intervals)
    joint_intervals = get_all_joint_intervals(joint_intervals, tutor_intervals)

    total_time = sum([i[1] - i[0] for i in joint_intervals])
    return total_time
