def get_intervals_from_list(lst: list) -> list:
    return list(zip(lst[::2], lst[1::2]))


def get_joint_interval(t1: tuple, t2: tuple) -> tuple:
    start = max(t1[0], t2[0])
    end = min(t1[1], t2[1])
    return (start, end) if start <= end else None


def get_all_joint_intervals(l1: list, l2: list) -> list:
    joint_intervals = []
    for i1 in l1:
        for i2 in l2:
            joint_interval = get_joint_interval(i1, i2)
            if joint_interval:
                joint_intervals.append(joint_interval)
    return joint_intervals


def get_total_crossing_time(lst: list) -> int:
    lst.sort()
    prev = lst[0]
    total_time = 0
    for curr in lst[1:]:
        if prev[1] > curr[0]:
            prev = [prev[0], max(prev[1], curr[1])]
        else:
            total_time += prev[1] - prev[0]
            prev = curr
    total_time += prev[1] - prev[0]
    return total_time


def appearance(data: dict) -> int:
    joint_intervals = get_intervals_from_list(data['lesson'])
    for intervals in (data['pupil'], data['tutor']):
        intervals = get_intervals_from_list(intervals)
        joint_intervals = get_all_joint_intervals(joint_intervals, intervals)

    return get_total_crossing_time(joint_intervals)
