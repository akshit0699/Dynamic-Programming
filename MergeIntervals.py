class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0: return []
        intervals.sort()
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        intervals.pop(0)
        
        for x in intervals:
            if x[0]>end:
                res.append([start, end])
                start = x[0]
            if x[1]>end:
                end = x[1]
                
        res.append([start, end])
        return res
