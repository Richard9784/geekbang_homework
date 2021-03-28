class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        
        # 记录任务出现的次数
        task_map = dict()
        for task in tasks:
            if task not in task_map:
                task_map[task] = 1
            else:
                task_map[task] += 1
  
        max_task_count = max(task_map.values())
        res = (max_task_count - 1) *(n+1)

        for sort in (task_map.values()):
            if sort == max_task_count:
                res += 1
        return res if res >= length else length

if __name__ == "__main__":
    test = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(test.leastInterval(task,n))