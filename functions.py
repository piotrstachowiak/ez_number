import data
import re
import random


def generate_phonebook(phonebook_length: int) -> set:
    """
    Generate set of mobile numbers.


    :param phonebook_length:
    :return:
    """
    ranges_length = 0
    for r in data.ranges:
        ranges_length += len(r)
    phonebook = set()
    while len(phonebook) < phonebook_length:
        ranges_length_copy = ranges_length
        # index is used to pick the range, from which a random number will be picked
        # tried simply merging ranges, but it took waaaaaaaaaaay too long to process
        index = random.choice(range(1, ranges_length + 1))
        for r in data.ranges:
            ranges_length_copy -= len(r)
            if index > ranges_length_copy:
                phonebook.add(random.choice(r))
                break
    return phonebook


def print_user_interface() -> dict:
    """

    :return:
    """
    mode, numbers_amount = None, None
    print("\nWelcome to ez_numbers - mobile numbers that make sense!\n"
          "\nAvailable modes are:\n"
          "1 - The Default - generates 15 numbers in standard format (e.g. \"881 111 881\").\n"
          "2 - The Custom - generates up to 100 numbers (you choose how many!) consisting of a "
          "4-digit pattern and a single digit rest (e.g.: \"6646 1 6646\", \"5335 5335 0\") or in standard format.\n"
          "3 - The Weird - generates up to 100 numbers that are... mostly rather interesting than practical.")
    while True:
        try:
            mode = int(input("\nSelect mode: "))
        except ValueError:
            print("Oops! That was no valid number. Try again!")
        if mode in [1, 2, 201101430, 3]:
            break
        else:
            print("Available mode commands are: 1, 2, 3.")
    if mode == 1:
        numbers_amount = 15
        print("Well done! Processing...\n")
    elif mode == 2 or mode == 3:
        while True:
            try:
                numbers_amount = int(input("\nHow many numbers do you want to get? (1 minimum, 100 maximum): "))
            except ValueError:
                # print("If only Earl Of Lemongrab saw what you just typed...")
                print("Oops! That was no valid number. Try again!")
            if numbers_amount in range(1, 101):
                print("LETS GO! Processing...\n")
                break
    return {
        "mode": mode,
        "numbers_amount": numbers_amount
    }


def handle_user_request(phonebook: set, ez_numbers: list, mode: int, numbers_amount: int):
    """

    :param phonebook:
    :param ez_numbers:
    :param mode:
    :param numbers_amount:
    :return:
    """
    final_data = None
    match mode:
        case 1:
            final_data = divide_phonebook_by_3(phonebook, ez_numbers)
        case 2:
            half_data = divide_phonebook_by_part_length(phonebook, ez_numbers, 4, 2)
            final_data = divide_phonebook_by_3(half_data["phonebook"], half_data["ez_numbers"])
        case 201101430:
            print("\u210c\U0001D508\u210c\U0001D508\u00A0"*2005*random.randint(21, 37))
        case 3:
            half_data = divide_phonebook_by_part_length(phonebook, ez_numbers, 4, 2)
            final_data = divide_phonebook_by_part_length(half_data["phonebook"], half_data["ez_numbers"], 3, 2)
    outcome = sorted(final_data["ez_numbers"], key=lambda number: ((len(set(number))), -len(number.split(' '))))
    print("\n".join(outcome[:numbers_amount]))


def divide_phonebook_by_3(phonebook: set, ez_numbers: list) -> dict:
    """

    :param phonebook:
    :param ez_numbers:
    :return:
    """
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
    return {
        "phonebook": phonebook,
        "ez_numbers": ez_numbers
    }


def divide_phonebook_by_part_length(phonebook: set, ez_numbers: list, part_length: int, matches: int) -> dict:
    """

    :param phonebook:
    :param ez_numbers:
    :param part_length:
    :param matches:
    :return:
    """
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
    return {
        "phonebook": phonebook,
        "ez_numbers": ez_numbers
    }
