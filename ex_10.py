# -*- coding:utf-8 -*-

# escape string
# \\
# \'
# \"
# \a bell
# \b backspace
# \f formfeed
# \n  linefeed
# \N{name} charter named name in the unicode database
# \r carriage return
# \t tab
# \uxxxx charter with 16-bit hex value xxxx(unicode only)
# \Uxxxxxxxx charter with 32-bit hex value xxxxxxxx (unicode only)
# \v ASCII Vertical tab
# \ooo charter with octal value ooo
# \xhh charter with hex value hh



tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,