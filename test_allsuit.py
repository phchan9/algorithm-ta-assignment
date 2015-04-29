import unittest
from rob import Code
import random

__author__ = 'phchang'


class TestCode(unittest.TestCase):



    def memoziation(self, nums):
        """
        Memorization version for this problem
        :param nums:
        :return:
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        mm = [-1] * len(nums)
        mm[0] = nums[0]
        mm[1] = nums[1] if nums[1] > nums[0] else nums[0] # NOTICE this keypoint
        def mem_recursive(nums, idx):

            if mm[idx] != -1:
                return mm[idx]

            mm[idx] = max( mem_recursive(nums,idx-2) + nums[idx], mem_recursive(nums, idx-1))
            return mm[idx]

        return mem_recursive(nums, len(nums)-1)

    def verifier(self,list_num ,ans ,list_house):
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
        # Check Correctness by memoziation version
        print "Check if ans is equal to memozation version ?",
        self.assertEqual(self.memoziation(list_num), ans, "Not equal to memoziation version")
        print "Y"

        # Check sum
        print "return list" ,list_house
        sum = 0
        for val in list_house:
            if val > len(list_num) or val <= 0:
                self.fail("index out of range in returen list")
            sum += list_num[val-1]  # This is real index , off by 1

        print "Check if sum of list (%d) == ans (%d)?" % (sum, ans),
        self.assertEqual(ans,sum,"Sum of the return list isn't equal to return sum, %d vs %d" % (ans,sum))
        print "Y"

        # Check adjacency
        print "Check adjacency of return list ?",
        pre = -2
        for val in list_house:
            self.assertNotEqual(pre, val-1, "Adjaceny rule violated, (%d,%d)" %(pre, val-1))
            pre = val
        print "Y"

        print "Pass !"

    def setUp(self):
        self.code = Code()
        self.runner = self.code.rob_list


    def test_0(self):
        l = []
        ans, ret_list = self.runner(l)
        print l
        self.verifier(l, ans, ret_list)

    def test_1(self):
        l = [100]
        ans, ret_list = self.runner(l)
        print l
        self.verifier(l, ans, ret_list)

    def test_rand(self):
        scopes = [100, 500, 1000]
        for scope in scopes:
            l = [ random.randint(1,1000) for i in range(scope)]
            ans, ret_list = self.runner(l)
            print l
            self.verifier(l, ans, ret_list)

    def test_zerofilled(self):
        l = []
        for i in range(40):
            l.append(random.randint(1,10000))
            l.extend([0]*random.randint(1,50))
        ans, ret_list = self.runner(l)
        print l
        self.verifier(l, ans, ret_list)

    def test_middle_zero(self):
        l = [ 0 if i != 51 else 1 for i in range(100)]
        ans, ret_list = self.runner(l)
        print l
        self.verifier(l, ans, ret_list)

    def test_first_tail_zero(self):
        l = [ 0 if i != 1 and i != 89 else 1 for i in range(100)]
        ans, ret_list = self.runner(l)
        print l
        self.verifier(l, ans, ret_list)

    @unittest.skip("Just for test of recursion depth")
    def test_limit_memo(self):
        for i in range(1200,1400):  # upper 1400 , get limit
            l = [ random.randint(1,10000) for j in range(i)]
            ans, ret_list = self.runner(l)
            print l
            self.verifier(l, ans, ret_list)


if __name__ == "__main__":
    unittest.main()
