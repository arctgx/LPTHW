# -*- coding:utf-8 -*-

"""
复制文件
"""

from sys import argv
from os.path import exists


script, from_file, to_file = argv

print "copy file [%s] to [%s]." % (from_file, to_file)

in_file = open(from_file)
in_data = in_file.read()

print "The input file is %d bytes long." % len(in_data)

print "Does the output file exists? %r" % exists(to_file)

out_file = open(to_file, 'w')
out_file.write(in_data)

print "copt file %s to %s done" % (from_file, to_file)
in_file.close();
out_file.close();