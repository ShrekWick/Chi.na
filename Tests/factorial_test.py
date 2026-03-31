# a = 0
# b = 1
# c = 0
# counter = 0
# while counter<101:
#     print(a)
#     c = a
#     a = b
#     b = b+c
#     counter +=1


def factorial(x):
    res = 1
    for x in range(1,x+1):
        res = res * x
    return(res)

# try:
#     print(factorial(int(input("Факториал какого числа ты хотел бы узнать? "))))
# except ValueError:
#     print("Нафига тебе столько? Меньше знаешь крепче спишь")

print(factorial(1559))