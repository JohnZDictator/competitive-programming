class Solution:
    def calculate(self, s: str) -> int:
        counter = 1
 
        arr = self.oprArr(s)
        output = [int(arr[0])]
    

        while len(output) < 3 and counter < len(arr):
            if arr[counter] == '*':
                output[0] = int(output[0]) * int(arr[counter+1])
            elif arr[counter] == '/':
                output[0] = int(output[0]) // int(arr[counter+1])
            else:
                output.append(arr[counter])
                output.append(int(arr[counter+1]))
            counter += 2
            
        while counter < len(arr):
            if arr[counter] == '*':
                output[2] = output[2] * int(arr[counter+1])
            elif arr[counter] == '/':
                output[2] = output[2] // int(arr[counter+1])
            elif output[1] == '+':
                output[0] = output[0] + output[2]
                output[1] = arr[counter]
                output[2] = int(arr[counter+1])
            elif output[1] == '-':
                output[0] = output[0] - output[2]
                output[1] = arr[counter]
                output[2] = int(arr[counter+1])
            counter += 2
        if len(output) == 3:
            if output[1] == '+':
                return output[0] + output[2]
            elif output[1] == '-':
                return output[0] - output[2]
            elif output[1] == '*':
                return output[0] * output[2]
            elif output[1] == '/':
                return output[0] // output[2]
        
        
        return output[0]
    
    def oprArr(self, s):
        oprStr = ''
        operations = ['*', '/', '+', '-']
        arr = []
        for c in s:
            if c not in operations:
                oprStr += c
            else:
                arr.append(int(oprStr))
                arr.append(c)
                oprStr = ''
        arr.append(oprStr)
        return arr