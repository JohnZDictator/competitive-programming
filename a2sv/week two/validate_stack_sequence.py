class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        my_stack = []
        counter = 0
        my_stack_counter = 0
        
        while my_stack_counter < len(pushed):
            if not my_stack:
                my_stack.append(pushed[my_stack_counter])
                my_stack_counter += 1
            if my_stack[-1] == popped[counter]:
                counter += 1
                my_stack.pop()
            else:
                my_stack.append(pushed[my_stack_counter])
                my_stack_counter += 1    
        while my_stack and my_stack[-1] == popped[counter]:
            counter += 1
            my_stack.pop()
        if len(my_stack) == 0:
            return True
        return False