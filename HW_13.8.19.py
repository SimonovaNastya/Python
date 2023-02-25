tickets = int(input("Введите количество билетов:"))
summ = 0

for i in range(1, tickets + 1):
    age = int(input("Введите возраст посетителя №: " + str(i)))
    if 18 <= age < 25:
        summ += 990
    elif age >= 25:
        summ += 1390

if tickets > 3:
    summ -= (summ / 100 * 10)

print("Сумма к оплате: " + str(summ))