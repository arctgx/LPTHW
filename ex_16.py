# -*- coding:utf-8 -*-

from sys import argv

script, file_name = argv

target = open(file_name, 'w')

print "Truncating the file [%s]." % file_name
target.truncate()

print "Now input three lines."

line_1 = raw_input("line_1 : ")
line_2 = raw_input("line_2 : ")
line_3 = raw_input("line_3 : ")

print "Save to file [%s]." % file_name
target.write(line_1)
target.write("\n")

target.write(line_2)
target.write("\n")

target.write(line_3)
target.write("\n")

print "close file[%s]." % file_name
target.close()