import heapq
import copy

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    minHeap = []
    heapq.heapify(minHeap)

    max_size = 0
    for i in range(0, len(intervals)):
        heapq.heappush(minHeap, intervals[i])
        if intervals[i][0] >= minHeap[0][1]:
            heapq.heappop(minHeap)
        max_size = max(len(minHeap), max_size)
    return max_size


if __name__ == "__main__":
    print(minMeetingRooms([[4, 5], [2, 3], [2, 4], [3, 5]]))
