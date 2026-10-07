"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        busy = []
        for i in intervals:
            for time in range(i.start,i.end):
                if time in busy:
                    return False
                busy.append(time)
        return True
                

