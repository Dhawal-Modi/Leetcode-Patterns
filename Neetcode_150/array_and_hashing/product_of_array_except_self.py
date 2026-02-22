from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix_prod = [1] * len(nums)
    for i in range(1,len(nums)):
        prefix_prod[i] = (prefix_prod[i - 1] * nums[i - 1])

    suffix_prod = [1] * len(nums)
    for j in range(len(nums) - 2, -1, -1):
        suffix_prod[j] = (suffix_prod[j + 1]  * nums[j + 1])

    return [a*b for a,b in zip(prefix_prod,suffix_prod)]


if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]))
    print(productExceptSelf([-1,1,0,-3,3]))