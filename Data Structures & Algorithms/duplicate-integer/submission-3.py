class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        v = False

        for i in nums:
            if i in seen:
                v = True
                break
            else:
                seen.append(i)
        return v

        