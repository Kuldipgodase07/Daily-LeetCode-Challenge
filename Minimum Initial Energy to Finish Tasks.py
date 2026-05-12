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
    