# 1

a = 5
b = 3
c = 10
d = 10
print('1. ', ((a ** 5 * b ** 10) ** (1/2) / (c + d) ** 5) ** (1/5))

# 2

xa, ya = (782, 645)
xb, yb = (-834, 801)
xc, yc = (0, 0)
xd, yd = (482, -176)
ab = ((xb - xa) ** 2 + (yb - ya) ** 2) ** (1/2)
cd = ((xc - xd) ** 2 + (yc - yd) ** 2) ** (1/2)
print('2. ', '|AB|= ', ab, '|CD|= ', cd)

# 3
# angle between two vectors:
# cos(phi) = (a, b)/(|a|*|b|)

from math import acos, degrees

x1 = xb - xa
y1 = yb - ya
x2 = xd - xc
y2 = yd - yc
cos_phi = (x1 * x2 + y1 * y2) / (ab * cd) # in radians
print('3. ', 'Angle between AB and CD (in degrees): ', 180 - degrees(acos(cos_phi))) # need acute angle

# 4
# sin^2(x) + cos^2(x) = 1

import math
phi = math.pi / 4
res1 = math.sin(phi) ** 2 + math.cos(phi) ** 2
phi = math.pi / 8
res2 = math.sin(phi) ** 2 + math.cos(phi) ** 2
phi = math.pi / 1000
res3 = math.sin(phi) ** 2 + math.cos(phi) ** 2
print('4. ', res1, res2, res3)

# 5
# len() function counts length of string

x = 2
res1 = len(str(2 ** x ** x))
x = 5
res2 = len(str(2 ** x ** x))
x = 7
res3 = len(str(2 ** x ** x))
print('5. ', res1, res2, res3)
