class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        counter_x, counter_y = 0, 0 
        
        while counter_x < len(intervals):
            curr_lower_bound = intervals[counter_x][0]
            curr_upper_bound = intervals[counter_x][1]
            while counter_y < len(intervals):
                next_lower_bound = intervals[counter_y][0]
                next_upper_bound = intervals[counter_y][1]
                if counter_x == counter_y:              
                    counter_y += 1
                    continue
                elif curr_upper_bound >= next_lower_bound and curr_upper_bound <= next_upper_bound:
                    lower_bound = min(curr_lower_bound, next_lower_bound)
                    upper_bound = max(curr_upper_bound, next_upper_bound)
                    intervals[counter_x] = [lower_bound, upper_bound]
                    intervals.pop(counter_y)
                    counter_x -= 1
                    break
                counter_y += 1
            counter_y = 0
            counter_x += 1
        return intervals
    