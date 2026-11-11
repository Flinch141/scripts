import numpy as np
import matplotlib.pyplot as plt

days = range(1,15)
t_night = [-1.2,0.3,-2.1,1.5,3.8,2.4,0.9,-0.4,1.8,3.2,4.6,2.9,1.1,-0.3]
t_day = [5.1,6.3,4.8,7.2,9.5,8.1,6.7,5.9,7.4,8.8,10.2,9.1,7.5,6.2]
t_0 = [0]*len(days)

aver_d = [sum(t_day)/14]*14
aver_n = [sum(t_night)/14]*14

fig, ax = plt.subplots(figsize=(10,7))

ax.plot(days,t_day,color='orange',marker='o',label=f't днем')
ax.plot(days,aver_d,color='orange',label=f'Средняя температура днём')

ax.plot(days,t_night,color='blue',marker='s',ls='--',label=f't днем')
ax.plot(days,aver_n,color='blue',ls='--',label=f'Средняя температура ночью')

ax.plot(days,t_0,)

ax.set_title('Температура днём и ночью')
ax.set_xlabel('День')
ax.set_ylabel('Температура C°')

ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left')

fig.savefig('weather.png',dpi=150)
plt.show()