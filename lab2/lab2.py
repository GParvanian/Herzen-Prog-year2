def add(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i]+nums[j] == target) and (j!=i):
                return [i, j]
    return "Подходящих пар нет"

print(add([2,7,11,15], 9))
