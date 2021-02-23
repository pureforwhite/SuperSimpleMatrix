import random as r
import time

s = ["0", "", "", ' ']
l = []
c = 0

for i in range(118):
	x = r.randint(0,3)
	l.append(s[x])

	c += 1

for i in range(10000):
	if c % 5== 0:
		x_s = [r.randint(0,117)for x in range(10)]

		for i in x_s:
			l[i] = s[r.randint(0,3)]
	print(*l)
	c += 1
	time.sleep(0.1)
