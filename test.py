import math
comb = math.comb(90, 2)
p = comb * (0.007**2) * ((1-0.007)**88)
print(str(100*p) + "%")