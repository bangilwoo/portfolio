from function import MyCircularDeque
from function import mergeKLists

mcd = MyCircularDeque.MyCircularDeque(3)
mkl = mergeKLists.Solution()

if __name__ == '__main__':
    print(mcd.insertLast(2))
    print(mcd.insertFront(1))
    print(mcd.deleteFront())
    print(mcd.deleteLast())

if __name__ == '__main__':
    print(mkl.mergeKLists(l1=[1,4,5], l2=[1,3,4], l3=[2,6]))
