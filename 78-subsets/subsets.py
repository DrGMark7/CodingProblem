from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        for i in range(len(nums)+1):
            comb = list(combinations(tuple(nums),i))
            for j in comb:
                answer.append(list(j))

        return answer 