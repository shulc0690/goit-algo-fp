import numpy as np
import matplotlib.pyplot as plt


# Функція для імітації кидків кубиків
def roll_dice(num_rolls):
    sums = []
    for _ in range(num_rolls):
        dice1 = np.random.randint(1, 7)
        dice2 = np.random.randint(1, 7)
        sums.append(dice1 + dice2)
    return sums


# Кількість кидків
num_rolls = 100000

# Виконуємо імітацію кидків
sums = roll_dice(num_rolls)

# Обчислюємо ймовірності кожної суми
sum_counts = {i: 0 for i in range(2, 13)}
for result in sums:
    sum_counts[result] += 1

# Перетворюємо кількість на ймовірності
sum_probabilities = {k: v / num_rolls for k, v in sum_counts.items()}

# Відображення результатів на графіку
sums_list = list(sum_probabilities.keys())
probabilities_list = list(sum_probabilities.values())

plt.bar(sums_list, probabilities_list, color="blue", alpha=0.7)
plt.xlabel("Сума чисел на кубиках")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум чисел на кубиках (Монте-Карло)")
plt.xticks(np.arange(2, 13, step=1))
plt.grid(True)
plt.show()

# Вивід ймовірностей у вигляді таблиці
print("Сума\tЙмовірність")
for k, v in sum_probabilities.items():
    print(f"{k}\t{v:.4f}")
