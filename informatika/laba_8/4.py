import matplotlib.pyplot as plt
from pathlib import Path

labels = ['Спасает мир', 'Восстанавливает суперсилы во сне',
          'Играет в кибер-квесты', 'Другое']
hours = [8, 7, 5, 4]

fig, ax = plt.subplots(figsize=(7, 7))

ax.pie(hours,
       labels=labels,
       autopct='%1.1f%%',
       startangle=90,
       colors=['tab:red', 'tab:blue', 'tab:green', 'tab:orange'])

ax.set_title('День супергероя Алексея')

fig.tight_layout()

fig.savefig('superhero.png', dpi=150)
plt.show()