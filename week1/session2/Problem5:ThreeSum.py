# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


def three_sum(nums):
    if len(nums) < 3:
        return []
    if len(nums) == 3:
        return nums if nums[0] + nums[1] + nums[2] == 0 else []

    nums.sort()

    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            return res
        target = -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    return res


# Example Usage

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
print("---")
nums = [0, 1, 1]
print(three_sum(nums))
print("---")

nums = [0, 0, 0]
print(three_sum(nums))
# Example Output:

# [[-1, -1, 2], [-1, 0, 1]]
# []
# [[0, 0, 0]]
