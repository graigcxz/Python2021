# -*- utf-8 -*-

# 7-9 五香烟熏牛肉(pastrami)卖完了

sandwich_orders = ['pastrami', 'chicken sandwich', 'pastrami', 'cheese sandwich', 'ham sandwich', 'pastrami',
                   'tuna sandwich']
finished_sandwiches = []
print("All of pastrami have been sold out!")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    else:
        finished_sandwiches.append(current_sandwich)
        print("I made you " + current_sandwich + '.')

print("\nI have made these sandwiches: ")
print(finished_sandwiches)
