word = input()

while not word == "end":
    print(f"{word} = {(word[::-1])}")

    word = input()

#
# x = "apples"
# y = "lemons"
#
# z = "I like %s and %s" % (x, y)
#
# print(z)