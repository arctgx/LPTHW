# -*- coding:utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But It didn't sing.",
    "So I said goodnight."
)

print "%s" % "测试啊测试" # 测试啊测试
print "%r" % "测试啊测试" # '\xe6\xb5\x8b\xe8\xaf\x95\xe5\x95\x8a\xe6\xb5\x8b\xe8\xaf\x95'

