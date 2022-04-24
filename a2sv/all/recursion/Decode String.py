class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                char_arr = []
                while stack and not stack[-1].isdigit():
                    char_arr.append(stack.pop())
                
                repeat_term = ""
                while stack and stack[-1].isdigit():
                    repeat_term = stack.pop() + repeat_term
                
                repeat_term = int(repeat_term) if repeat_term else 1
                str_char = ""
                for index in range(len(char_arr)-1, -1, -1):
                    if char_arr[index] != '[' and char_arr[index] != ']':
                        str_char += char_arr[index]
                
                str_char = repeat_term * str_char
                stack.append(str_char)
            
            else:
                stack.append(char)

        return "".join(stack)