class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        extend_list = nums.copy()
        counter = 0

        for i in extend_list:
            if i == val:
                nums.remove(i)
                #nums.append("_")
            else:
                counter += 1

        return counter

                