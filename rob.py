__author__ = 'phchang'
import msgpack,sys

class Code:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        pre2,pre = 0, 0
        for i in num:
            pre2, pre = pre, max(pre2+i,pre)
        return pre


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


