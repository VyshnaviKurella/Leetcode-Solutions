class Solution:
    def reverse(self, x: int) -> int:
      x= str(x)
      x=x[::-1]
      if x[-1] =="-":
          x= int("-"+x[0:-1])
      else:
          x= int(x)
      if x > pow(2,31) or x<pow(-2,31):
          return 0
    #   print(type(x))
      return x