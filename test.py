import random

# ranges of mobile phones numbers in Poland according to Wikipedia
ranges = (
    range(450000000, 452999999),
    range(459000000, 459999999),
    range(500000000, 519999999),
    range(530000000, 539999999),
    range(570000000, 571499999),
    range(572000000, 573499999),
    range(573900000, 579429999),
    range(579500000, 579579999),
    range(579600000, 579999999),
    range(600000000, 609999999),
    range(660000000, 669999999),
    range(690000000, 690699999),
    range(690800000, 699999999),
    range(720000000, 739899999),
    range(739910000, 739939999),
    range(780000000, 780299999),
    range(780700000, 780899999),
    range(781000000, 785999999),
    range(786080000, 786089999),
    range(786100000, 786299999),
    range(786500000, 799599999),
    range(799700000, 799999999),
    range(880000000, 882999999),
    range(882200000, 882299999),
    range(883000000, 889999999)
)


def generate_numbers(amount: int) -> set:
    ranges_length = 0
    for r in ranges:
        ranges_length += len(r)
    numbers = set()
    while len(numbers) < amount:
        ranges_length_copy = ranges_length
        # index is used to pick the range from which a random number will be picked
        # tried simply merging ranges, but it took waaaaaaaaaay too long to process
        index = random.choice(range(1, ranges_length + 1))
        for r in ranges:
            ranges_length_copy -= len(r)
            if index > ranges_length_copy:
                numbers.add(random.choice(r))
                break
    return numbers
