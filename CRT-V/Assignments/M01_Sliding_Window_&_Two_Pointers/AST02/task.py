def Check_Palindrome(n: int,s:str) -> bool:
   left=0
   right=n-1
   while left<right:
      if s[left]!=s[right]:
         a = s[left + 1:right + 1]
         b = s[left:right]
         return a==a[::-1] or b==b[::-1]
      left+=1
      right-=1
   return True


if __name__ == '__main__':
   n = int(input())
   s = input()
   print(Check_Palindrome(n,s))
