def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])

    #first_interval = intervals[0]
    count = 0
    last_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:
            count += 1
        else:
            last_end = intervals[i][1]
    return count


if __name__ == "__main__":
    print(eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(eraseOverlapIntervals([[1, 2], [2, 3]]))
