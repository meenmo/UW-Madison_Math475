count = 0
for i in range(1,10001):
    if (i % 4 == 0) or (i % 6 == 0) or  (i % 7 == 0) or (i % 10 == 0):
        count += 1

print(10000-count)
