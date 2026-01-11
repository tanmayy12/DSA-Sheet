class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        # Step 2: Merge overlapping intervals
        for i in range(1, len(intervals)):
            last = result[-1]
            curr = intervals[i]

            if curr[0] <= last[1]:  # Overlap
                last[1] = max(last[1], curr[1])
            else:
                result.append(curr)

        return result
