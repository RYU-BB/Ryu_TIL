def menu_print():
    print("도형을 선택하세요")
    print("1. N단 케이크")
    print("2. 번개")
    print("3. 종료")


def cake():
    while True:
        print("N단 케이크의 N입력")
        print("(1이상 10이하의 N 입력) : ", end="")
        cake_n = int(input())

        if 0 < cake_n < 11:
            for i in range(cake_n):
                for j in range(2):
                    print("    " * (cake_n - 1 - i), end="")
                    print("*" * (1 + 4 * i) * 2)
            break
        else:
            print("1이상 10이하의 숫자를 입력해주세요.")


def thunder():
    while True:
        print("번개의 밑변 길이")
        print("(3이상 10이하의 길이 입력) : ")
        thunder_n = int(input())

        if 2 < thunder_n < 11:
            for i in range(1, thunder_n + 1):
                print(" " * (thunder_n - i), end="")
                if i == thunder_n:
                    print("*" * thunder_n * 2)
                else:
                    print("*" * thunder_n)

            for i in range(1, thunder_n):
                print(" " * (thunder_n - i), end="")
                print("*" * thunder_n)
            break
        else:
            print("3이상 10이하의 숫자를 입력해주세요.")


while True:
    menu_print()
    menu_num = int(input())

    if menu_num == 1:
        cake()

    elif menu_num == 2:
        thunder()

    elif menu_num == 3:

        break

    else:
        print("메뉴를 다시 선택해주세요.")
