'''
leetcode:- 74

#Flatten a matrix

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
arr=[]
for row in matrix:
    arr+=row
print(arr)


#Traditional Approach

from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        arr=[]
        for row in matrix:
            arr+=row
        n=len(arr)
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if target==arr[mid]:
                return True
            elif target<arr[mid]:
                right=mid-1
            else:
                left=mid+1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))


#Optimal Approach

from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left,right=0,m*n-1
        while left<=right:
            mid=(left+right)//2
            row,col=mid//n,mid%n
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                right=mid-1
            else:
                left=mid+1
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))



leetcode:- 240

from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        r=0
        c=n-1 
        while r<m and c>=0:
            val=matrix[r][c]
            if val==target:
                return True
            elif val<target:
                r+=1
            else:
                c-=1
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(searchMatrix(matrix,target))



leetcode:- 378
'''
from typing import List
def kthSmallest( matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        def countLessOrEqual(target):
            count = 0
            row = n - 1
            col = 0       
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row + 1  
                    col += 1
                else:
                    row -= 1
            return count
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                high = mid - 1  
            else:
                low = mid + 1                 
        return ans
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix,k))