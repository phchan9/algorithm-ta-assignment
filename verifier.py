#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import datetime
from checker import Checker
import msgpack


def DetectRuntimeError(filename):
	f = open(filename, 'r')
	for line in f:
		if ( line.find('run_innerloop detected host state invariant failure') >=0 ):
			return True
	return False

def Log(msg, bStdout = True):
	log_file = open('reliable_wrapper_log.report','a')
	szLine = '[' + str(datetime.datetime.now()) + ']\t' + msg
	log_file.write(szLine + '\n')
	if (bStdout):
		print(szLine)
	log_file.close()

def Equal(out_string, gold_string):
	out_words = out_string.split()
	gold_words = gold_string.split()
	return out_words == gold_words



if __name__ == "__main__":

	if (len(sys.argv) != 2):
		Log("Syntax: verifier.py clean|checkname")
		sys.exit(-1)

	if (sys.argv[1]=='clean'):
		os.remove('output.txt')
		sys.exit(0)


	with open('output.txt.{0}'.format(sys.argv[1]), 'r') as f:
		unpacker = msgpack.Unpacker(f)
		#outputs = [line.strip() for line in unpacker if line.strip()]
		outputs = [line for line in unpacker]

	with open('output.txt.gold', 'r') as f:
		unpacker = msgpack.Unpacker(f)
		#outputs_gold = [line.strip() for line in unpacker if line.strip()]
		outputs_gold = [line for line in unpacker]


	fCP = open('check_pattern_concise_{0}.report.final'.format(sys.argv[1]),'w')
	nTest = len(outputs_gold)/2
	teacher = Checker()

	for k in range(0, min(len(outputs),len(outputs_gold)),2):
		#gold_ans = int(outputs_gold[k])
		#orig_list = map(lambda x:int(x),outputs_gold[k+1].split())
		#user_ans = int(outputs[k])
		#ret_list = map(lambda x:int(x),outputs[k+1].split())
		gold_ans, user_ans = outputs_gold[k], outputs[k]
		orig_list, ret_list = outputs_gold[k+1], outputs[k+1]

		if ( teacher.check_all(orig_list, gold_ans, user_ans, ret_list)):
			strCheck = 'check {0}: PASSED (1/{1})\n'.format(k/2+1, nTest)
		else:
			strCheck = 'check {0}:        (0/{1})\n'.format(k/2+1, nTest)
		fCP.write(strCheck)

	fCP.close()
