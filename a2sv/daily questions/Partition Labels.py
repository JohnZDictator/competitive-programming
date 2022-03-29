"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

 

Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.

"""

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        myDict = {}
        for index in range(len(s)):
            myDict[s[index]] = index
        
        minRange = 0
        maxRange = -1
        output = []
        for index in range(len(s)):
            if index == maxRange:
                output.append( index - minRange + 1 )
                minRange = index + 1
            
            if myDict[s[index]] > maxRange: 
                maxRange = myDict[s[index]]
                
                if index == maxRange:
                    output.append( index - minRange + 1)
                    minRange = index + 1
                    
        return output