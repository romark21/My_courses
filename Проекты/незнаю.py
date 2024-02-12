def check_user_input(input):
        try:
            val = float(input)
            return val
        except ValueError:
            print(f"Ошибка ввода")


def add_income():

    money_income = float(input('Введите сумму: '))
    description_income = input('Добавтье описание дохода: ')
    print()
    return money_income, description_income

def add_outcome():

    money_outcome = input('Введите сумму: ')
    check_user_input(money_outcome)


        #     return float(money_outcome)
        # except ValueError:
        #     print(f"Ошибка ввода {money_outcome}")

    description_outcome = input('Добавтье описание расхода: ')
    print()
    return money_outcome, description_outcome

def main():
    wallet_income = {}
    wallet_outcome = {}
    outcome_summa = 0
    income_summa = 0

    while True:
        comands = input("1 - Добавить доход\n2 - Добавить расход\n3 - Посмотреть 'Доходы и Расходы'\n Введите команду: ")
        print()

        if comands == '1':
            money_income, description_income = add_income()
            wallet_income[money_income] = description_income

        elif comands == '2':
            money_outcome, description_outcome = add_outcome()
            wallet_outcome[money_outcome] = description_outcome

        elif comands == '3':
            print("Ваши доходы:")
            for i, j in wallet_income.items():
                income_summa += i
                print(f'{i}€ - {j}')
                print()

            print("Ваши расходы:")
            for i, j in wallet_outcome.items():
                outcome_summa += i
                print(f'{i}€ - {j}')
                print()

            print(f'Ваши доходы: {income_summa}€')
            print(f'Ваши расходы: {outcome_summa}€')


if __name__ == '__main__':
    main()
