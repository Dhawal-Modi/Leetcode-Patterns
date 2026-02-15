class Solution:
    def loopExists(self, arr):
        # TODO: Write your code here
        for i in range(len(arr)):
            #is_forward = arr[i] >= 0
            if arr[i] >= 0:
                is_forward = True
            else:
                is_forward = False

            slow,fast = i,i

            while True:
                slow = self.movePointer(slow, is_forward, arr)
                fast = self.movePointer(fast, is_forward, arr)
                if fast != -1:
                    fast = self.movePointer(fast, is_forward, arr)

                #break if the direction of the movement changes or slow equals fast
                if fast == -1 or slow == -1 or slow == fast:
                    break

            if slow != -1 and slow == fast:
                return True

        return False

    def movePointer(self, current_index, is_forward, arr):

        #direction = arr[current_index] >= 0
        if arr[current_index] >= 0:
            direction = True
        else:
            direction = False

        if direction != is_forward:
            return -1

        next_index = (current_index + arr[current_index]) % len(arr)

        # This condition checks if the cycle only has one element, if it does then return -1 as we don't want one
        # element cycles
        if next_index == current_index:
            next_index = -1

        return next_index


def main():
    sol = Solution()
    print("Loop exists: " + str(sol.loopExists([1, 2, -1, 2, 2])))
    print("Loop exists: " + str(sol.loopExists([2, 1, -1, -2])))


main()
