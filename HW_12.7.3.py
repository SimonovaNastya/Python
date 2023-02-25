per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = []

for i in per_cent:
    result = int(money / 100 * per_cent[i])
    deposit.append(result)

print(deposit)
print('Максимальная сумма, которую вы можете заработать — ' + str(max(deposit)))