def main():
    while True:
        intro = input("Вы хотите посчитать кол-во символов в введенном тексте? ")
        if intro == 'да':
                text = input(f"Введите текст: ")
                text_len = len(text)
                print(f'Количество символов в тексте : {text_len}')
                continue
        elif intro == 'нет':
            print("Тогда иди от сюда!!!")
            break




main()