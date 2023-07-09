# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def output() -> None:
    name: str = "yoko"
    print(f"おはよう{name}さん")


def data_type() -> None:
    # type確認(int,str)
    print(type(3))
    print(type(3.0))
    print(type("Hello"))

    # 計算
    print(2 + 2)
    print((50 - 5 * 6) / 4)  # 割り算は常にfloat
    print(17 // 3)  # 商
    print(17 % 3)  # 余り
    print(5 ** 2)  # 5の2乗

    print("Hello" + " World!")
    print(3 * 'Hello')

    # 型変換
    print(3 * int("3"))
    print(4.0 + float("4.0"))
    print("x:" + str(43))


def variable() -> None:
    # Pythonは動的(その値を蓄えることができ再利用できる。意味を持たせられる)
    name: str = input("名前は何ですか")
    print(f"おはよう{name}さん")


def bifurcation_process() -> None:
    # FizzBuzz(and or not)
    fizz: int = 10
    if fizz % 3 == 0 and fizz % 5 == 0:
        print("FizzBuzz")
    elif fizz % 3 == 0:
        print("Fizz")
    elif fizz % 5 == 0:
        print("Buzz")
    else:
        print(fizz)


def iterative_process() -> None:
    # while文（0から10の偶数出力）
    a: int = 0
    while a <= 10:
        print(a, end=',')
        a = a + 2
    print()
    print("--------")
    # for,range文(1から20までの数字でFizzBuzz)
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def break_continue() -> None:
    # break文(2で割れる数が来たら直近のfor文を抜ける)
    for num in range(1, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            break
        print("Found an odd number", num)

    print("---------")

    # continue文(continue以下をskipして次に進める)
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found an odd number", num)


def calc_price(cost_price: int, tax: float) -> int:
    price: float = cost_price * tax
    return int(price)


def sequence() -> None:
    # リスト(0,始まり)
    list_1: list = []
    list_1.append(216)  # 末尾に追加
    list_1.insert(0, "x")  # 先頭に追加
    print(list_1)
    list_2: list = [3, "test", 5]
    print(list_2[1])  # アクセス
    list_2.pop(1)  # 削除

    for i in list_2:
        print(i)

    # タプル(変更できない)
    tuple_1: tuple = (10, 100)
    print(tuple_1[0])
    for i in tuple_1:
        print(i)

    # 辞書
    tel_1: dict = {}
    tel_1["Jack"] = 443  # 追加
    tel_1["Tom"] = 559  # 追加
    print(tel_1)
    del tel_1["Jack"]
    print(tel_1)
    tel_2: dict = {'yoko': 1001, 'kotobuki': '0221'}
    for k, v in tel_2.items():
        print(k, v)


def error_except() -> None:
    try:
        x: int = int(input("Please enter a number: "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


class Character:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp

    def show_status(self):
        print(f"name:{self.name} HP:{self.hp} MP:{self.mp}")

    def attack(self):
        print(f"{self.name}は敵に攻撃")

    def damage(self, damage_value):
        print(f"{self.name}はダメージを受けた")
        self.hp = self.hp - damage_value


class Wizard(Character):
    def magic(self, use_mp: int):
        self.attack()
        self.mp = self.mp - use_mp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('---出力---')
    output()
    print('---データ型---')
    data_type()
    print('---変数---')
    variable()
    print('---分岐処理---')
    bifurcation_process()
    print('---繰り返し処理---')
    iterative_process()
    print('---break,continue---')
    break_continue()
    print('---関数---')
    ans = calc_price(100, 1.1)
    print(ans)
    print('---リスト、タプル、辞書---')
    sequence()
    print('---例外処理---')
    error_except()
    print('---クラス---')
    warrior: Character = Character("戦士", 40, 10)
    warrior.show_status()
    warrior.attack()
    warrior.damage(10)
    warrior.show_status()

    magician: Wizard = Wizard("魔法使い", 20, 50)
    magician.show_status()
    magician.magic(50)
    magician.show_status()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
