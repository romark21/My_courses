num = int(input())
ints_count_in_num = 0
even_ints_in_num = 0  #Счётчик чётных цифр
odd_ints_in_num = 0  #Счётчик нечётных цифр
ints_summa_in_num = 0 #Сумма всех цифр
ints_multip_in_num = 1 #Произведение всех цифр
max_int_in_num = 0  # Максимальная цифра в числе
min_int_in_num = 9 # Минимальная цифра в числе
while num > 0:
    last = num % 10 # Берём последнюю цифру
    if max_int_in_num < last:
        max_int_in_num = last # Максимальная цифра в числе
    elif min_int_in_num > last:
        min_int_in_num = last # Минимальная цифра в числе
    ints_count_in_num +=1 #СЧетчик считает кол-во цифр в числе
    ints_summa_in_num += last #Сумма всех цифр
    ints_multip_in_num *= last #Произведение всех цифр
    if last % 2 == 0:
        even_ints_in_num += 1 #Счётчик чётных цифр
    else:
        odd_ints_in_num += 1#Счётчик нечётных цифр
    num //= 10 # Удаляем последнюю цифру из числа

print(f"Количество цифр в числе: {ints_count_in_num}")
print(f"Количество чётных цифр в числе: {even_ints_in_num}")
print(f"Количество нечётных цифр в числе: {odd_ints_in_num}")
print(f"Сумма цифр в числе: {ints_summa_in_num}")
print(f"Произведение цифр в числе: {ints_multip_in_num}")
print(f"Максимальная цифра в числе: {max_int_in_num}")
print(f"Минимальная цифра в числе: {min_int_in_num}")
