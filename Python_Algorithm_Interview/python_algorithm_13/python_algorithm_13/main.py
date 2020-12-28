# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from function import networkDelayTime
from function import findCheapestPrice

ndt = networkDelayTime.Solution()
fcp = findCheapestPrice.Solution()

if __name__ == '__main__':
    print(ndt.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], N=4, K=2))
    print((fcp.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0)))