__author__ = 'phchang'
import msgpack

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
    with open("input.bin","r") as infile, open("output.txt","w") as outfile:
        packer = msgpack.Packer()
        unpacker = msgpack.Unpacker(infile)

        # cnt_test = unpacker.readline()
        print unpacker, type(unpacker)
        # outfile.write(packer.pack(result))

