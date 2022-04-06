class Solution:
    memo = {}
    
    def findKthBit(self, n: int, k: int) -> str:
        
        def reverseBit(bit):
            reversedBits = []
            for index in range(len(bit) - 1, -1, -1):
                reversedBits.append(bit[index])
            
            return "".join(reversedBits)
        
        def invertBit(bit):
            invertedBits = ["0" for i in range(len(bit))]
            for index in range(len(bit)):
                if bit[index] == "0":
                    invertedBits[index] = "1"
                elif bit[index] == "1":
                    invertedBits[index] = "0"
            
            return "".join(invertedBits)
        
        def findNthBit(n):
            if n in self.memo:
                return self.memo[n]
        
            if n == 1:
                return "0"

            self.memo[n] = findNthBit(n-1) + "1" + reverseBit(invertBit(findNthBit(n-1))) 

            return self.memo[n]
        
        return findNthBit(n)[k-1]