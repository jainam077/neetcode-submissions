class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = {j: i for i, j in enumerate(nums)}
        return(index.get(target,-1))
