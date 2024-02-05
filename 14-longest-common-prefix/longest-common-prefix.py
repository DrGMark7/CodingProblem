class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp,answer = [],""
        counter_index = 0

        if len(strs) == 1:
            return f"{strs[0]}"

        while True:
            temp = []
            for word in strs:
                try:
                    temp.append(word[counter_index])
                except IndexError:
                    return answer

            if len(set(temp)) == 1:
                answer += temp[0]
                counter_index += 1
            else:
                break
            #print(temp,counter_index)
        return answer
        