__author__ = 'phchang'
import traceback,sys

class Checker:
    """
    Validates houses if they statisfy the following conditions:
        1. index range
        2. adjacency relation
        4. difference between return value and sum of list
        3. empty case
    :param list_num:
    :param gold_ans:
    :param user_ans:
    :param list_house:
    :return:
    """

    def check_all(self, list_num, gold_ans, user_ans, list_house):
        # print "original list" , list_num
        # print "ans" , ans
        # print "return list", list_house
        return self.check_sum(list_num, gold_ans, user_ans, list_house) and \
               self.check_list(list_num, list_house)

    def check_sum(self, list_num, gold_ans, user_ans, list_house):
        """
        Check sum
        1. check gold answer and user answer
        2. check sum of return list
        """

        sum = 0
        try:
            assert gold_ans == user_ans , "Gold sum != User sum"

            for val in list_house:
                sum += list_num[val-1]  #off by one

            assert gold_ans == sum , "Sum of the return list isn't equal to return sum, %d vs %d" % (gold_ans,sum)
            # print "Pass check sum!"
            return True
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            return False


    def check_list(self,list_num, list_house):
        """
        Check adjecency list
        """
        pre = -1
        list_house.sort()
        try:
            for val in list_house:
                assert pre != val-1 ,"Adjaceny rule violated, (%d,%d)" % (pre, val-1)
                pre = val
            # print "Pass check_list!"
            return True
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            return False
