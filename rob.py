__author__ = 'phchang'
import msgpack,sys

class Code:

    # Version 1
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        pre2,pre = 0, 0
        for i in num:
            pre2, pre = pre, max(pre2+i, pre)
        return pre

    # Version 2
    # @param num, a list of integer
    # @return an integer, an list of precedence
    def rob_list(self, num):
        dp = [0] * (len(num)+1)
        pre = [0] * (len(num)+1)
        if len(num) == 0:
            return 0, []

        mynum = [0] + num  # Not to override the original number list
        dp[1] = mynum[1]
        pre[1] = 1
        for i in range(2, len(mynum)):
            dp[i] = max(dp[i-2] + mynum[i], dp[i-1])
            pre[i] = i-2 if dp[i-2] + mynum[i] > dp[i-1] else i-1

        sum = dp[-1]
        path = []
        while sum != 0:
            idx = dp.index(sum)  # find first index of value
            sum -= mynum[idx]
            path.append(idx)

        return dp[-1], path[::-1]


if __name__ == "__main__":

    #with open("input.txt","r") as infile, open("output.txt","w") as outfile:
    with open("input.bin","r") as infile, open("output.bin","w") as outfile:
        packer = msgpack.Packer()
        unpacker = msgpack.Unpacker(infile)
        # TODO: Get the line from unpacker
        cnt_test =  unpacker.next()
        solver = Code()
        for val in unpacker:  # val is type of str
            print "input:", val.strip()
            ans = '%d\n' % (Code().rob(map(lambda x:int(x),val.strip().split())))
            print "output:", ans ,
            # TODO: Write result to packer
            outfile.write(packer.pack(ans))


