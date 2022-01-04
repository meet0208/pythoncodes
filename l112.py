def is_sort_list(nums):
    result = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
    return result

nums1 = [1,2,4,6,8,10,12,14,16,17]

print(is_sort_list(nums1))

nums2 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]

print(is_sort_list(nums2))

#or
def sort_list(nums):
    if sorted(nums)==nums:
        return True
    else:
        return False

print(sort_list(nums1))
print(sort_list(nums2))
