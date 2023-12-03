num = int(input("Введите трехзначное число: "))
sum = num % 10 + num // 10 % 10 + num // 100
print("Сумма цифр в числе:", sum)
