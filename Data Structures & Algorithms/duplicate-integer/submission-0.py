class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = set()
        res = False
        for i  in nums:
            if i not in h:
                h.add(i)
            else:
                res = True
                break

        return res


    