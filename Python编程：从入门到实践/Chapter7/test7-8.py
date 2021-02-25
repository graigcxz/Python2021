# -*- utf-8 -*-

# 7-8：熟食店

sandwich_orders = ['chicken sandwich', 'cheese sandwich', 'ham sandwich', 'tuna sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    finished_sandwiches.append(current_sandwich)
    print("I made you " + current_sandwich + '.')

print("I have made these sandwiches: ")
print(finished_sandwiches)
