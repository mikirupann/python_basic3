line = input("行数を入力してください: ")
column = input("列数を入力してください: ")

for number1 in range(1, (int(line)) + 1):
    for number2 in range(1, (int(column)) + 1):
        print(f" {number2} × {number1} = {str(number1 * number2).rjust(2)}", end=" | ")
    print()
