# Смоделировать простейший калькулятор, умеющий выпонять 4 основные арифметические операции
while True:
    try:
        x1 = int(input("Первое число"))
        op = input("Операция")
        x2 = int(input("Второе число"))
        break
    except ValueError:
        print("ОШибка")

summa = 0
vichitanie = 0
umn = 0
delen = 0
if op == "+":
    summa = x1 + x2
    print(summa)
elif op == "-":
    vichitanie = x1 - x2
    print(vichitanie)
elif op == "*":
    umn = x1 * x2
    print(umn)
elif op == ":":
    delen = x1 / x2
    print(delen)
else:
    print("ошибка")