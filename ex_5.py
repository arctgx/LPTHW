# -*- coding:utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = "white"
my_hair = "Brown"


print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's teeth are usually %s depending ne the coffee." % my_teeth

# 多个
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print "If I add %r, %r and %r I get %r." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

test_float = 4.55
print "%r round to %d." % (test_float, round(test_float))