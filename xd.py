import re
from test import generate_numbers
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

nums = [999919999, 123412341, 123456789, 999999999, 234523523]


def div_by_4_short(numbers):
    for x in numbers:
        number = str(x)
        # in 9-digit numbers 4 digit pattern must occur in the first 5 digits if it is to occur again
        # parts = [number[:4], number[1:5]]
        # x = re.findall("9999", number)
        parts = re.findall(".{4}", number)
        for part in parts:
            if len(re.findall(f"{part}", number)) >= 2:
                # print(f"{part_1} {number[4:5]} {part_1}")
                # "if x" removes spaces
                print(" ".join([x for x in re.split(f"({part})", number) if x]))
                break


# div_by_4_short(nums)


# --- PODZIAŁ NA 3 ---

phonebook = generate_numbers(50000)
ez_numbers = []


def div_by_3(numbers):
    for x in numbers.copy():
        number = str(x)
        parts = re.findall(".{3}", number)
        for part in parts:
            if len(re.findall(f"{part}", number)) >= 2:
                # print(f"{part_1} {number[4:5]} {part_1}")
                # "if x" removes spaces
                number = " ".join([x for x in re.split(f"({part})", number) if x])
                if len(number.split(" ")) < 4:
                    ez_numbers.append(number)
                    phonebook.remove(x)
                    break
        # for part in parts:
        #     if len(re.findall(f"{part}", number)) == 2:
        #         print(part)
    #     while number:
    #         values.append(number[:3])
    #         number = number[3:]
    #     dataset.update({"0": values})
    #     test.append(dataset)
    # print("\n",test)


def div_by_2(numbers):
    for x in numbers:
        number = str(x)
        parts = re.findall(".{2}", number)
        # print(parts)
        for part in parts:
            if len(re.findall(f"{part}", number)) >= 3:
                # print(f"{part_1} {number[4:5]} {part_1}")
                # "if x" removes spaces
                print(" ".join([x for x in re.split(f"({part})", number) if x]))
                break


def div_by_part_lenght(numbers, part_length, matches_number):
    for x in numbers.copy():
        number = str(x)
        parts = re.findall(f".{{{part_length}}}", number)
        # parts = re.compile(f".{{{part_length}}}")
        # print(parts.pattern)
        # parts = re.compile(".{4}")
        # print(parts.pattern)

        # print(re.findall(f".{part_length}", number))
        # print(parts)
        for part in parts:
            if len(re.findall(f"{part}", number)) >= matches_number:
                # print(f"{part_1} {number[4:5]} {part_1}")
                # "if x" removes spaces
                number = " ".join([x for x in re.split(f"({part})", number) if x])
                if len(number.split(" ")) < 4:
                    ez_numbers.append(number)
                    phonebook.remove(x)
                # ez_numbers.append(" ".join([x for x in re.split(f"({part})", number) if x]))
                break


user_input, numbers_amount = 0, 0

while True:
    try:
        user_input = int(input("\nPlease enter a number (1, 2, or 3): "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    if user_input in [1, 2, 3, 201101430]:
        break

if user_input == 1:
    print("Well done! Processing...")
    div_by_3(phonebook)
    numbers_amount = 25
elif user_input == 2:
    while True:
        try:
            user_input = int(input("\nHow many numbers do you want to get? (100 maximum): "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        if numbers_amount in range(1, 101):
            # print("If Earl Of Lemongrab saw what you just... UNACCEPTABLE!")
            print("LETS GO, processing...")
            break

    div_by_part_lenght(phonebook, 4, 2)
    div_by_part_lenght(phonebook, 3, 2)

outcome = sorted(ez_numbers, key=lambda number: ((len(set(number))), -len(number.split(' '))))
print("\n".join(outcome[:numbers_amount]))

# option for user to decide, turns out numbers with 4-digit patterns
# require more information to be remembered (position of the rest)
