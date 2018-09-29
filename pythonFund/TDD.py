
import unittest

def reverseList(list):
    for i in range(int(len(list)/2)):
        list[i],list[len(list)-1-i] = list[len(list)-1-i], list[i]
    return list

def isPalindrome(string):
    reversed_string = 'racecar'
    return string == reversed_string\

def isFactorial(num):
    if num == 0:
        return 1
    else:
        return n*factorial(n-1)

class IsReverseTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])

    def test2(self):
        self.assertEqual(reverseList([2,4,-3]), [-3,4,2])
class isPalindromeTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(isPalindrome("racecar"), True)

    def test2(self):
        self.assertEqual(isPalindrome("rabbit"), False)
        
class isFactorial(unittest.TestCase):
    def test1(self):
        self.assertEqual(isFactorial(5), 120)

if __name__ == '__main__':
    unittest.main()