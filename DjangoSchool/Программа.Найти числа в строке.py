import re


def main() -> None: # 1-ый способ
    my_string = "dgjt2kg 4564fgh7 kkjl 98"
    numbers = []
    temp = ''
    for i in my_string:
        if i.isdigit():
            temp += i
        elif temp:
            numbers.append(int(temp))
            temp = ''
    if i.isdigit():
        numbers.append(int(i))
    print(numbers)


# main()




def search_number() -> None: # 2-ой способ
    my_string = "dgjt2kg 4564fgh7 kkjl 98"
    nums = re.findall('[0-9]+', my_string)
    print(nums)
    numbers = []
    for i in nums:
        numbers.append(int(i))
    print(numbers)


search_number()



def search() -> None: # 3-ий способ

    my_string = "dgjt2kg 4564fgh7 kkjl 98"
    numbers = [int(i) for i in re.findall('\d+', my_string)]
    print(numbers)

# search()


