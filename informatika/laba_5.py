# 1
# stroka = str(input())
# res = ''
# for i in stroka:
#     if i.isalpha():
#         res += i
# print(res)
# 2
# size = int(input())
# i = 1
# while i < size + 1:
#     spaces = ' ' * (size - i)
#     slash = '#' * (2 * i - 1)
#     print(spaces + slash)
#     i += 1
# a = ' ' * (size - 1)
# print(a + "#")
# лаба 3 9 задание
# number = str(input())
# number = list(number)
# flag = True
# for i in range(len(number) - 2):
#     a,b,c = number[i], number[i+1], number[i+2]
#     if (a.isdigit() and b.isdigit() and c.isdigit()):
#         flag = False
#         break
# if flag:
#     print("Знак старый")
# else:
#     print("Знак новый")
#3
# n = int(input())
# ln = len(str(n))
# cnt = 0
# for i in range(1,n+1):
#     ln = len(str(i))
#     digit = str(i)
#     p = sum(int(j) ** ln for j in digit)
#     if p == i:
#         cnt += 1
# print(cnt)
# 4
# text = str(input())
# word = str(input())
# res = ''
# l = 0
# for i in text:
#     if i == word[l]:
#         l += 1
#         res += i
#     if res == word:
#         break
# if res == word:
#     print(True)
# else:
#     print(False)
#5
# from random import*
# a = randint(1, 100)
# while True:
#     dig = int(input())
#     if dig == a:
#         break
#     if dig > a:
#         print("число больше")
#     elif dig < a:
#         print("Число меньше")
#     else:
#         print("Ты угадал")
#         break
#6
# message = str(input("Введите сообщение: "))
# choice = int(input("Выберите действие(1-11): "))
# if choice == 1:  #1
#     x = ''
#     lst = [x for x in message if x != ',' and x != ' ']
#     new = ''
#     for i in lst:
#         new = new + i
#     new = new.lower()
#     if new == new[::-1]:
#         print(True)
#     else:
#         print(False)
# if choice == 2:  #2
#     cnt = 0
#     for i in message:
#         if i.isalpha():
#             cnt += 1
#     print(cnt)
# if choice == 3:  #3
#     if message.isdigit():
#         print("Только цифры")
#     else: print("NO")
# if choice == 4:   #4
#     if message.isalpha():
#         print('Yes')
#     else:
#         print('No')
# if choice == 5:  #5
#     print(message[::-1])
# if choice == 6:  #6
#     print(message.upepr())
# if choice == 7:  #7
#     print(message.lower())
# if choice == 8:  #8
#     print(message.replace(' ','_'))
# if choice == 9:     #9
#     if message.find("@"):
#         print('Yes, its email')
#     else:
#         print('its not email')
# if choice == 10:   #10      
#     print(message[message.find("@"):])
# 7
# email = input()
# password = input()
# flag = True
# flage = True
# if email.count('@') != 1:
#     print('нет занка @')
#     flag = False
# if email.find('@') > email.find('.'):
#     print('Точка стоит перед знаком @')
#     flag = False
# if (email[0] == '@' or email[0] == '.'):
#     print('Email начинается не с того знака')
#     flag = False
# if (email[-1] == '@' or email[-1] == '.'):
#     flag = False
#     print('Email кончается не тем знаком')
# if 6 > len(email) or len(email) > 30:
#     print('Недопустимая длина')
#     flag = False
# if len(password) < 8:
#     print('Длниа пароля недопустимая')
#     falge = False
# if (password.count('0') == 0 and password.count('1') == 0 and password.count('2') == 0
#     and password.count('3') == 0 and password.count('4') == 0 and password.count('5') == 0
#     and password.count('6') == 0 and password.count('7') == 0 and password.count('8') == 0
#     and password.count('9') == 0):
#     print('В пароле нет цифр')
# if password == password.lower():
#     print('Заглавных букв нет')
#     flage = False
# if password == password.upper():
#     print('Строчных букв нет')
#     flage = False
# if (password.count('!') == 0 and password.count('@') == 0 and password.count('#') == 0
#     and password.count('$') == 0 and password.count('$') == 0 and password.count('%') == 0
#     and password.count('^') == 0 and password.count('&') == 0
#     and password.count('*') == 0):
#     flage = False
#     print('Пароль не содержит спец. символов')
# 8
# lines = [input() for x in range(3)]
# xk = []
# vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
# for i in range(len(lines)):
#     cnt = 0
#     for j in range(len(lines[i])):
#         if lines[i][j] in vowels:
#             cnt += 1
#     xk.append(cnt)
# if xk[0] == 5 and xk[1] == 7 and xk[2] == 5:
#     print('Хайку')
# else:
#     print("Не хайку")
# 9
word = input()
if word[-1] == '#':
    res = []
    word = word[:-1]
    if len(word) % 2 == 0:
        for i in range(0,len(word),2):
            res.append(word[i])
        for i in range(len(word)-1,0,-2):
           res.append(word[i])
    else:
        for i in range(0,len(word),2):
            res.append(word[i])
        for i in range(len(word)-2,0,-2):
            res.append(word[i])

    rr = ''
    for i in res:
        rr = rr + i
    print(rr)
else:
    print('Ошибка! Отсутствует символ #')
# 10
# name = input()
# result = ""
# for char in name:
#     if char.isupper():
#         result += "_" + char.lower()
#     else:
#         result += char
# print(result)
