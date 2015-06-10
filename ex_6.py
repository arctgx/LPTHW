# -*- coding:utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x # %r for debugging
print "I also said '%s'." % y

hilarious = False # hilarious 欢闹的; 令人捧腹的; 非常滑稽的; 喜不自禁的;
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side"
print w + e # 使用 + 来拼接字符串