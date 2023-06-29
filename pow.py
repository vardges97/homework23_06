
def power_of(x):
    def power(y):
        return x**y
    return power
    y = 3
res = power_of(3)
fin_res = res(4)
print(fin_res)
