def main(nums: list[int]) -> bool:
    # nums_dict = {}
    #
    # for i in nums:
    #     if not i in nums_dict:
    #         nums_dict[i] = 0
    #     nums_dict[i] += 1
    #
    # for k in nums_dict:
    #     if nums_dict[k] >= 2:
    #         return True
    # return False

    num_seen = set()

    for i in nums:
        if i in num_seen:
            return True
        num_seen.add(i)
    return False

if __name__ == "__main__":
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]

    print(main(nums1))
    print(main(nums2))
    print(main(nums3))