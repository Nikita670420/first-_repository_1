import random, time

number = random.randint(1, 1000)
print('Я загадал число от 1, до 1000. Попробуй его отгадать!')
while True:
    try:
        time.sleep(1)
        answer = int(input('\nТвой вариант: '))
        if answer == number:
            print(f'Ты угадал! Моё число и вправду {number}')
            break
        elif answer > number:
            print('Хорошая попытка, но моё число меньше!')
        else:
            print('Хорошая попытка, но моё число больше!')
    except ValueError:
        print(f'\nОй-ой! Вы написали свой вариант, но ваш вариант, это не целое число! Давайте попробуем ещё раз\n')