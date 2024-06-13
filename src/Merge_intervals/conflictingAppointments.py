def canAttendAllAppointments(intervals):
    intervals.sort(key=lambda x: x[0])

    first_interval = intervals[0]

    for current in intervals[1:]:
        a_overlaps_b = current[0] < first_interval[0] < current[1]
        b_overlaps_a = first_interval[0] < current[0] < first_interval[1]

        if a_overlaps_b or b_overlaps_a:
            #first_interval = current
            return False
        first_interval = current
    return True


if __name__ == "__main__":
    print(canAttendAllAppointments([[6, 7], [2, 4], [8, 12]]))
    print(canAttendAllAppointments([[4, 5], [2, 3], [3, 6]]))
    print(canAttendAllAppointments([[1, 4], [2, 5], [7, 9]]))
