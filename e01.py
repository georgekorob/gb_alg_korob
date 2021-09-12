# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import namedtuple
from random import uniform

Company = namedtuple('Company', ['q1', 'q2', 'q3', 'q4'])

company_dic = {'company_1': Company(
                q1=uniform(1, 20),
                q2=uniform(1, 20),
                q3=uniform(1, 20),
                q4=uniform(1, 20)
            ), 'company_2': Company(
                q1=uniform(1, 20),
                q2=uniform(1, 20),
                q3=uniform(1, 20),
                q4=uniform(1, 20)
            ), 'company_3': Company(
                q1=uniform(1, 20),
                q2=uniform(1, 20),
                q3=uniform(1, 20),
                q4=uniform(1, 20)
            ), 'company_4': Company(
                q1=uniform(1, 20),
                q2=uniform(1, 20),
                q3=uniform(1, 20),
                q4=uniform(1, 20)
            )}

n = int(input("Введите количество предприятий: "))

for i in range(n):
    name = input(f'Введите наименование {i + 1} предприятие: ')
    profit_q = [float(input(f'Прибыль за {q} квартал: ')) for q in range(1, 5)]
    company_dic[name] = Company(q1=profit_q[0], q2=profit_q[1], q3=profit_q[2], q4=profit_q[3])

year_profit = {name: sum(profit) for name, profit in company_dic.items()}
average_profit = sum(year_profit.values()) / len(year_profit)
print(f'Средняя прибыль предприятий: {average_profit:.6f}')

print('Предприятия, у которых прибыль выше среднего:')
for name, profit in year_profit.items():
    if profit >= average_profit:
        print(f'{name}\t{profit:.6f}')

print('Предприятия, у которых прибыль выше среднего:')
for name, profit in year_profit.items():
    if profit < average_profit:
        print(f'{name}\t{profit:.6f}')

# Вывод
# Введите количество предприятий: 2
# Введите наименование 1 предприятие: lukoil
# Прибыль за 1 квартал: 18
# Прибыль за 2 квартал: 17
# Прибыль за 3 квартал: 15
# Прибыль за 4 квартал: 16
# Введите наименование 2 предприятие: gazprom
# Прибыль за 1 квартал: 19
# Прибыль за 2 квартал: 18
# Прибыль за 3 квартал: 17
# Прибыль за 4 квартал: 14
# Средняя прибыль предприятий: 49.200460
# Предприятия, у которых прибыль выше среднего:
# company_2	51.798399
# company_4	50.946123
# lukoil	66.000000
# gazprom	68.000000
# Предприятия, у которых прибыль выше среднего:
# company_1	33.350822
# company_3	25.107418
