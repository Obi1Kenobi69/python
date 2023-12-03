number = int(input("Введите трехзначное число: "))
num1 = number // 100
num2 = (number % 100) // 10
num3 = number % 10

product = num1 * num2 * num3
print("Произведение цифр:", product)
