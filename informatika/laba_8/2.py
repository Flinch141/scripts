import numpy as np
import matplotlib.pyplot as plt

days = list(range(1, 15))
screen = [4.5, 5.2, 5.8, 4.9, 6.1, 6.8, 7.2, 7.5, 8.1, 7.8, 8.5, 9.0, 9.3, 9.7]
battery = [58, 52, 48, 55, 42, 38, 33, 29, 22, 25, 18, 14, 11, 8]

avg1= [sum(screen)/len(screen)] * 14
avg2= [sum(battery)/len(battery)] * 14

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.plot(days,screen,marker='o',label=f'Экран.ч.')
ax1.plot(days,avg1,ls='--',color='tab:blue')

ax2.plot(days,battery,marker='s',color='orange',label=f'Процент заряда')
ax2.plot(days,avg2,ls='--',color='orange')

ax1.set_title('Экранное время')
ax1.set_xlabel('День')
ax1.set_ylabel('Часы')

ax2.set_title('Заряд батареи к кноцу дня')
ax2.set_xlabel('День')
ax2.set_ylabel('Процент заряда')

ax1.grid(True, linestyle='--', alpha=0.6)
ax2.grid(True, linestyle='--', alpha=0.6)

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

ax1.set_ylim(0, 11)
ax2.set_ylim(0, 100) 

fig.savefig('phone.png',dpi=150)

plt.show()