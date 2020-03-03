# https://leetcode.com/problems/queue-reconstruction-by-height/description/
# 406. Queue Reconstruction by Height
# Medium
#
# 2126
#
# 252
#
# Add to List
#
# Share
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
# Accepted
# 105,079
# Submissions
# 167,866


# %%
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # -a[1] for the last people to have a proper index (highest h, k=0)
        people.sort(key=lambda a: (a[0], -a[1]))
        res = [[]] * len(people)
        indices = list(range(len(people)))
        for j, (h, k) in enumerate(people):
            i = indices.pop(k)  # return k-th remaining position
            res[i] = people[j]
        return res


# %%
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
Solution().reconstructQueue(people)
