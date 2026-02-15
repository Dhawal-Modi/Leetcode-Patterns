from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


class Solution:
    def findEmployeeFreeTime(self, schedule):
        result = []
        minheap = []

        for i in range(len(schedule)):
            heappush(minheap, EmployeeInterval())
        return result
