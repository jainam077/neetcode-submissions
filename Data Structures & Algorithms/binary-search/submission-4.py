class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def split(arr, target):
            temp = []
            mid = int(len(arr)//2)

            if target not in arr:
                return -1

            elif target < arr[mid]:
                temp = arr[0:mid]
                return split(temp, target)

            elif target > arr[mid]:
                temp = arr[mid:]
                return split(temp, target)

            elif target == arr[mid]:
                return nums.index(target)

            
        return split(nums, target)
