line = input("行数を入力してください: ")
column = input("列数を入力してください: ")

for number1 in range(1, int(line)):
    for number2 in range(1, int(column)):
        print(f" {number2} × {number1} = {number1 * number2} |", end="")
    print()
