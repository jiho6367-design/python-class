"""여러 종류의 음료를 복수로 선택할 수 있는 자판기 프로그램입니다."""


def show_menu(drinks):
    """자판기 음료 메뉴를 출력합니다."""
    print("\n========== 음료 자판기 ==========")
    for number, drink in drinks.items():
        print(
            f"{number}. {drink['name']} - {drink['price']:,}원 "
            f"(재고: {drink['stock']}개)"
        )
    print("0. 선택 완료")
    print("=================================")


def input_money():
    """올바른 금액을 입력할 때까지 다시 입력받습니다."""
    while True:
        try:
            money = int(input("투입할 금액을 입력하세요: "))
            if money > 0:
                return money
            else:
                print("0원보다 큰 금액을 입력해 주세요.")
        except ValueError:
            print("금액은 숫자로 입력해 주세요.")


def input_quantity():
    """올바른 수량을 입력할 때까지 다시 입력받습니다."""
    while True:
        try:
            quantity = int(input("구매할 수량을 입력하세요: "))
            if quantity > 0:
                return quantity
            else:
                print("수량은 1개 이상 입력해 주세요.")
        except ValueError:
            print("수량은 숫자로 입력해 주세요.")


def main():
    drinks = {
        "1": {"name": "콜라", "price": 1000, "stock": 10},
        "2": {"name": "사이다", "price": 1000, "stock": 10},
        "3": {"name": "오렌지주스", "price": 1500, "stock": 10},
        "4": {"name": "생수", "price": 700, "stock": 10},
        "5": {"name": "캔커피", "price": 1200, "stock": 10},
    }

    selected_drinks = {}
    money = input_money()
    remaining_money = money

    while True:
        show_menu(drinks)
        print(f"현재 잔액: {remaining_money:,}원")
        choice = input("음료 번호를 선택하세요: ").strip()

        if choice == "0":
            break
        elif choice not in drinks:
            print("메뉴에 있는 번호를 선택해 주세요.")
        else:
            drink = drinks[choice]
            quantity = input_quantity()
            total_price = drink["price"] * quantity

            if quantity > drink["stock"]:
                print(f"재고가 부족합니다. 현재 재고는 {drink['stock']}개입니다.")
            elif total_price > remaining_money:
                print(
                    f"잔액이 부족합니다. {total_price - remaining_money:,}원이 더 필요합니다."
                )
            else:
                drink["stock"] -= quantity
                remaining_money -= total_price

                if choice in selected_drinks:
                    selected_drinks[choice] += quantity
                else:
                    selected_drinks[choice] = quantity

                print(
                    f"{drink['name']} {quantity}개를 선택했습니다. "
                    f"남은 금액은 {remaining_money:,}원입니다."
                )

    print("\n========== 음료 생산 ==========")
    if selected_drinks:
        for number, quantity in selected_drinks.items():
            drink_name = drinks[number]["name"]
            print(f"{drink_name} {quantity}개가 나왔습니다.")
    else:
        print("선택한 음료가 없습니다.")

    used_money = money - remaining_money
    print(f"총 사용 금액: {used_money:,}원")
    print(f"거스름돈: {remaining_money:,}원")
    print("이용해 주셔서 감사합니다.")


if __name__ == "__main__":
    main()
