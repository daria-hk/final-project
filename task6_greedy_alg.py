class Item:
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
        self.ratio =  calories / value

def knapSack(items: list[Item], budget: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if budget >= item.value:
            budget -= item.value
            total_value += item.calories
            print(f"{item.name}: калорії - {item.calories}, ціна - {item.value}")
            print(f"Лишилось грошей: {budget}")
    return total_value


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# дані іжі
items_list = [Item(name, details["cost"], details["calories"]) for name, details in items.items()]
# бюджет
budget = 90
# виклик функції
print(f"Загальна кількість калорій в рамках бюджету: {knapSack(items_list, budget)}")  # 870
