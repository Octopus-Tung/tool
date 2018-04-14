#!/usr/bin/env python

import sys
import hashlib

def read_shattered():

	f1 = open('shattered-1.pdf','rb')
	f2 = open('shattered-2.pdf','rb')

	shattered1 = f1.read(320)
	shattered2 = f2.read(320)

	f1.close()
	f2.close()
	
	return [shattered1, shattered2]

def collision(shattered, put_something, start_with):

	for i in range(10000000):
		suffix = str(hex(i))[2:]
		if len(suffix) % 2 == 1:
			suffix = '0' + suffix
		m = hashlib.sha1()
		m.update(shattered[0] + str(put_something) + suffix.decode("hex"))
		if m.hexdigest().startswith(str(start_with)):
			print 'meet @ ' + str(i)
			print hashlib.sha1(shattered[0] + str(put_something) + suffix.decode("hex")).hexdigest()
			print hashlib.sha1(shattered[1] + str(put_something) + suffix.decode("hex")).hexdigest()
			break
		elif i == 9999999:
			print 'Not found! QAQ'

if __name__ == "__main__":
	argc = len(sys.argv)
	if argc > 3:
		print 'Error!'
		sys.exit()
	else:
		shattered = read_shattered()
		if argc == 1:
			collision(shattered, '', '')
		elif argc == 2:
			collision(shattered, sys.argv[1], '')
		elif argc == 3:
			collision(shattered, sys.argv[1], sys.argv[2])
		sys.exit()

