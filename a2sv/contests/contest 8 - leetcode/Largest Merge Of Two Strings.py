class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        
        word1 = [char for char in word1]
        word2 = [char for char in word2]
        
        count1 = 0
        count2 = 0
        
        while count1 < len(word1) and count2 < len(word2):
            if word1[count1] > word2[count2]:
                merge.append(word1[count1])
                count1 += 1
            elif word2[count2] > word1[count1]:
                merge.append(word2[count2])
                count2 += 1
            else:
                if word2[count2:] > word1[count1:]:
                    merge.append(word2[count2])
                    count2 += 1
                
                elif word1[count1:] > word2[count2:]:
                    merge.append(word1[count1])
                    count1 += 1
                else:
                    merge.append(word1[count1])
                    count1 += 1
        
        if count1 == len(word1) and count2 < len(word2):
            for index in range(count2, len(word2)):
                merge.append(word2[index])
            return ''.join(merge)
        
        elif count2 == len(word2) and count1 < len(word1):
            for index in range(count1, len(word1)):
                merge.append(word1[index])
            return ''.join(merge)
        
        return ''.join(merge)