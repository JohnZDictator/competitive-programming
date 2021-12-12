class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        temp = ''
        result = ''
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                words_index = int(words[i][-1])
                temp = words[i]
                words[i] = words[words_index - 1]
                words[words_index - 1] = temp
        for j in range(len(words)):
            result += words[j][:-1]
            if j < len(words) - 1:
                result += ' '
        return result