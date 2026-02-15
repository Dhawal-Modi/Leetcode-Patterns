from heapq import *


def findmaxcpuload(jobs):
    jobs.sort(key=lambda x: x[0])
    max_cpu_load = 0
    current_cpu_load = 0
    minheap = []

    for i in range(0, len(jobs)):
        while len(minheap) > 0 and jobs[i][0] >= minheap[0][1]:
            current_cpu_load -= minheap[0][2]
            heappop(minheap)

        heappush(minheap, jobs[i])
        current_cpu_load += jobs[i][2]

        if current_cpu_load > max_cpu_load:
            max_cpu_load = current_cpu_load

    return max_cpu_load


if __name__ == "__main__":
    print(findmaxcpuload([[1, 4, 3], [2, 5, 4], [7, 9, 6]]))
    print(findmaxcpuload([[6, 7, 10], [2, 4, 11], [8, 12, 15]]))
    print(findmaxcpuload([[1, 4, 2], [2, 4, 1], [3, 6, 5]]))
