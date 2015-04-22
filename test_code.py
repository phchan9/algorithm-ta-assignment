import unittest
from rob import Code
import random

__author__ = 'phchang'


class TestCode(unittest.TestCase):

    def setUp(self):
        self.code = Code()
        self.test_sum = 0

    def recursive(self, nums , idx):
        """
        Recursive Version for this Rob problem
        :param nums:
        :param idx:
        :return:
        """
        if idx < 0:
            return 0
        else:
            pre = self.recursive(nums, idx-1)
            pre2 = self.recursive(nums, idx-2)
            if pre > pre2 + nums[idx]:
                return pre
            else:
                return pre2 + nums[idx]

    def check_list(self,list_num ,ans ,list_house):
        """
        Validates houses if they statisfy the following conditions:
            1. index range
            2. adjacency relation
            4. difference between return value and sum of list
            3. empty case
        :param list_num:
        :param ans:
        :param list_house:
        :return:
        """
        sum = 0
        print list_house

        # Check sum
        for val in list_house:
            sum += list_num[val]

        print "Check?", ans, sum

        self.assertEqual(ans,sum,"Sum of the return list isn't equal to return sum, %d vs %d" % (ans,sum))

        # Check adjacency
        pre = -2
        for val in list_house:
            self.assertNotEqual(pre, val-1, "Adjaceny rule violated, (%d,%d)" %(pre, val-1))
            pre = val

        print "Pass check_list!"



    ### Version 1 ###################################
    def test_empty(self):
        self.assertEqual(0,self.code.rob([]))

    def test_one(self):
        self.assertEqual(100, self.code.rob([100]))

    def test_two(self):
        self.assertEqual(3, self.code.rob([3,1]))

    def test_four(self):
        l = [25,0,12,83]
        self.assertEqual(108, self.code.rob(l))

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
        range of randint : < 100
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

    ### Version 2 ###################################
    def test_empty_checklist(self):
        l = []
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)

    def test_one_checklist(self):
        l = [100]
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)

    def test_seq100_checklist(self):
        l = range(1, 100)
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(2500, ans)
        self.check_list(l, ans, ret_list)

    def test_zeropad100_checklist(self):
        """
        test case: randint 0 randint 0 randint 0 .....
        list size: 100
        range of randint : < 100
        """
        l = [ random.randint(1,100) if i % 2 else 0 for i in range(1,100)]
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)

    def test_zeropadd100_checklist(self):
        """
        test case: randint 0 0 randint 0 0 randint 0 0.....
        list size: 100
        range of randint : < 100
        """
        l = [ random.randint(1,100) if i % 3 == 1 else 0 for i in range(1,5)]
        print l
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)
        # TODO: Debug this case, return precedence list Error!


if __name__ == "__main__":
    unittest.main()