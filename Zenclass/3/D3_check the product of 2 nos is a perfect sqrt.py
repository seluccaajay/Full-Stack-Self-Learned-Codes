## CHECK WHETHER PRODUCT OF TWO NUMBERS IS A PERFECT SQUARE NUMBERS
import math
N = int(input())
M = int(input())
product = N * M
root = math.sqrt(product)
if(int(root + 0.5) ** 2 == product):
  print("yes")
else:
  print("no")