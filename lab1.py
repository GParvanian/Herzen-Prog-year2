def add(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i]+nums[j] == target) and (j!=i):
                return i, j
            else:
                return "Подходящих пар нет"
