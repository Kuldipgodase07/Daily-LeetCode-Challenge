
# ## Problem Understanding

# **2496. Check if Array Is Good**

# You are given an integer array `nums`. The array is called **"good"** if it is a permutation of the array `base[n]`, defined as:

# ```
# base[n] = [1, 2, 3, ..., n-1, n, n]
# ```

# That is, `base[n]` contains integers `1` through `n-1` exactly once, and `n` appears **exactly twice**.

# Return `True` if `nums` is good, otherwise `False`.

# **Example:**
# ```
# nums = [2, 1, 3, 3] → True   (base[3] = [1, 2, 3, 3])
# nums = [1, 3, 3, 2] → True   (same elements, order doesn't matter)
# nums = [1, 1]       → True   (base[1] = [1, 1])
# nums = [3, 4, 4, 1, 2] → False (n=4, but 3 appears once, not matching base[4])
# ```

# ---

# ## Approach

# The key insight: if `nums` is good with parameter `n`, then:
# - `n = max(nums)`
# - `n` must appear **exactly twice**
# - Every integer from `1` to `n-1` must appear **exactly once**

# Use a **frequency counter (hash map)**. Count occurrences, then validate these two rules.

# ---

# ## Algorithm

# 1. Compute `n = max(nums)`.
# 2. Count frequency of each element using `Counter`.
# 3. Check that `n` appears exactly **2** times.
# 4. Check that every integer `1` through `n-1` appears exactly **1** time.
# 5. Also verify `len(nums) == n + 1` (total elements = n-1 ones + 2 n's = n+1).

# ---

# ## Code

# ```python
# from collections import Counter

# class Solution:
#     def isGood(self, nums: list[int]) -> bool:
#         n = max(nums)
#         freq = Counter(nums)

#         if len(nums) != n + 1:
#             return False

#         if freq[n] != 2:
#             return False

#         for i in range(1, n):
#             if freq[i] != 1:
#                 return False

#         return True
# ```

# ---

# ## Line-by-Line Explanation

# - `n = max(nums)`: The largest value is the `n` of `base[n]`.
# - `freq = Counter(nums)`: Builds a frequency map in O(n) time.
# - `if len(nums) != n + 1`: Quick length check — `base[n]` has exactly `n+1` elements. Catches impossible cases early.
# - `if freq[n] != 2`: `n` must appear exactly twice.
# - `for i in range(1, n)`: Check each value from 1 to n-1.
# - `if freq[i] != 1`: Each must appear exactly once; any deviation → not good.
# - `return True`: All checks passed.

# ---

# ## Dry Run

# **Input:** `nums = [2, 1, 3, 3]`

# | Step | Operation | Value |
# |------|-----------|-------|
# | `n = max(nums)` | max is 3 | `n = 3` |
# | `len(nums)` | 4 == n+1 = 4 ✅ | pass |
# | `freq[3]` | 2 ✅ | pass |
# | `freq[1]` | 1 ✅ | pass |
# | `freq[2]` | 1 ✅ | pass |
# | **Result** | All checks pass | `True` |

# **Input:** `nums = [3, 4, 4, 1, 2]`

# | Step | Operation | Value |
# |------|-----------|-------|
# | `n = max(nums)` | max is 4 | `n = 4` |
# | `len(nums)` | 5 == n+1 = 5 ✅ | pass |
# | `freq[4]` | 2 ✅ | pass |
# | `freq[1]` | 1 ✅ | pass |
# | `freq[2]` | 1 ✅ | pass |
# | `freq[3]` | 1 ✅ | pass |
# | **Result** | All checks pass | `True` ← Wait... |

# Hmm, actually `[3,4,4,1,2]` **is** good (`base[4] = [1,2,3,4,4]`)! LeetCode's example `[3,4,4,1,2]` returns `True`. Let's check a false one:

# **Input:** `nums = [1, 2, 3, 4]`

# | Step | Operation | Value |
# |------|-----------|-------|
# | `n = 4` | — | — |
# | `len(nums)` | 4 ≠ 5 ❌ | **False** |

# ---

# ## Complexity

# - **Time:** `O(n)` — one pass for `Counter`, one pass for validation (1 to n-1).
# - **Space:** `O(n)` — for the frequency map.

# ---

# ## Edge Cases

# | Case | Behavior |
# |------|----------|
# | `[1, 1]` | `n=1`, len=2=n+1 ✅, `freq[1]=2` ✅ → `True` |
# | `[1, 2]` | `n=2`, len=2≠3 → `False` |
# | All same elements `[3,3,3]` | `n=3`, `freq[1]` missing → `False` |
# | `[1]` | `n=1`, len=1≠2 → `False` |
# | Large `n` with a gap | Some `freq[i]` = 0 → `False` |

# The length check is a powerful early filter — it eliminates most invalid inputs instantly without needing to scan the full frequency map.


from collections import Counter

class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = max(nums)
        freq = Counter(nums)

        if len(nums) != n + 1:
            return False

        if freq[n] != 2:
            return False

        for i in range(1, n):
            if freq[i] != 1:
                return False

        return True