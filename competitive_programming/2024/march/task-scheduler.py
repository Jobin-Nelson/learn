"""
Created Date: 2024-03-19
Qn: You are given an array of CPU tasks, each represented by letters A to Z,
    and a cooling time, n. Each cycle or interval allows the completion of one
    task. Tasks can be completed in any order, but there's a constraint: identical
    tasks must be separated by at least n intervals due to cooling time.

    Return the minimum number of intervals required to complete all tasks.
Link: https://leetcode.com/problems/task-scheduler/
Notes:
    - fill in idle slots
"""
def leastInterval(tasks: list[str], n: int) -> int:
    counter = [0] * 26
    max_val = 0
    max_count = 0
    for task in tasks:
        id = ord(task) - ord('A')
        counter[id] += 1
        if max_val == counter[id]:
            max_count += 1
        elif max_val < counter[id]:
            max_val = counter[id]
            max_count = 1

    part_count = max_val - 1
    part_length = n - (max_count - 1)
    empty_slots = part_count * part_length
    available_tasks = len(tasks) - max_val * max_count
    idles = max(0, empty_slots - available_tasks)

    return len(tasks) + idles

if __name__ == '__main__':
    t1, n1 = ["A","A","A","B","B","B"], 2
    t2, n2 = ["A","C","A","B","D","B"], 1
    t3, n3 = ["A","A","A", "B","B","B"], 3

    print(leastInterval(t1, n1))
    print(leastInterval(t2, n2))
    print(leastInterval(t3, n3))
