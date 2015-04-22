import unittest
from rob import Code
import random

__author__ = 'phchang'


class TestCode(unittest.TestCase):

    def setUp(self):
        self.code = Code()
        self.test_sum = 0

    def recursive(self, nums , idx):
        if idx < 0:
            return 0
        else:
            pre = self.recursive(nums, idx-1)
            pre2 = self.recursive(nums, idx-2)
            if pre > pre2 + nums[idx]:
                return pre
            else:
                return pre2 + nums[idx]

    def test_empty(self):
        self.assertEqual(0,self.code.rob([]))

    def test_one(self):
        self.assertEqual(100, self.code.rob([100]))

    def test_two(self):
        self.assertEqual(3, self.code.rob([3,1]))

    def test_sequential(self):
        """
        test case: [1,3,4,5,6]

        """
        l = [1,3,4,5,6]
        self.assertEqual(self.recursive(l, len(l) - 1), self.code.rob(l))

    def test_10_40(self):
        """
        test case: randint....
        list size: 10~40
        """
        for i in range(10,40):
            l = [random.randint(1,100) for j in range(i)]
            print "random input list(len:{})".format(len(l)), l
            self.assertEqual(self.recursive(l, len(l) - 1), self.code.rob(l))
            print "ans",self.code.rob(l)

    # @unittest.skip("Too big")
    def test_seq100(self):
        """
        test case: 1..100
        list size: 100
        Recursive version can't solve it , cuz too large
        """
        l = range(1,100)
        # print self.code.rob(l)
        # self.assertEqual(self.recursive(l, len(l) - 1), self.code.rob(l))
        self.assertEqual(2500, self.code.rob(l))
        pass

    def test_zeropad100(self):
        """
        test case: randint 0 randint 0 randint 0 .....
        list size: 100
        range of randint : < 20
        """
        l = [ random.randint(1,100) if i % 2 else 0 for i in range(1,100)]
        ans = sum(l)
        self.assertEqual(ans, self.code.rob(l))

    def test_zeropadd100(self):
        """
        test case: randint 0 0 randint 0 0 randint 0 0.....
        list size: 100
        range of randint : < 100
        """
        l = [ random.randint(1,100) if i % 3 == 1 else 0 for i in range(1,100)]
        # print l
        ans = sum(l)
        self.assertEqual(ans, self.code.rob(l))


if __name__ == "__main__":
    unittest.main()