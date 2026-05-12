#1665. Minimum Initial Energy to Finish Tasks

# You are given an array tasks where tasks[i] = [actuali, minimumi]:

# actuali is the actual amount of energy you spend to finish the ith task.
# minimumi is the minimum amount of energy you require to begin the ith task.
# For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

# You can finish the tasks in any order you like.

# Return the minimum initial amount of energy you will need to finish all the tasks.

 

# Example 1:

# Input: tasks = [[1,2],[2,4],[4,8]]
# Output: 8
# Explanation:
# Starting with 8 energy, we finish the tasks in the following order:
#     - 3rd task. Now energy = 8 - 4 = 4.
#     - 2nd task. Now energy = 4 - 2 = 2.
#     - 1st task. Now energy = 2 - 1 = 1.
# Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.
# Example 2:

# Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
# Output: 32
# Explanation:
# Starting with 32 energy, we finish the tasks in the following order:
#     - 1st task. Now energy = 32 - 1 = 31.
#     - 2nd task. Now energy = 31 - 2 = 29.
#     - 3rd task. Now energy = 29 - 10 = 19.
#     - 4th task. Now energy = 19 - 10 = 9.
#     - 5th task. Now energy = 9 - 8 = 1.
# Example 3:

# Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
# Output: 27
# Explanation:
# Starting with 27 energy, we finish the tasks in the following order:
#     - 5th task. Now energy = 27 - 5 = 22.
#     - 2nd task. Now energy = 22 - 2 = 20.
#     - 3rd task. Now energy = 20 - 3 = 17.
#     - 1st task. Now energy = 17 - 1 = 16.
#     - 4th task. Now energy = 16 - 4 = 12.
#     - 6th task. Now energy = 12 - 6 = 6.
 

# Constraints:

# 1 <= tasks.length <= 105
# 1 <= actual​i <= minimumi <= 104

#Solution Approach:

# Problem Understanding

# You are given `n` tasks where each task is `[actual_i, minimum_i]`:
# - `actual_i` = energy consumed to complete the task
# - `minimum_i` = minimum energy you must **have before starting** the task

# Find the **minimum initial energy** needed so you can complete **all tasks** in some order.

# ---

# Approach — Greedy

# The key insight is: **in what order should we do the tasks?**

# We want to minimize "wasted" energy (the buffer we need to hold before starting). Consider two tasks A and B. We should do A before B if:

# > `min_A - actual_A < min_B - actual_B`

# i.e., sort tasks by **`minimum - actual`** (called the "buffer") in **descending order**. Tasks with larger buffers should come first because they demand more "slack" relative to what they consume.

# Once the optimal order is found, simulate backwards (or accumulate greedily) to find the minimum starting energy.

# ---

# Algorithm

# 1. Sort tasks by `(minimum - actual)` in **descending** order.
# 2. Initialize `answer = 0` and `current_energy = 0`.
# 3. Traverse tasks from last to first (backwards):
#    - At each task, the energy needed before this task is `max(current_energy + actual, minimum)`.
#    - Update `answer` by working backwards.
# 4. Alternatively, simulate forward: track how much energy you'd need at each step and propagate it backwards.

# A cleaner forward simulation:

# ```
# sort tasks by (min - actual) descending
# answer = 0, curr = 0
# for each task in sorted order:
#     if curr < task.minimum:
#         answer += task.minimum - curr
#         curr = task.minimum
#     curr -= task.actual
# return answer
# ```

# ---

#Code

# ```python
# class Solution:
#     def minimumEffort(self, tasks: list[list[int]]) -> int:
#         # Sort by buffer (minimum - actual) in descending order
#         tasks.sort(key=lambda t: t[1] - t[0], reverse=True)

#         answer = 0
#         curr = 0  # current energy we have

#         for actual, minimum in tasks:
#             if curr < minimum:
#                 # Top up energy to meet the minimum requirement
#                 answer += minimum - curr
#                 curr = minimum
#             # Spend energy on this task
#             curr -= actual

#         return answer
# ```

# ---

#Line-by-Line Explanation

# - `tasks.sort(key=lambda t: t[1] - t[0], reverse=True)`: Sort tasks so those needing the most "slack" (buffer = min − actual) go first.
# - `answer = 0, curr = 0`: `answer` accumulates the initial energy we need; `curr` tracks energy in hand.
# - `for actual, minimum in tasks`: Iterate in optimal order.
# - `if curr < minimum`: We don't have enough energy to even start this task.
# - `answer += minimum - curr`: Record the top-up needed, add it to total initial energy.
# - `curr = minimum`: Bring energy up to the threshold.
# - `curr -= actual`: Deduct the cost of completing the task.

# ---

# Dry Run

# Input: `tasks = [[1,2],[2,4],[4,8]]`

# Sorted by `(min - actual)` descending:
# - `[4, 8]` → buffer = 4
# - `[2, 4]` → buffer = 2
# - `[1, 2]` → buffer = 1

# | Step | Task (actual, min) | curr before | Top-up needed | curr after |
# |------|-------------------|-------------|---------------|------------|
# | 1 | (4, 8) | 0 | 8 → answer=8 | 8−4=4 |
# | 2 | (2, 4) | 4 | 0 (4 ≥ 4) | 4−2=2 |
# | 3 | (1, 2) | 2 | 0 (2 ≥ 2) | 2−1=1 |

# **Answer = 8** ✅

# Verify: Start with 8 → do [4,8]: 8≥8 ✓, left=4 → do [2,4]: 4≥4 ✓, left=2 → do [1,2]: 2≥2 ✓, left=1.

# ---

# Complexity

# - **Time:** `O(n log n)` — dominated by sorting
# - **Space:** `O(1)` — only a few variables (sorting is in-place)

# ---

#Why the Sort Key Works (Proof Sketch)

# Compare doing task A then B vs B then A, starting with energy `e`:

# - **A then B:** need `e ≥ min_A` and `e - actual_A ≥ min_B` → `e ≥ max(min_A, min_B + actual_A)`
# - **B then A:** need `e ≥ max(min_B, min_A + actual_B)`

# A before B is better when `min_B + actual_A ≤ min_A + actual_B`, i.e., `min_B - actual_B ≤ min_A - actual_A`, i.e., A has a **larger buffer** → confirms sorting by buffer descending.

# ---

# Edge Cases

# - **Single task:** `[actual, min]` → answer is `min` (need `min` energy before starting).
# - **All tasks have same buffer:** Order doesn't matter; still works correctly.
# - **actual == minimum:** Buffer is 0; these tasks go last.
# - **Large n (up to 10⁵):** `O(n log n)` handles comfortably.

class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # Sort by buffer (minimum - actual) in descending order
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)

        answer = 0
        curr = 0  # current energy we have

        for actual, minimum in tasks:
            if curr < minimum:
                # Top up energy to meet the minimum requirement
                answer += minimum - curr
                curr = minimum
            # Spend energy on this task
            curr -= actual

        return answer
    