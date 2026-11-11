import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

names = ['Маргарита Мания', 'Пепперони-Парад', 'Гавайский Хаос',
         'Четыре Сыра и Слёзы', 'Веганский Бунт']
sales = [23, 45, 56, 78, 32]

x = np.arange(len(names))

w = max(sales)
for i in range(len(sales)):
    if sales[i] == w:
        win = i
        break

colors = ['tab:blue'] * len(names)
colors[win] = 'orange'

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(x, sales, width=0.6, color=colors,
              edgecolor='blue', linewidth=1.5, hatch='//')

for i in range(len(x)):
    ax.text(x[i], sales[i] + 1, str(sales[i]), ha='center')

ax.set_xticks(x)
ax.set_xticklabels(names, rotation=15)

ax.set_title('Битва пиццерий: продажи за неделю', fontsize=15, fontweight='bold')
ax.set_xlabel('Пиццерия', fontsize=12)
ax.set_ylabel('Продано пицц, шт.', fontsize=12)
ax.set_ylim(0, max(sales) * 1.15)
ax.grid(axis='y', linestyle='--', alpha=0.5)

fig.tight_layout()

fig.savefig('pizzeria.png', dpi=150)
plt.show()