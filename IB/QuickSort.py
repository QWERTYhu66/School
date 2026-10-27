def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    newlist = []
    pivot = nums[0]
    nums.pop(0)

    for i in nums[:]:
        if i <= pivot:
            newlist.append(i)
            nums.remove(i)

    return quick_sort(newlist) + [pivot] + quick_sort(nums)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))