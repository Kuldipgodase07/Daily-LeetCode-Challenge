# Problem 1674. Minimum Moves to Make Array Complementary:

# You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

# The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

# Return the minimum number of moves required to make nums complementary.

 

# Example 1:

# Input: nums = [1,2,4,3], limit = 4
# Output: 1
# Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined elements are changed).
# nums[0] + nums[3] = 1 + 3 = 4.
# nums[1] + nums[2] = 2 + 2 = 4.
# nums[2] + nums[1] = 2 + 2 = 4.
# nums[3] + nums[0] = 3 + 1 = 4.
# Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
# Example 2:

# Input: nums = [1,2,2,1], limit = 2
# Output: 2
# Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot change any number to 3 since 3 > limit.
# Example 3:

# Input: nums = [1,2,1,2], limit = 2
# Output: 0
# Explanation: nums is already complementary.
 

# Constraints:

# n == nums.length
# 2 <= n <= 105
# 1 <= nums[i] <= limit <= 105
# n is even.

# Solution Approach:

# ## Problem Understanding

# **1674. Minimum Moves to Make Array Complementary**

# You're given an integer array `nums` of **even length** `n` and an integer `limit`. Each element satisfies `1 <= nums[i] <= limit`.

# In one move, you can **replace any element** with any integer in `[1, limit]`.

# A pair `(nums[i], nums[n-1-i])` is **complementary** if their sum equals the same target `T` for all pairs simultaneously.

# **Goal:** Return the minimum number of moves to make all pairs complementary (i.e., all pairs sum to the same value `T`).

# ---

# ## Approach

# The key insight: we need to find the best target sum `T` (ranging from `2` to `2*limit`) that requires the **fewest replacements** across all pairs.

# For each pair `(a, b)` where `a = nums[i]`, `b = nums[n-1-i]`:

# - **0 moves needed** if `a + b == T` already
# - **1 move needed** if `T` is in range `[min(a,b)+1, max(a,b)+limit]` (one element can reach T)
# - **2 moves needed** otherwise (T is outside reach, need to replace both)

# Instead of checking every T from 2 to 2\*limit for every pair (O(n \* limit)), we use a **difference array** (sweep line) to accumulate the cost savings efficiently in O(n + limit).

# ---

# ## Algorithm

# 1. Initialize a difference array `delta` of size `2*limit + 2`, all zeros. Start with a baseline of `2*n` moves (worst case: replace both elements in every pair).
# 2. For each pair `(a, b)`:
#    - Over range `[2, 2*limit]`, the default cost is **2**.
#    - Over `[min(a,b)+1, max(a,b)+limit]`, cost drops to **1** → mark `-1` at start, `+1` after end.
#    - At exactly `a+b`, cost drops to **0** → mark `-1` at `a+b`, `+1` at `a+b+1`.
# 3. Do a prefix sum over `delta` to get actual cost adjustments per T.
# 4. Return the minimum total cost across all T values.

# ---

# ## Code

# ```python
# class Solution:
#     def minMoves(self, nums: list[int], limit: int) -> int:
#         n = len(nums)
#         # delta[t] stores the change in total moves at sum = t
#         delta = [0] * (2 * limit + 2)

#         for i in range(n // 2):
#             a, b = nums[i], nums[n - 1 - i]
#             lo, hi = min(a, b), max(a, b)

#             # For T in [lo+1, hi+limit]: need 1 move (reduce from 2 to 1)
#             delta[lo + 1] -= 1
#             delta[hi + limit + 1] += 1

#             # For T == a+b: need 0 moves (reduce from 1 to 0)
#             delta[a + b] -= 1
#             delta[a + b + 1] += 1

#         # Base cost: 2 moves per pair
#         total_moves = 2 * (n // 2)
#         ans = total_moves
#         cur = total_moves

#         for t in range(2, 2 * limit + 1):
#             cur += delta[t]
#             ans = min(ans, cur)

#         return ans
# ```

# ---

# ## Line-by-Line Explanation

# - `delta = [0] * (2 * limit + 2)`: Difference array indexed by possible sum T (from 2 to 2\*limit).
# - `for i in range(n // 2)`: Process each symmetric pair.
# - `a, b = nums[i], nums[n-1-i]`: Get the pair.
# - `lo, hi = min(a, b), max(a, b)`: For clean range math.
# - `delta[lo+1] -= 1` / `delta[hi+limit+1] += 1`: For T in `[lo+1, hi+limit]`, only 1 move needed instead of 2 → save 1.
# - `delta[a+b] -= 1` / `delta[a+b+1] += 1`: For T == `a+b`, 0 moves needed → save 1 more.
# - `total_moves = 2 * (n // 2)`: Worst-case baseline (replace both in every pair).
# - Prefix sum loop: accumulate delta to get actual cost at each T, track minimum.

# ---

# ## Dry Run

# **Input:** `nums = [1, 2, 4, 3]`, `limit = 4`

# Pairs: `(nums[0], nums[3]) = (1, 3)` and `(nums[1], nums[2]) = (2, 4)`

# **Pair (1, 3):** lo=1, hi=3
# - 1 move range: T ∈ [2, 7] → `delta[2]-=1`, `delta[8]+=1`
# - 0 move at T=4 → `delta[4]-=1`, `delta[5]+=1`

# **Pair (2, 4):** lo=2, hi=4
# - 1 move range: T ∈ [3, 8] → `delta[3]-=1`, `delta[9]+=1`
# - 0 move at T=6 → `delta[6]-=1`, `delta[7]+=1`

# **delta:** index: `[0,0,−1,−1,−1,+1,−1,+1,+1,+1]`

# Baseline = 4 (2 pairs × 2 moves)

# | T | delta[T] | cur | ans |
# |---|----------|-----|-----|
# | 2 | −1 | 3 | 3 |
# | 3 | −1 | 2 | 2 |
# | 4 | −1 | 1 | 1 |
# | 5 | +1 | 2 | 1 |
# | 6 | −1 | 1 | 1 |
# | 7 | +1 | 2 | 1 |
# | 8 | +1 | 3 | 1 |

# **Answer: 1** ✅ (change `nums[1]` from 2 to 1, making all pairs sum to 4)

# ---

# ## Complexity

# - **Time:** `O(n + limit)` — one pass over pairs + one prefix sum sweep
# - **Space:** `O(limit)` — for the delta array

# This is optimal compared to the brute-force `O(n * limit)`.

# ---

# ## Edge Cases

# - **All pairs already complementary:** delta collapses to 0 at that T → answer is 0.
# - **n = 2 (single pair):** Works correctly, only one pair to process.
# - **limit = 1:** All elements must be 1, target T = 2, cost is 0 if all are already 1.
# - **a == b:** lo == hi, range becomes `[lo+1, lo+limit]`, still valid.

# ---

# **Pattern recognized:** Difference array / sweep line — a powerful trick whenever you need to efficiently apply range updates and then find a global minimum/maximum. 

class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        # delta[t] stores the change in total moves at sum = t
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo, hi = min(a, b), max(a, b)

            # For T in [lo+1, hi+limit]: need 1 move (reduce from 2 to 1)
            delta[lo + 1] -= 1
            delta[hi + limit + 1] += 1

            # For T == a+b: need 0 moves (reduce from 1 to 0)
            delta[a + b] -= 1
            delta[a + b + 1] += 1

        # Base cost: 2 moves per pair
        total_moves = 2 * (n // 2)
        ans = total_moves
        cur = total_moves

        for t in range(2, 2 * limit + 1):
            cur += delta[t]
            ans = min(ans, cur)

        return ans