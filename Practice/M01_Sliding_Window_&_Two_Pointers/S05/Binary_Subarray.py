'''
leetcode:- 1493

from typing import List
def longestSubarray(nums: List[int]) -> int:
        left=0
        count=0
        max_len=0
        for right in range(len(nums)):
            if nums[right]==0:
                count+=1
            while count>1:
                if nums[left]==0:
                    count-=1
                left+=1
            max_len=max(max_len,right-left)   
        return max_len
nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))


leetcode:- 1004

from typing import List
def longestOnes(nums: List[int], k: int) -> int:
        left=0
        count=0
        max_len=0
        for right in range(len(nums)):
            if nums[right]==0:
                count+=1
            while count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            max_len=max(max_len,right-left+1)   
        return max_len  
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3 
print(longestOnes(nums,k))


leetcode:- 930 and 1358
930:-

from typing import List
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
        def sub_arr(k):
            if k<0:
                return 0
            left=0
            count=0
            curr_sum=0
            for right in range(len(nums)):
                curr_sum+=nums[right] 
                while curr_sum>k:
                    curr_sum-=nums[left]
                    left+=1
                count+=(right-left+1)
            return count
        return sub_arr(goal)-sub_arr(goal-1)
nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums,goal))


1358:-
'''
from typing import List
def numberOfSubstrings(s: str) -> int:
        last_pos = {'a': -1, 'b': -1, 'c': -1}
        count = 0 
        for i, char in enumerate(s):
            last_pos[char] = i
            count += 1 + min(last_pos.values())
        return count
s = "abcabc"
print(numberOfSubstrings(s))
        