import unittest
from rob import Code
from checker import Checker
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

    def memoziation(self, nums):
        mm = [-1] * len(nums)
        mm[0] = nums[0]
        mm[1] = nums[1] if nums[1] > nums[0] else nums[0] # NOTICE this keypoint
        def mem_recursive(nums, idx):

            if mm[idx] != -1:
                return mm[idx]

            mm[idx] = max( mem_recursive(nums,idx-2) + nums[idx], mem_recursive(nums, idx-1))
            return mm[idx]

        return mem_recursive(nums, len(nums)-1)
        # Debug use
        # ans = mem_recursive(nums, len(nums)-1)
        #print mm
        #return ans


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
            sum += list_num[val-1]  #off by one

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
        self.assertEqual(self.memoziation(l), self.code.rob(l))

    def test_10_40(self):
        """
        test case: randint....
        list size: 10~40
        """
        for i in range(10,40):
            l = [random.randint(1,100) for j in range(i)]
            print "random input list(len:{})".format(len(l)), l
            #self.assertEqual(self.recursive(l, len(l) - 1), self.code.rob(l))
            self.assertEqual(self.memoziation(l), self.code.rob(l))
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
        l = [ random.randint(1,100) if i % 3 == 1 else 0 for i in range(1,100)]
        print l
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)
        # TODO: Debug this case, return precedence list Error!

    def test_zerofilled_checklist(self):
        """
        test case:  0 0 0 0.... 1 0 0 0....
        :return:
        """
        l = [0]*20
        l.insert(9,123)
        print l
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)

    def test_zerofilledmiddle_checklist(self):
        """
        test case:  1 0 0 0.... 0 0 0 0.... 1
        :return:
        """
        l = [0]*20
        l.insert(0,123)
        l.append(321)
        print l
        ans, ret_list = self.code.rob_list(l)
        self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)

    def test_zerorandomfilled_checklist(self):
        """
        random zero padded interval
        test case:  1 0 1 0 0 123 0 .... 1 0 0 0....
        :return:
        """
        l = []
        for i in range(40):
            l.append(random.randint(1,100))
            l.extend([0] * random.randint(1,10))
        print l
        ans, ret_list = self.code.rob_list(l)
        # self.assertEqual(sum(l), ans)
        self.assertEqual( self.memoziation(l), ans)
        self.check_list(l, ans, ret_list)

    def test_random10_checklist(self):
        l = [ random.randint(1,100) for i in range(1,10)]
        print l
        ans, ret_list = self.code.rob_list(l)
        # self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)

    def test_random100_checklist(self):
        l = [ random.randint(1,100) for i in range(1,100)]
        print l
        ans, ret_list = self.code.rob_list(l)
        # self.assertEqual(sum(l), ans)
        self.check_list(l, ans, ret_list)

    def test_checker(self):

        teacher = Checker()
        l = [ random.randint(1,100) for i in range(1,55000)]
        # print l
        ans, ret_list = self.code.rob_list(l)
        # ret_list = ret_list[::-1]
        gold_ans = self.code.rob(l)
        self.assertTrue(teacher.check_all(l, gold_ans, ans, ret_list),"Checker Fail!")
        l = []
        print l
        ans, ret_list = self.code.rob_list(l)
        gold_ans = self.code.rob(l)
        self.assertTrue(teacher.check_all(l, gold_ans, ans, ret_list),"Checker Fail!")
        l = [100]
        print l
        ans, ret_list = self.code.rob_list(l)
        gold_ans = self.code.rob(l)
        self.assertTrue(teacher.check_all(l, gold_ans, ans, ret_list),"Checker Fail!")

if __name__ == "__main__":
    unittest.main()