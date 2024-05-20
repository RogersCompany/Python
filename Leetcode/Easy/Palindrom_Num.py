class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        div = 1
        while x > 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div
            print (right)
            print (left)
            if left != right: return False
            x = (x - (x  // div) * div) // 10
            div = div // 100
        return True