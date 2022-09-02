class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        prev = [-1, -1]
        for interval in intervals:
            if interval[0] < prev[1]:
                return False
            prev = interval
        return True