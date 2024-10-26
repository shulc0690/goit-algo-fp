def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if info["cost"] <= budget:
            budget -= info["cost"]
            total_calories += info["calories"]
            chosen_items.append(item)

    return chosen_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100
chosen_items, total_calories = greedy_algorithm(items, budget)
print(f"Вибрані страви: {chosen_items}")
print(f"Загальна калорійність: {total_calories}")


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info["cost"]
        calories = item_info["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відтворення вибраних страв
    w = budget
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, item_info = item_list[i - 1]
            chosen_items.append(item_name)
            w -= item_info["cost"]

    return chosen_items, dp[n][budget]


budget = 100
chosen_items, total_calories = dynamic_programming(items, budget)
print(f"Вибрані страви: {chosen_items}")
print(f"Загальна калорійність: {total_calories}")
