import unittest

from leetcode._0005_longest_palindromic_substring import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertIn(Solution().longestPalindrome("babad"), ["bab", "aba"])
        self.assertIn(Solution().longestPalindrome("cbbd"), ["bb"])
        self.assertIn(Solution().longestPalindrome("a"), ["a"])
        self.assertIn(Solution().longestPalindrome("ac"), ["a"])
        self.assertIn(Solution().longestPalindrome2(
            "32101232100123210012321001232100123210012321001232100123210012321"
            "00123210012321001232100123210012321001232100123210012321001232100"
            "12321001232100123210012321001232100123210012321001232100123210012"
            "32100123210012321001232100123210012321001232100123210012321001232"
            "10012321001232100123210012321001232100123210012321001232100123210"
            "01232100123210012321001232100123210012321001232100123210012321001"
            "23210012321001232100123210012321001232100123210012321001232100123"
            "21001232100123210012321001232100123210012321001232100123210012321"
            "00123210012321001232100123210012321001232100123210012321001232100"
            "12321001232100123210012321001232100123210012321001232100123210012"
            "32100123210012321001232100123210012321001232100123210012321001232"
            "10012321001232100123210012321001232100123210012321001232100123210"
            "01232100123210012321001232100123210012321001232100123210012321001"
            "23210012321001232100123210012321001232100123210012321001232100123"
            "21001232100123210012321001232100123210012321001232100123210123210"
            "012321001232100123210123"),
            ["3210123210012321001232100123210012321001232100123210012321001232"
             "1001232100123210012321001232100123210012321001232100123210012321"
             "0012321001232100123210012321001232100123210012321001232100123210"
             "0123210012321001232100123210012321001232100123210012321001232100"
             "1232100123210012321001232100123210012321001232100123210012321001"
             "2321001232100123210012321001232100123210012321001232100123210012"
             "3210012321001232100123210012321001232100123210012321001232100123"
             "2100123210012321001232100123210012321001232100123210012321001232"
             "1001232100123210012321001232100123210012321001232100123210012321"
             "0012321001232100123210012321001232100123210012321001232100123210"
             "0123210012321001232100123210012321001232100123210012321001232100"
             "1232100123210012321001232100123210012321001232100123210012321001"
             "2321001232100123210012321001232100123210012321001232100123210012"
             "3210012321001232100123210012321001232100123210012321001232100123"
             "2100123210012321001232100123210012321001232100123210012321001232"
             "100123210123"])


if __name__ == '__main__':
    unittest.main()