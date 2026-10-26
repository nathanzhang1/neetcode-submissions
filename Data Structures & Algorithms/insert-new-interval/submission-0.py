class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        i = 0
        new_start, new_end = newInterval[0], newInterval[1]
        merged = False

        out = []
        if not intervals:
            return [newInterval]

        if new_end < intervals[0][0]:
            out.append(newInterval)
            merged = True

        while i < len(intervals):
            i_start, i_end = intervals[i][0], intervals[i][1]

            if i_end < new_start:
                out.append(intervals[i])
                i += 1
            elif i_end >= new_start and i_start <= new_end:
                merged_start = min(i_start, new_start)
                merged_end = max(i_end, new_end)
                while i_end >= new_start and i_start <= new_end:
                    merged_end = max(i_end, new_end)
                    i += 1
                    if i >= len(intervals):
                        break
                    i_start, i_end = intervals[i][0], intervals[i][1]
                out.append([merged_start, merged_end])
                merged = True
            elif i_start > new_end:
                if not merged:
                    out.append(newInterval)
                    merged = True
                out.append(intervals[i])
                i += 1
 
        if not merged:
            out.append(newInterval)
        
        return out

# Iterate through intervals using pointer
    # Find starting point of new merged interval then ending point
    # If i[end] < new[start] (interval completely before new interval)
        # Add i to out
        # Shift i
    # If i[end] >= new[start] and i[start] <= new[end] (any interval overlapping with new interval)
        # merged[start] = min(i[start], new[start])
        # While there is still overlap and there is still next interval
            # Shift i
        # merged[end] = max(i[end], new[end])
        # Add merged to out
    # If i[start] > new[end] (interval completely after new interval)
        # Add i to out
        # Shift i