class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        task_queue = []
        counter = 0
        multiplier = 0
        
        while max(task_freq.values()) > 0:
            for x in enumerate(task_freq.most_common()):
                if task_freq[x[1][0]] == 0:
                    continue
                elif counter < n+1:
                    if x[1][0] not in task_queue:
                        task_queue.append(x[1][0])
                        task_freq[x[1][0]] -= 1
                        counter += 1
                    else:
                        task_queue.append('idle')
                        counter += 1
                else:
                    task_queue = []
                    counter = 0
                    multiplier += 1
                    break
                        
        return multiplier * (n+1) + len(task_queue)