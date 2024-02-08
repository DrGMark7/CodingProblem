class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        class_word = []

        for word in strs:
            key_check = sorted(list(word))
            if key_check not in [i[0] for i in class_word]:
                temp = [
                    key_check,[]
                ]
                class_word.append(temp)

        for word in strs:
            check_word = sorted(list(word))
            check_list = [w[0] for w in class_word]

            if check_word in check_list:
                class_word[check_list.index(check_word)][-1].append(word)

        for item in class_word:
            answer.append(item[-1])

        return sorted(answer,key=lambda x:len(x))