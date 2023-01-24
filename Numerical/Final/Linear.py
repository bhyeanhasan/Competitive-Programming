x = [95, 85, 80, 70, 60]
y = [90, 80, 70, 65, 60]

sx = 0
sy = 0

ssx = 0
sxy = 0
n = len(x)

for i in range(n):
    sx += x[i]
    sy += y[i]
    ssx += x[i] ** 2
    sxy += x[i] * y[i]

meanx = sx / n
meany = sy / n

b = (n * sxy - (sx * sy)) / (n * ssx - sx ** 2)

a = meany - b * meanx

print("%0.03f" % a)
