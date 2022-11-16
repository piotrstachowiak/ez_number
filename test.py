import random, time
from functools import reduce
from itertools import chain

# print(random.randrange(1, 9))
start = time.time()
# ranges = list(chain(

#pomysl
#suma dlugosci przedzialow
#z tego random
#random to index
#wyszukujemy w ktorym przedziale ten index jest
#w tym przedziale randomujemy

# ranges = (
#     range(450000000, 452999999),
#     range(459000000, 459999999),
#     range(500000000, 519999999),
#     range(530000000, 539999999),
#     range(570000000, 571499999),
#     range(572000000, 573499999),
#     range(573900000, 579429999),
#     range(579500000, 579579999),
#     range(579600000, 579999999),
#     range(600000000, 609999999),
#     range(660000000, 669999999),
#     range(690000000, 690699999),
#     range(690800000, 699999999),
#     range(720000000, 739899999),
#     range(739910000, 739939999),
#     range(780000000, 780299999),
#     range(780700000, 780899999),
#     range(781000000, 785999999),
#     range(786080000, 786089999),
#     range(786100000, 786299999),
#     range(786500000, 799599999),
#     range(799700000, 799999999),
#     range(880000000, 882999999),
#     range(882200000, 882299999),
#     range(883000000, 889999999)
# )

ranges = (
    range(10, 20),
    range(30, 40)
)

ranges_length = 0
for r in ranges: ranges_length += len(r)
print(ranges_length)

index = random.choice(range(1, ranges_length + 1))
print(index)

# print(ranges_length - index)
for r in ranges:
    ranges_length -= len(r)
    if index > ranges_length:
        print(r)
        break

# print(*range(1,21))

# merged_ranges = functools.reduce(lambda a, b: a + b, ranges)
# print(ranges)
# b = {random.randrange(*ranges) for x in range(1000)}
# print(type(ranges))


# # ty Sumukh Barve https://stackoverflow.com/questions/33730396/how-to-generate-random-integers-with-multiple-ranges
# def randomPicker(howMany, *ranges):
#     mergedRange = reduce(lambda a, b: a + b, ranges)
#     ans = []
#     for i in range(howMany):
#         ans.append(random.choice(mergedRange))
#     return ans
#
#
# print(randomPicker(10, ranges))
# start = time.time()
# print(random.choices(ranges, k=30000))
stop = time.time()
# print(lenght)
print(stop-start)
