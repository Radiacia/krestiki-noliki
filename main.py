field = [[" "] * 3 for i in range(3)]
def greet():
    print("||||||||||||Здравствуйте!!!^^||||||||||")
    print("|||||||||||Игра называется|||||||||||||")
    print("|||||||||Крестики(Х)-Нолики(О)|||||||||")
    print("||||||||-----------------------||||||||")
    print("||||||||||Правила следующие:|||||||||||")
    print("||||Форма ввода - две координаты - x y|")
    print("||||||||||x - номер строки|||||||||||||")
    print("||||||||||y - номер столбца||||||||||||")
    print("||||||||||||||Удачи!|||||||||||||||||||")

def show():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

def sho():
    print()
    print("   | 0 | 1 | 2 | ")
    print(" ---------------- ")
    for i,row in enumerate(field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(" ---------------- ")
    print()

def ask():
    while True:
        cords = input("     Ваш ход:").split()
        if len(cords) != 2:
            print("Введите ТОЛЬКО 2 координаты")
            continue

        x,y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите ТОЛЬКО числа")
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты за пределами...")
            continue

        if field[x][y] != " ":
            print("Ячейка занята")
            continue

        return x, y

def check_winner_krestikov():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["X", "X", "X"]:
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["X", "X", "X"]:
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ["X", "X", "X"]:
        return True

    return False

def check_winner_nolikov():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["O", "O", "O"]:
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["O", "O", "O"]:
            return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
    if symbols == ["O", "O", "O"]:
        return True

    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
    if symbols == ["O", "O", "O"]:
        return True

    return False

num = 0
greet()
while True:
    num += 1

    sho()

    if num % 2  == 1:
        print ("Ходит Крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_winner_krestikov():
        print("Победили Крестики")
        break

    if check_winner_nolikov():
        print("Победили Нолики")
        break

    if num == 9:
        print("Ничья")
        break


