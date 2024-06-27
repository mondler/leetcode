class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        """
        Counts the number of days without meetings.

        Args:
            days (int): Total number of days.
            meetings (list[list[int]]): List of meeting intervals.

        Returns:
            int: Number of days without meetings.
        """
        # Sort the meetings by start time
        meetings.sort(key=lambda x: x[0])

        days_meeting = 0  # Count of days with meetings

        # Iterate over meetings except the last one
        for i in range(len(meetings) - 1):
            current_start, current_end = meetings[i]
            next_start, next_end = meetings[i + 1]

            # If the next meeting doesn't overlap with the current one
            if next_start > current_end:
                # Add the duration of the current meeting to days_meeting
                days_meeting += current_end - current_start + 1
            else:
                # Merge the current and next meetings if they overlap
                meetings[i + 1] = [current_start, max(current_end, next_end)]

        # Add the duration of the last meeting to days_meeting
        days_meeting += meetings[-1][1] - meetings[-1][0] + 1

        # Return the number of days without meetings
        return days - days_meeting


days = 10
meetings = [[5, 7], [1, 3], [9, 10]]

print(Solution().countDays(days, meetings))

days = 5
meetings = [[2, 4], [1, 3]]

print(Solution().countDays(days, meetings))

days = 6
meetings = [[1, 6]]

print(Solution().countDays(days, meetings))
