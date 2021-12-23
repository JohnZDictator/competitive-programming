class Solution:
    def reverseParentheses(self, s: str) -> str:
        reverse_str = ''
        output = []
        
        for x in s:
            if x == ')':
                while output[-1] != '(':
                    reverse_str += output.pop(-1)
                output.pop(-1)
                output += reverse_str
                reverse_str = ''
                continue
            output.append(x)
            
        return ''.join(str(x) for x in output)