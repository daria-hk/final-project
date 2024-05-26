def knapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]
    # Створюємо таблицю для зберігання інформації про вибрані предмети
    selected_items = [[False for w in range(W + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                # Перевіряємо, чи краще вибрати поточний предмет
                if val[i - 1] + K[i - 1][w - wt[i - 1]] > K[i - 1][w]:
                    K[i][w] = val[i - 1] + K[i - 1][w - wt[i - 1]]
                    selected_items[i][w] = True
                else:
                    K[i][w] = K[i - 1][w]
            else:
                K[i][w] = K[i - 1][w]

    # Повертаємо оптимальну вартість та інформацію про вибрані предмети
    return K[n][W], selected_items

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

cost = [item["cost"] for item in items.values()]
calories = [item["calories"] for item in items.values()]
budget = 90
n = len(calories)

# Оптимальна вартість
total_value, selected_items = knapSack(budget, cost, calories, n)
print("Загальна кількість калорій в рамках бюджету:", total_value)

# Виводимо вибрані предмети
total_cost = budget
for i in range(n, 0, -1):
    if selected_items[i][total_cost]:
        item_name = list(items.keys())[i - 1]
        item_calories = calories[i - 1]
        item_value = cost[i - 1]
        print(f"{item_name}: калорії - {item_calories}, ціна - {item_value}")
        total_cost -= cost[i - 1]
        print(f"Лишилось грошей: {total_cost}")
