# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Array import isPalindrome
from Array import reverseString
from Array import reorderLogFiles
from Array import mostCommonWord
from Array import groupAnagrams
from Array import longestPalindrome

ips = isPalindrome.Solution()
rss = reverseString.Solution()
rls = reorderLogFiles.Solution()
mcs = mostCommonWord.Solution()
gas = groupAnagrams.Solution()
lps = longestPalindrome.Solution()

if __name__ == '__main__':
    print(ips.isPalindrome1("A man, a plan, a canal: Panama"))

if __name__ == '__main__':
    print(rss.reverseString(["h", "e", "l", "l", "o"]))

if __name__ == '__main__':
    print(rls.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

if __name__ == '__main__':
    print('\n', mcs.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))

if __name__ == '__main__':
    print('\n', gas.groupAnagrams((["eat", "tea", "tan", "ate", "nat", "bat"])))

if __name__ == '__main__':
    print(lps.longestPalindrome("babad"))