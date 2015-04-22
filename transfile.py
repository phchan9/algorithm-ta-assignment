from __future__ import with_statement
import msgpack,sys
import argparse
__author__ = 'phchang'



def compress(filename):
    f_prefix = filename.split(".")[0]
    print "MsgPack Packs", filename, "to", f_prefix+".bin"
    with open(filename,"r") as infile, open(f_prefix+".bin","w") as outfile:
        packer = msgpack.Packer()
        for s in infile:
            outfile.write(packer.pack(s))

def extract(filename):
    f_prefix = filename.split(".")[0]
    print "MsgPack Unpacks", filename, "to", f_prefix+".txt"
    with open(filename,"r")  as infile ,open(f_prefix+".txt","w") as outfile:
        unpacker = msgpack.Unpacker(infile)
        for s in unpacker:
            outfile.write(s)

def parser_init():
    parser = argparse.ArgumentParser(description="pack/unpack bin/txt file")
    parser.add_argument("file", help="*.bin/*.txt")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--pack", help="msgpack function to pack *.txt file", action="store_true")
    group.add_argument("-x", "--unpack", help="msgpack function to unpack *.bin file", action="store_true")
    parser.add_argument("-v","--verbose", help="More info", action="count", default=0)
    return parser

def print_file(filename, nopacked):
    with open(filename,"r") as fin:
        if nopacked:
            for line in fin:
                print line.strip()
        else:
            unpacker = msgpack.Unpacker(fin)
            for line in unpacker:
                print line.strip()



if __name__ == "__main__":
    parser = parser_init()
    args = parser.parse_args()

    if args.pack:
        compress(args.file)
    elif args.unpack:
        extract(args.file)
    else:
        parser.error("Should set option [-c | -x]")

    if args.verbose >= 1:
        print_file(args.file, args.pack)

    print "Done!"

