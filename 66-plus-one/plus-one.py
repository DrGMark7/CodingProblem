class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        for i in digits:
            number += str(i)
        return [int(i) for i in str(int(number)+1)]