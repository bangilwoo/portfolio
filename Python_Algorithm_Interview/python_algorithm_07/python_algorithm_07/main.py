# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Array import TwoSum
from Array import Trap
from Array import ThreeSum
from Array import ArrayPairSum
from Array import ProductExceptSelf
from Array import MaxProfit

tss = TwoSum.Solution()
trs = Trap.Solution()
ths = ThreeSum.Solution()
aps = ArrayPairSum.Solution()
pes = ProductExceptSelf.Solution()
mps = MaxProfit.Solution()

if __name__ == '__main__':
  print(tss.twoSum1([2, 7, 11, 15], 9)) # Question 7
  print(trs.trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) # Question 8
  print(ths.threeSum1([-1, 0, 1, 2, -1, -4])) # Question 9
  print(aps.arrayPairSum1([1, 4, 3, 2])) # Question 10
  print(pes.productExceptSelf([1, 2, 3, 4])) # Question 11
  print(mps.maxProfit1([7, 1, 5, 3, 6, 4])) # Question 12
