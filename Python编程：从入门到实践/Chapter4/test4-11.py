# 4-11 你的披萨和我的披萨

pizzas = ['pizza_a', 'pizza_b', 'pizza_c', 'pizza_d']

# 复制pizzas列表
friend_pizzas = pizzas[:]

# 在新的列表中做增加一种披萨
friend_pizzas.append('pizza_e')

# 打印两个新列表
print('\nMy favourite pizzas are:')
print(pizzas)
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
print(friend_pizzas)
for friend_pizza in friend_pizzas:
    print(friend_pizza)
