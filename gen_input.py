__author__ = 'phchang'

import random
from rob import Code


if __name__ == '__main__':
    with open("input.txt", "w") as input, open("output.txt.gold","w") as output:
        tests = []
        # tests.append([])
        tests.append([100])
        tests.append([ random.randint(1,10000) for i in range(100)])
        tests.append([ random.randint(1,10000) for i in range(500)])
        tests.append([ random.randint(1,10000) for i in range(1500)])
        tests.append([ random.randint(1,10000) for i in range(2500)])
        tests.append([ random.randint(1,10000) for i in range(5500)])
        tests.append([ random.randint(1,10000) for i in range(9500)])

        zerofilled_test1 = []
        for i in range(40):
            zerofilled_test1.append(random.randint(1,1000))
            zerofilled_test1.extend([0] * random.randint(1,100))
        zerofilled_test2 = [0]*10000
        zerofilled_test2[3333] = 1234

        zerofilled_test3 = [0]*10000
        zerofilled_test3.insert(0,199999)
        zerofilled_test3.append(23232323)

        tests.append(zerofilled_test1)
        tests.append(zerofilled_test2)
        tests.append(zerofilled_test3)

        size = len(tests)
        first_line = "%d\n" % (size)
        input.write(first_line)
        coder = Code()

        for test in tests:
            line = "%s\n" % ( " ".join(map(str,test)))
            input.write(line)

            ans = coder.rob(test)
            ans_line = "%d\n" % ans
            output.write(ans_line)
            output.write(line)

