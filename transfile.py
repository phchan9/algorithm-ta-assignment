from __future__ import with_statement
import msgpack,sys
__author__ = 'phchang'



def compress(filename):
    f_prefix = filename.split(".")[0]
    with open(filename,"r") as infile, open(f_prefix+".bin","w") as outfile:
        packer = msgpack.Packer()
        for s in infile:
            outfile.write(packer.pack(s))

def extract(filename):
    f_prefix = filename.split(".")[0]
    with open(filename,"r")  as infile ,open(f_prefix+".txt","w") as outfile:
        unpacker = msgpack.Unpacker(infile)
        for s in unpacker:
            outfile.write(s)




if __name__ == "__main__":
    # TODO: Add python argparse use, -pack -unpack -verbose(-v, which print in stdin)
    usage = "Usage: python gen_binary.py <pack/unpack> <filename>"
    if len(sys.argv) != 3:
        print usage
    else:
        if sys.argv[1] == "unpack":
            extract(sys.argv[2].strip())
        elif sys.argv[1] == "pack":
            compress(sys.argv[2].strip())
        else:
            print "Error mode: only for pack/unpack"
            print usage
