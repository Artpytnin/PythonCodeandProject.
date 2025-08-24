money = int(input("Please input money : "))

coins10 = money // 10
money = money - (coins10 * 10)
coins5 = money // 5
money = money - (coins5 * 5)
coins2 = money // 2
money = money - (coins2 * 2)
coins1 = money 

print("10 = %d coins" % coins10)
print("5 = %d coins" % coins5)
print("2 = %d coins" % coins2)
print("1 = %d coins" % coins1)
