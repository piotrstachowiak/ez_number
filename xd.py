import random
import re
# import pandas

# print(random.randrange(100,200,2))  - trzeci parametr step nie rzumiem

# generator zajętych numerów
# b = {random.randrange(600000000, 900000000) for x in range(1000)}
# print(b)

# d = "15315, 15314, 15152"
# print(re.findall("[0-9]{2}

# c = {re.findall(".2", str(x)) for x in range(100)}
# print(c)


numb = 123456789
# print("\ntestowany numer:", numb)
test = re.findall("7.", str(numb))
# print(test)

# plan: numer na string, pociac w trzyznakowe sekwencje, jesli sekwencja sie powtarza - aukces
test2 = str(numb)[:3]
# print(test2)

test3 = []
# index = len(str(numb))-2
# print(index)

numb3 = numb
while numb3:
    test3.append(str(numb3)[:3])
    numb3 = str(numb3)[3:]
# print("test 3:", test3)

test4 = []
numb4 = str(numb)
while numb4[2:]:
    test4.append(numb4[:3])
    numb4 = numb4[1:]

# print("test 4:", test4)
# za pomocą // 2 ustalić index
# numer podzielic na fragmenty rownej dlugosci według indexu
# gdy index dzieli bez reszty slice jak w test 3 (na ten moment, pozniej porownywanie fragmentow)

# gdy index dzieli z resztą sprawdzić wszystkie możliwe: 6 6666 6661, 6666 6 6661, 6666 6666 1
# wynik dzielenia bez reszty przez index +1 to ilość możliwych pozycji fragmentu wielkości reszty w numerze
# możliwe pozycje reszty: numer[0], numer[index], numer[index*2]...
"""
test5 = []
every = []
numb5 = str(numb)

# długość fragmentu do porównania w pierwszym obiegu pętli
index = len(numb5) // 2

# ilość możliwych miejsc położenia reszty numeru  !!! GDY JEST RESZTA

while index > 1:
    numb5 = str(numb)
    options = len(numb5) // index + 1
    dataset = []
    if options % 2 != 0:
        # to dziala dla 4, potrzebna abstrakcja na inne opcje... czy naprawde?
        # przypadek 4, przypadek 3, przypadek 2 dla  tego problemu

        # implementacja dla dowolnie długich liczb też może być - druga rzecz
        # to by był w sumie generator fajnych liczb xd !!!! do różnych zastosowań (hasła, identyfikacja)
        while options:
            options -= 1
            reminder = numb5[index * options]
            numb5 = numb5[0: index * options] + numb5[index * options + 1:]
            dataset = [
                {
                    options: [
                        reminder,
                        numb5[0:index],
                        numb5[index:]
                    ]
                }
            ]
            test5.append(dataset)
    else:
        while numb5:
            dataset.append(str(numb5)[:index])
            numb5 = str(numb5)[index:]

        test5.append(dataset)
    index -= 1

# print(numb5)
# print(test5)
df = pandas.DataFrame(test5)
# print(df)
"""
# print(numb5[0:index+1:]+numb5[index+2:])
# NIE KASUJ KODU, NIE WARTO XD

test = []
# --- PODZIAŁ NA 4 ---
numb = 999929999
numb4 = str(numb)


def analize_number(number):
    number = str(number)
    fragment_lenght = len(number) // 2
    # wynik dzielenia bez reszty przez fragment_lenght +1 to ilość możliwych pozycji reszty w numerze
    options = len(number) // fragment_lenght + 1
    # możliwe miejsca reszty: numer[fragment_lenght * 0], numer[fragment_lenght * 1], numer[fragment_lenght * 2]
    while options:
        options -= 1
        parts = []
        # numb_copy = number
        reminder = number[fragment_lenght * options]
        main = number[0: fragment_lenght * options] + number[fragment_lenght * options + 1:]
        part_1 = main[0:fragment_lenght]
        part_2 = main[fragment_lenght:]
        if part_1 == part_2:
            parts.extend([part_1, part_2])
            parts.insert(options, reminder)
            return ' '.join(parts)


def recontruct_number(part_1, part_2, reminder, option):
    if option == 2:
        return part_1 + ' ' + part_2 + ' ' + reminder
    elif option == 1:
        return part_1 + ' ' + reminder + ' ' + part_2
    else:
        return reminder + ' ' + part_1 + ' ' + part_2


def div_by_4(numbers):
    # for number in numbers: print("\nEZ:", number) if analize_number(number) else print("uneazy :((")
    for number in numbers:
        ez_number = analize_number(number)
        if ez_number:
            print("\nEZ:", ez_number)

        # dataset = [
        #     {
        #         options + 1: [
        #             reminder,
        #             main[0:fragment_lenght],
        #             main[fragment_lenght:]
        #         ]
        #     }
        # ]
        # test.append(dataset)


# test_numbers = {random.randrange(600000000, 900000000) for x in range(1000)}
# div_by_4(test_numbers)
# div_by_4([999919999, 123412341, 456316328])

nums = [999919999, 123412341, 123456789]


def div_by_4_short(numbers):
    for x in numbers:
        number = str(x)
        parts = [number[:4], number[1:5]]
        # x = re.findall("9999", number)
        for part in parts:
            if len(re.findall(f"{part}", number)) == 2:
                # print(f"{part_1} {number[4:5]} {part_1}")
                print(" ".join([x for x in re.split(f"({part})", number,) if x]))
                break


div_by_4_short(nums)

# y = re.findall(part_2, numb)
# print("{}{}".format(x,y))
# print(f"{x}{y}")


# --- PODZIAŁ NA 3 ---
# numb3 = str(numb)
# dataset = {}
# values = []
# while numb3:
#     values.append(numb3[:3])
#     numb3 = numb3[3:]
# dataset.update({"0": })
# test.append(dataset)

# --- PODZIAŁ NA 2 ---
# numb2 = str(numb)
# fragment_lenght = 2
# options = 1 + len(numb2) // fragment_lenght
# while options:
#     options -= 1
#     reminder = numb2[fragment_lenght * options]
#     main = numb2[0: fragment_lenght * options] + numb2[fragment_lenght * options + 1:]
#     dataset = [
#         {
#             options + 1: [
#                 reminder,
#                 re.findall('..', main)
#             ]
#         }
#     ]
#     test.append(dataset)

#
# dataframe = pandas.DataFrame(test)
# print(dataframe)
