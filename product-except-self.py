from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        answer = [1] * size

        # calculate the prefixes
        prefix = 1
        for i in range(size):
            answer[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(size - 1, -1, -1):
            answer[i] = answer[i] * postfix
            postfix = postfix * nums[i]

        return answer


s = Solution()
nums = [1, 2, 3, 4]
answer = s.productExceptSelf(nums)
print(answer)
# print(range(5))


# [6, 1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6]

# [5, 6, 1, 2, 3, 4]
# [4, 5, 6, 1, 2, 3]

# [5,30,30,60,,]  totals[i] = totals[i - 1] * nums[i - 1]
# [,,,,,]
