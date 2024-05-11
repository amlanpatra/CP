# 45 cycle = 4*n ^ 2 + 1 // / even number ^ 2 + 1
# 90 cycle = 4*n ^ 2 - 9*n + 6
# 135 cycle = 4n ^ 2 - 10n + 7
# 180 cycle = 4*n ^ 2 - 3*n + 1
# 225 cycle = (2n+1) ^ 2 // / odd number ^ 2
# 270 cycle = 4*n ^ 2 + 3*n + 1
# 315 cycle = 4*n ^ 2 - 6*n + 3
# 360 cycle = 4*n ^ 2 - 7*n + 4
# derived from Ulam's spiral and oeis.org

for n in range(2, 100):
    print(4*((n-1)**2) - 3*(n-1) + 1)  # 180
    print(4*(n**2) - 10*n + 7)  # 135
    print(4*(n**2) - 9*n + 6)  # 90
    print(4*((n-1)**2) + 1)  # 45
    print(4*(n**2) - 7*n + 4)  # 360
    print(4*(n**2) - 6*n + 3)  # 315
    print(4*((n-1)**2) + 3*(n-1) + 1)  # 270
    print((2*(n-1)+1)**2)  # 225
