__author__ = 'phchang'

import random
from rob import Code
import msgpack


if __name__ == '__main__':
    with open("input.txt", "w") as input, open("output.txt.gold","w") as output:
        tests = []
        tests.append([ random.randint(1,1000000) for i in range(100)])
        tests.append([ random.randint(1,1000000) for i in range(500)])

        zerofilled_test1 = []
        for i in range(10):
            zerofilled_test1.append(random.randint(1,100000))
            zerofilled_test1.extend([0] * random.randint(1,100))

        tests.append(zerofilled_test1)

        size = len(tests)
        coder = Code()
        packer = msgpack.Packer()
        input.write(packer.pack(size))

        for test in tests:
            input.write(packer.pack(test))

            ans = coder.rob(test)
            output.write(packer.pack(ans))
            output.write(packer.pack(test))

