class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        timestamps = []

        for start, end in intervals:
            timestamps.append((start, 1))
            timestamps.append((end, -1))
        
        timestamps.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        cur_start = timestamps[0][0]
        output = []

        for time, state in timestamps:
            count += state

            if state == 1 and count == 1:
                cur_start = time
            elif count == 0:
                output.append([cur_start, time])
        
        return output