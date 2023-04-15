# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         if len(digits) == 1:
#             if digits[-1] == 9:
#                 digits = [1,0]
#                 return digits
#             else:
#                 digits[-1] += 1
#                 return digits
#         if len(digits) != 1:
#             if digits[-1] == 9:
#                 digits[-1] = 0
#                 digits[-2] += 1
#                 return digits
#             else:
#                 digits[-1] += 1
#                 return digits

nums = [0, 1, 0, 3, 12]
numbers = []
for i in nums:
    if nums == 1:
        print(nums)
    else:
        if nums[i+1] == 0:
            numbers.append(nums[i])
            nums.remove(0)
            b = len(numbers)
            while b >0:
                nums.append(0)
                b -= 1
            print(nums)