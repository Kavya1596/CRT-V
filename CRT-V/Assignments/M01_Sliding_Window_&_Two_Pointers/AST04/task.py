def pairInSortedRotated(arr, target):  
   n = len(arr)
   small = 0
   for i in range(n):
        if arr[i] < arr[small]:
            small = i
   big = (small - 1 + n) % n

   while small != big:
        total = arr[small] + arr[big]

        if total == target:
            return True

        if total < target:
            small = (small + 1) % n
        else:
            big = (big - 1 + n) % n

   return False


if __name__ == '__main__':
   arr = list(map(int,input().split()))
   target = int(input())
   print(pairInSortedRotated(arr,target))
