def reverseString(s):
  left = 0
  right = - 1
  while left + 1 == - right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -=1

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -=1

