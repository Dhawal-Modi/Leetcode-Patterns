def merge(intervals):
    if len(intervals) < 2:
        return intervals

    if not intervals:
        return []

    # Sort the intervals by their starting times
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        # Check if there is an overlap
        if current[0] <= last_merged[1]:
            # Merge the intervals
            merged_intervals[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else:
            # No overlap, add the current interval to the merged list
            merged_intervals.append(current)

    return merged_intervals


if __name__ == "__main__":
    merge([[1, 4], [2, 6], [3, 5]])
