n = int(input())
power_one = 1
power_two = 2
while power_two <= n:
    power_two *= 2
    power_one += 1
print(power_one - 1, power_two // 2)