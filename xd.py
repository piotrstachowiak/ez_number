import test
import re
import random

phonebook = test.generate_numbers(50000)
ez_numbers = []


def divide_numbers_by_3(phonebook: set, ez_numbers: list) -> tuple:
    for number in phonebook.copy():
        current_number = str(number)
        parts = re.findall(".{3}", current_number)
        for part in parts:
            if len(re.findall(f"{part}", current_number)) >= 2:
                # "if x" removes spaces created by re.split
                current_number = " ".join([x for x in re.split(f"({part})", current_number) if x])
                if len(current_number.split(" ")) < 4:
                    ez_numbers.append(current_number)
                    phonebook.remove(number)
                    break
    return phonebook, ez_numbers


def divide_numbers_by_part_length(phonebook: set, ez_numbers: list, part_length: int, matches: int) -> tuple:
    for number in phonebook.copy():
        current_number = str(number)
        parts = re.findall(f".{{{part_length}}}", current_number)
        for part in parts:
            if len(re.findall(f"{part}", current_number)) >= matches:
                # "if x" removes spaces created by re.split
                current_number = " ".join([x for x in re.split(f"({part})", current_number) if x])
                ez_numbers.append(current_number)
                phonebook.remove(number)
                break
    return phonebook, ez_numbers


def interface():
    user_input, numbers_amount = 0, 0
    while True:
        try:
            user_input = int(input("\nPlease select mode: "))
        except ValueError:
            print("Oops! That was no valid number. Try again!")
        if user_input not in [1, 2, 201101430, 3]:
            print("Available mode commands are: 1, 2, 3.")
        else:
            break

    if user_input == 1:
        print("Well done! Processing...\n")
        divide_numbers_by_3(phonebook, ez_numbers)
        numbers_amount = 15
    elif user_input == 201101430:
        print("\u210c\U0001D508\u210c\U0001D508\u00A0"*2005*random.randint(21, 37))
    elif user_input == 2 or user_input == 3:
        while True:
            try:
                numbers_amount = int(input("\nHow many numbers do you want to get? (100 maximum): "))
            except ValueError:
                # print("If only Earl Of Lemongrab saw what you just typed...")
                print("Oops! That was no valid number. Try again!")
            if numbers_amount in range(1, 101):
                print("LETS GO, processing...\n")
                break
        if user_input == 2:
            aa = divide_numbers_by_part_length(phonebook, ez_numbers, 4, 2)
            divide_numbers_by_3(*aa)
        else:
            divide_numbers_by_part_length(phonebook, ez_numbers, 4, 2)
            divide_numbers_by_part_length(phonebook, ez_numbers, 3, 2)

    outcome = sorted(ez_numbers, key=lambda number: ((len(set(number))), -len(number.split(' '))))
    print("\n".join(outcome[:numbers_amount]))


interface()

# option for user to decide, turns out numbers with 4-digit patterns
# require more information to be remembered (position of the rest)
