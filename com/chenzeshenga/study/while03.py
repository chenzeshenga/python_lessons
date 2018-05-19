i = 1

while i < 10:
    j = 1
    while j <= i:
        result = i * j
        print("%s*%s=%s" % (j, i, i * j), end="\t")
        j += 1
    print()
    i += 1
